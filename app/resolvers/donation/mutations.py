from ariadne import MutationType, QueryType
from app.models import BookInformation
from app.main import logger

mutation = MutationType()
query = QueryType()

# 本の情報を保存
@mutation.field("addBook")
def resolve_add_book(_, info, title, authors, isbn_number, published_date, description, image_path):
    # TODO: isbnが既に存在すれば登録をスキップ
    db = info.context["db"]
    new_book = BookInformation(
        isbn_number=isbn_number,
        title=title,
        author=authors,
        published_date=published_date,
        description=description,
        image_path=image_path,
    )
    logger.info("##############################################")
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# 全book_informationテーブルのレコード全取得
@query.field("getAllBooks")
def resolve_books(_, info):
    db = info.context["db"]
    books = db.query(BookInformation).all()
    return books
