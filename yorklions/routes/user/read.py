from ...models.user import User
from ...extensions import db


def read_user():
    users = db.session.query(User).all()
    if not users:
        return {"message": "No users found"}, 400
    return {"users": [user.to_dict() for user in users]}, 200