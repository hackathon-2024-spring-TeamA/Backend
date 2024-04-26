# Ruby on Railsのマイグレーションファイルとは異なり、段階的でなく、一括でデータベースの状態をリセットしている。
# 必要なスクリプトは、docker-compose exec app poetry run python -m app.migrate_db
from sqlalchemy import create_engine

from app.models.task import Base

# データベースの接続情報を定義します。
DB_URL = "mysql+pymysql://root@db:3306/raretech_library?charset=utf8"
# create_engine関数を使用して、データベース接続エンジンを作成します。
# echo=TrueはSQLの実行ログをコンソールに出力するための設定です。
engine = create_engine(DB_URL, echo=True)

# reset_database関数はデータベースのテーブルをリセットするための関数です。
def reset_database():
    # Base.metadata.drop_allは、Baseに登録されたすべてのテーブルを削除します。
    Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_allは、Baseに登録されたすべてのテーブルを作成します。
    Base.metadata.create_all(bind=engine)

# スクリプトが直接実行された場合にreset_database関数を実行します。
if __name__ == "__main__":
    reset_database()
