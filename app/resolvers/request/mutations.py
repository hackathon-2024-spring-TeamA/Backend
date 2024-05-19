from ariadne import MutationType
from app.models import BookRequest, Book

mutation = MutationType()

@mutation.field("updateBookRequestStatus")
def resolve_update_book_request_status(_, info, requestId, status):
    db = info.context["db"]
    book_request = db.query(BookRequest).get(requestId)
    
    if book_request:
        book_request.status = status
        db.commit()
        
    return book_request
