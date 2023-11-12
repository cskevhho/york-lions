from ...models.user import User
from ...extensions import db


def read_user():
    users = db.session.query(User).all()
    if not users:
        return {"message": "No users found"}, 400
    
    user_data = [{"id": user.id, "name": user.name} for user in users]  # note this is will return that json format response thing
    return {"users": user_data}, 200
