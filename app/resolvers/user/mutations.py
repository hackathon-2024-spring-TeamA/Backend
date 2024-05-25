from ariadne import MutationType
from datetime import datetime
from app.models.user import User
import uuid

mutation = MutationType()

@mutation.field("createUser")
def resolve_create_user(_, info, request):
    db = info.context["db"]
    
    email = request["email"]
    password = request["password"]
    
    new_user = User(
        user_id=uuid.uuid4(),
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

@mutation.field("updateUserNickname")
def resolve_update_user_nickname(_, info, userId, nickname):
    db = info.context["db"]

    user = db.query(User).filter(User.user_id == userId).first()

    if user:
        user.nickname = nickname
        user.updated_at = datetime.now()
        db.commit()
        return "Success"
    else:
        return "User not found"