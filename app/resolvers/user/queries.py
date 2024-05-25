from ariadne import QueryType
from sqlalchemy.orm import joinedload
from app.models import User
from app.models.book_loan import BookLoan
from app.models.book import Book
from app.models.book_information import BookInformation

query = QueryType()

@query.field("authenticateUser")
def resolve_authenticate_user(_, info, request):
    email = request["email"]
    password = request["password"]

    # ここでは、emailとpasswordが一致する場合に認証成功（今回は仮のロジック）
    if email == "user@example.com" and password == "password":
        user = {"id": "1", "name": "John Doe", "email": email}
        return {"isSuccess": True, "errorMessage": None, "data": user}
    else:
        return {"isSuccess": False, "errorMessage": "Invalid email or password", "data": None}

@query.field("getUserNickname")
def resolve_get_user_nickname(_, info, userId):
    db = info.context["db"]
    user = db.query(User).filter(User.user_id == userId).first()
    if user:
        return user.nickname
    else:
        return None

@query.field("getUserBookLoans")
def resolve_get_user_book_loans(_, info, userId):
    db = info.context["db"]

    book_loans = (
        db.query(BookLoan)
        .options(joinedload(BookLoan.book).joinedload(Book.book_information))
        .filter(BookLoan.user_id == userId, BookLoan.is_held == True)
        .all()
    )

    return book_loans