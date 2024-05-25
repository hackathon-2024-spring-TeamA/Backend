from ariadne import QueryType
from sqlalchemy.orm import joinedload
from app.models import Book, BookInformation, BookLoan, BookRequest
from sqlalchemy import or_

query = QueryType()

@query.field("searchBooks")
def resolve_search_books(_, info, page, perPage, searchQuery=None):
    db = info.context["db"]

    query = db.query(Book).options(
        joinedload(Book.book_information),
        joinedload(Book.book_loans).load_only(BookLoan.id, BookLoan.rent_date, BookLoan.due_date, BookLoan.return_date, BookLoan.is_held),
        joinedload(Book.book_requests).load_only(BookRequest.id, BookRequest.book_id, BookRequest.requester_id, BookRequest.holder_id, BookRequest.request_date, BookRequest.status)
    )

    if searchQuery:
        query = query.join(BookInformation).filter(
            or_(
                BookInformation.title.ilike(f"%{searchQuery}%"),
                BookInformation.description.ilike(f"%{searchQuery}%")
            )
        )

    total_count = query.count()

    books = query.order_by(Book.created_at.desc()).limit(perPage).offset((page - 1) * perPage).all()

    for book in books:
        book.latest_book_loan = max(book.book_loans, key=lambda loan: loan.rent_date) if book.book_loans else None
        book.latest_book_request = max(book.book_requests, key=lambda request: request.request_date) if book.book_requests else None

    return {
        "totalCount": total_count,
        "currentPage": page,
        "perPage": perPage,
        "books": books,
    }