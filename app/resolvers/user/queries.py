from ariadne import QueryType

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