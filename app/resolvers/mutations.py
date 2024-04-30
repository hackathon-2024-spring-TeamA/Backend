from ariadne import MutationType
from datetime import datetime
from app.models.user import User

mutation = MutationType()

@mutation.field("createUser")
def resolve_create_user(_, info, request):
    db = info.context["db"]
    
    email = request["email"]
    password = request["password"]
    
    new_user = User(
        email=email,
        password=password,
        nickname="nickname",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        is_delete=False
    )
    
    db.add(new_user)
    db.commit()
    
    return "Seikou!"