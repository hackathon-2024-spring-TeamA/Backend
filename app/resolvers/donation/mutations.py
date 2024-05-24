from app.models.book_information import BookInformation
from app.models.book import Book
from app.models.user import User

from ariadne import MutationType
import datetime

mutation = MutationType()

@mutation.field("saveBook")
def resolve_save_book(_, info, user_id, isbn_number, title, author, published_date=None, description=None, image_path=None):
    db = info.context["db"]

    # Check if user exists
    user = db.query(User).filter_by(user_id=user_id).first()
    if not user:
        return {"error": "User not found"}

    # Check if book information already exists
    book_info = db.query(BookInformation).filter_by(isbn_number=isbn_number).first()
    if not book_info:
        # Create new book information
        book_info = BookInformation(
            isbn_number=isbn_number,
            title=title,
            author=author,
            published_date=published_date,
            description=description,
            image_path=image_path
        )
        db.add(book_info)
        db.commit()
        db.refresh(book_info)

    # Create new book entry
    new_book = Book(
        user_id=user_id,
        book_information_id=book_info.book_information_id,
        donation_date=datetime.date.today()
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return {"book": new_book}
