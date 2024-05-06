import os
from sqlalchemy import create_engine, text  # text をインポート
from sqlalchemy.orm import sessionmaker, declarative_base

# 環境変数からDB接続情報を取得
DB_ENDPOINT = os.getenv("DB_ENDPOINT", "")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USERNAME = os.getenv("DB_USERNAME", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "raretech_library")
DB_CHARSET = os.getenv("DB_CHARSET", "utf8")

# RDSを使用するように変更（CDKにて設定しているurlを使用している）
DB_URL = f"mysql+mysqldb://{DB_USERNAME}:{DB_PASSWORD}@{DB_ENDPOINT}:{DB_PORT}/{DB_NAME}?charset={DB_CHARSET}"

# Unix ソケットを無効にする設定を削除
engine = create_engine(DB_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_context(request):
    db = next(get_db()) # ジェネレータからセッションを取得し、確実に開始します。
    try:
        # シンプルなSELECTクエリを行う例
        result = db.execute(text("SELECT 1"))
        print(result.fetchall())  # デバッグ用に結果を表示
        return {"db": db, "request": request}
    finally:
        db.close() # リクエストが完了したらセッションをクローズします.
