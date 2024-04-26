# DockerHubから使いたいDockerイメージを選んで使用する
FROM python:3.11

# コンテナ側にappディレクトリを作成して、移動してコマンドを実行する
WORKDIR /app

# poetry(ライブラリや依存関係を管理するやつ)をインストール
RUN pip install --no-cache-dir poetry

# pyproject.tomlとpoetry.lockファイルをコピー
COPY pyproject.toml poetry.lock* ./

# poetryで依存関係をインストール
RUN poetry install --no-root

# アプリケーションのソースコードをコンテナにコピー
COPY . .

# コマンドを設定。UvicornでFastAPIアプリケーションを起動
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8888", "--reload"]
