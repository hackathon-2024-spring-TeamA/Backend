// AWS CDKのコアライブラリと、使用するAWSサービスを一括でインポートします。
import { aws_ec2 as ec2, aws_ecs as ecs, aws_elasticloadbalancingv2 as elbv2, aws_logs as logs, aws_ecr_assets as ecr_assets, aws_rds as rds, Stack, StackProps, App, RemovalPolicy } from 'aws-cdk-lib';

export class NewCdkStack extends Stack {
  constructor(scope: App, id: string, props?: StackProps) {
    super(scope, id, props);

    // VPCを作成します。ここでパブリックサブネットを定義しています。
    const vpc = new ec2.Vpc(this, 'Vpc', {
      maxAzs: 2, // 2つのアベイラビリティゾーンにまたがる
      subnetConfiguration: [
        {
          cidrMask: 24,
          name: 'public',
          subnetType: ec2.SubnetType.PUBLIC,
        },
        {
          cidrMask: 24,
          name: 'private',
          subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
        }
      ]
    });

    // 第三引数にはこのセキュリティグループが属するVPCのオブジェクト。vpcは上記で指定したVPCコンストラクタについた名前
    const securityGroupELB = new ec2.SecurityGroup(this, 'SecurityGroupELB', { vpc });
    securityGroupELB.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(80), 'Allow HTTP traffic from anywhere');

    // アプリケーション用のセキュリティグループ
    const securityGroupAPP = new ec2.SecurityGroup(this, 'SecurityGroupAPP', { vpc });
    // デフォルトですべてのインバウンドトラフィックを拒否している

    // RDS用のセキュリティグループ
    const securityGroupRDS = new ec2.SecurityGroup(this, 'SecurityGroupRDS', { vpc });

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
      memoryLimitMiB: 512,
      cpu: 256,
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

    // RDSインスタンスを作成します。
    const rdsInstance = new rds.DatabaseInstance(this, 'RDSInstance', {
      engine: rds.DatabaseInstanceEngine.mysql({ version: rds.MysqlEngineVersion.VER_8_0_34 }),
      instanceType: ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
      credentials: rds.Credentials.fromGeneratedSecret('admin'), // 'admin' is the username
      vpc,
      multiAz: true,
      securityGroups: [securityGroupRDS],
      vpcSubnets: {
        subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
      },
      allocatedStorage: 20,
      maxAllocatedStorage: 100,
      publiclyAccessible: false,
      removalPolicy: RemovalPolicy.DESTROY,
      databaseName: 'raretech_library',
    });

    // 環境変数の設定
    const dbEndpoint = rdsInstance.instanceEndpoint.hostname;
    const dbPort = rdsInstance.instanceEndpoint.port.toString();
    const dbUsername = 'admin';
    // シークレットの取得:rdsInstanceにはsecretプロパティがあり、このプロパティからシークレットにアクセスできます。
    const dbPassword = rdsInstance.secret?.secretValueFromJson('password')?.unsafeUnwrap() || '';
    const dbName = 'raretech_library';

    // ECSの環境変数にRDSの情報を設定
    container.addEnvironment('DB_ENDPOINT', dbEndpoint);
    container.addEnvironment('DB_PORT', dbPort);
    container.addEnvironment('DB_USERNAME', dbUsername);
    container.addEnvironment('DB_PASSWORD', dbPassword);
    container.addEnvironment('DB_NAME', dbName);
    container.addEnvironment('DB_CHARSET', 'utf8');

    // セキュリティグループのルールを追加。アプリケーションからRDSへのアクセス、RDSのセキュリティグループにも同様のルールを設定
    securityGroupAPP.addIngressRule(securityGroupRDS, ec2.Port.tcp(3306), 'Allow MySQL traffic from app to RDS');
    securityGroupAPP.addIngressRule(securityGroupRDS, ec2.Port.tcp(3306), 'Allow MySQL traffic from RDS to app');
  }
}

const app = new App();
new NewCdkStack(app, 'NewCdkStack');  // スタック名を変更
app.synth();

