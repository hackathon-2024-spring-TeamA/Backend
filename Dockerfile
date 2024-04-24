# DockerHubから使いたいDockerイメージを選んで使用する
FROM python:3.11

# コンテナ側にappディレクトリを作成して、移動してコマンドを実行する
WORKDIR /app

# # ホスト側のコンテキスト（dockerを実行するディレクトリ的な）にあるrequirements.txtをコンテナの中ににコピー
COPY requirements.txt .
# requirements.txtの中にある必要なものをpipを使ってコンテナの中にインストールしている
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8888", "--reload"]