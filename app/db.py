from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy.orm import sessionmaker, declarative_base

# 使用するデータベースのURLを定義します。この例ではMySQLを使用し、aiomysqlドライバを介して非同期で接続します。
# データベースユーザーはroot、データベース名はraretech_library、使用するポートは3306、文字コードはutf8です。
ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/raretech_library?charset=utf8"

# 上記のURLを使用して非同期エンジンを作成します。echo=TrueはSQL実行時のログを出力するための設定です。
async_engine = create_async_engine(ASYNC_DB_URL, echo=True)

# sessionmakerは、データベースセッションを作成するためのファクトリ関数です。
# ここでは非同期セッションAsyncSessionを使い、自動コミットを無効にし、自動フラッシュも無効に設定します。
# セッションは上で作成した非同期エンジンにバインドされます。
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

# declarative_base()は、SQLAlchemyでORMを利用する際に、ベースクラスを作成するための関数です。
# このベースクラスを継承して、データベースのテーブルに対応するPythonクラスを定義します。
Base = declarative_base()

# get_dbは、データベースセッションを提供する非同期ジェネレータ関数です。
# この関数はFastAPIの依存関係として使用され、リクエストの処理中にデータベースセッションを利用できるようにします。
async def get_db():
    async with async_session() as session:
        yield session
