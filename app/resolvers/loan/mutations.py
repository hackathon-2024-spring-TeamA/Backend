from ariadne import MutationType
from app.models import Book, BookRequest
from datetime import datetime
import uuid

mutation = MutationType()

@mutation.field("createBookRequest")
def resolve_create_book_request(_, info, request):
    db = info.context["db"]

    book_id = request["bookId"]
    holder_id = request["holderId"]
    requester_id = request["requesterId"]

    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        return {
            "isSuccess": False,
            "errorMessage": "本が見つかりません。",
        }

    latest_book_request = (
        db.query(BookRequest)
        .filter(BookRequest.book_id == book_id)
        .order_by(BookRequest.request_date.desc())
        .first()
    )

    if latest_book_request and latest_book_request.status in [
        "requested",
        "sending",
    ]:
        return {
            "isSuccess": False,
            "errorMessage": "すでに他の人からのリクエストがあります。",
        }

    new_book_request = BookRequest(
        id=str(uuid.uuid4()),
        book_id=book_id,
        requester_id=requester_id,
        holder_id=holder_id,
        request_date=datetime.now(),
        status="requested",
    )

    db.add(new_book_request)
    db.commit()

    return {
        "isSuccess": True,
        "errorMessage": None,
    }