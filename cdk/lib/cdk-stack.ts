// AWS CDKのコアライブラリと、使用するAWSサービスを一括でインポートします。
import { aws_ec2 as ec2, aws_ecs as ecs, aws_elasticloadbalancingv2 as elbv2, aws_logs as logs, aws_ecr_assets as ecr_assets, Stack, StackProps, App } from 'aws-cdk-lib';

export class CdkStack extends Stack {
  constructor(scope: App, id: string, props?: StackProps) {
    super(scope, id, props);

    // VPCを作成します。ここでパブリックサブネットを定義しています。
    const vpc = new ec2.Vpc(this, 'Vpc', {
      subnetConfiguration: [
        {
          cidrMask: 24,
          name: 'public',
          subnetType: ec2.SubnetType.PUBLIC,
        }
      ]
    });

    // セキュリティグループを作成します。1つはELB用、もう1つはアプリケーション用です。
    // 第三引数にはこのセキュリティグループが属するVPCのオブジェクト。vpcは上記で指定したVPCコンストラクタについた名前
    const securityGroupELB = new ec2.SecurityGroup(this, 'SecurityGroupELB', { vpc });
    securityGroupELB.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(80), 'Allow HTTP traffic from anywhere');

    const securityGroupAPP = new ec2.SecurityGroup(this, 'SecurityGroupAPP', { vpc });
    // デフォルトですべてのインバウンドトラフィックを拒否している

    // アプリケーションロードバランサーを作成します。インターネットからアクセス可能に設定しています。
    const alb = new elbv2.ApplicationLoadBalancer(this, 'ALB', {
      vpc,
      securityGroup: securityGroupELB,
      internetFacing: true // インターネットからのアクセスが可能
    });
    const listenerHTTP = alb.addListener('ListenerHTTP', {
      port: 80,
    });

    // ターゲットグループを作成し、ヘルスチェックの設定を行います。
    const targetGroup = new elbv2.ApplicationTargetGroup(this, 'TG', {
      vpc,
      port: 8888, //ここをアプリに合わせて変更
      protocol: elbv2.ApplicationProtocol.HTTP,
      targetType: elbv2.TargetType.IP,
      healthCheck: {
        path: '/docs', // ヘルスチェックのパスに変更
        healthyHttpCodes: '200',
      },
    });

    listenerHTTP.addTargetGroups('DefaultHTTPSResponse', {
      targetGroups: [targetGroup]
    });

    // ECSクラスターを作成します。
    const cluster = new ecs.Cluster(this, 'Cluster', {
      vpc,
    });

    // Fargateタスク定義を作成し、コンテナを追加します。
    // ここだけでECRレポジトリの作成
    // docker build
    // docker tag
    // docker push(ECRレポジトリへpush)
    // タスク定義へdocker uriの登録
    // タスク定義の更新が行われている
    const fargateTaskDefinition = new ecs.FargateTaskDefinition(this, 'TaskDef', {
      memoryLimitMiB: 1024,
      cpu: 512,
      runtimePlatform: {
        cpuArchitecture: ecs.CpuArchitecture.X86_64,  // CPUアーキテクチャを指定
        operatingSystemFamily: ecs.OperatingSystemFamily.LINUX,  // OSファミリーを指定
      }
    });
    const container = fargateTaskDefinition.addContainer('NextAppContainer', {
      image: ecs.ContainerImage.fromAsset('../', { // Dockerファイルの場所を指定し、プラットフォームも指定
        platform: ecr_assets.Platform.LINUX_AMD64, // プラットフォームを指定
      }),
      logging: ecs.LogDrivers.awsLogs({
        streamPrefix: 'app', // appの名前
        logRetention: logs.RetentionDays.ONE_MONTH,
      }),
    });
    container.addPortMappings({
      containerPort: 8888, // コンテナのポートも8888に設定
      hostPort: 8888
    });

    // Fargateサービスを作成し、ターゲットグループに接続します。
    const service = new ecs.FargateService(this, 'Service', {
      cluster,
      taskDefinition: fargateTaskDefinition,
      desiredCount: 1,
      assignPublicIp: true,
      securityGroups: [securityGroupAPP]
    });
    service.attachToApplicationTargetGroup(targetGroup);
  }
}
