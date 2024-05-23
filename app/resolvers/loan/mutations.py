from ariadne import MutationType
from app.models import Book, BookRequest, BookLoan
from datetime import datetime, timedelta
import uuid

mutation = MutationType()

def is_already_borrowed(db, requester_id):
    latest_requester_request = (
        db.query(BookRequest)
        .filter(BookRequest.requester_id == requester_id)
        .order_by(BookRequest.request_date.desc())
        .first()
    )

    if latest_requester_request and latest_requester_request.status in [
        "requested",
        "sending",
    ]:
        return True
    elif latest_requester_request and latest_requester_request.status == "arrived":
        latest_requester_loan = (
            db.query(BookLoan)
            .filter(BookLoan.user_id == requester_id)
            .order_by(BookLoan.rent_date.desc())
            .first()
        )
        if latest_requester_loan:
            due_date_noon = datetime.combine(latest_requester_loan.due_date + timedelta(days=1), datetime.min.time()) + timedelta(hours=12)
            if due_date_noon > datetime.now():
                return True

    return False

@mutation.field("createBookRequest")
def resolve_create_book_request(_, info, request):
    db = info.context["db"]
    book_id = request["bookId"]
    holder_id = request["holderId"]
    requester_id = request["requesterId"]

    if is_already_borrowed(db, requester_id):
        return {
            "isSuccess": False,
            "errorMessage": "既に本を一冊借りています。",
        }

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