from datetime import datetime, timedelta
from ariadne import MutationType
from app.models import BookRequest, Book, BookLoan
import uuid

mutation = MutationType()

@mutation.field("updateBookRequestStatus")
def resolve_update_book_request_status(_, info, requestId, status, userId=None, bookId=None):
    db = info.context["db"]
    book_request = db.query(BookRequest).get(requestId)
    if not book_request:
        return None

    book_request.status = status

    if status == "arrived" and userId and bookId:
        rent_date = datetime.now().date()
        due_date = rent_date + timedelta(weeks=2)
        book_loan = BookLoan(
            id=str(uuid.uuid4()),
            user_id=userId,
            book_id=bookId,
            rent_date=rent_date,
            due_date=due_date,
            is_held=True
        )
        db.add(book_loan)
    elif status == "arrived":
        raise ValueError("userId and bookId are required when status is 'arrived'")

    db.commit()
    return book_request