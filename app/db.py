from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "mysql+mysqldb://root@db:3306/raretech_library?charset=utf8"

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
        return {"db": db, "request": request}
    finally:
        db.close() # リクエストが完了したらセッションをクローズします。