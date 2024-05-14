from ariadne import QueryType
from sqlalchemy.orm import joinedload
from app.models import BookRequest, Book

query = QueryType()

@query.field("paginatedBookRequests")
def resolve_paginated_book_requests(_, info, page, perPage):
    db = info.context["db"]

    total_count = db.query(BookRequest).count()
    book_requests = (
        db.query(BookRequest)
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