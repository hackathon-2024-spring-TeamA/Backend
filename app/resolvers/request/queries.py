from ariadne import QueryType
from sqlalchemy.orm import joinedload
from app.models import BookRequest, Book, User

query = QueryType()

@query.field("paginatedBookRequests")
def resolve_paginated_book_requests(_, info, page, perPage, userId, isMyRequest):
    db = info.context["db"]
    
    filter_condition = BookRequest.requester_id == userId if isMyRequest else BookRequest.holder_id == userId
    
    total_count = db.query(BookRequest).filter(filter_condition).count()
    book_requests = (
        db.query(BookRequest)
        .filter(filter_condition)
        .options(joinedload(BookRequest.book).joinedload(Book.book_information))
        .order_by(BookRequest.request_date.desc())
        .limit(perPage)
        .offset((page - 1) * perPage)
        .all()
    )
    
    return {
        "totalCount": total_count,
        "currentPage": page,
        "perPage": perPage,
        "bookRequests": book_requests,
    }

@query.field("getBookRequest")
def resolve_get_book_request(_, info, requestId):
    db = info.context["db"]
    book_request = (
        db.query(BookRequest)
        .filter(BookRequest.id == requestId)
        .options(joinedload(BookRequest.book).joinedload(Book.book_information))
        .first()
    )
    return book_request