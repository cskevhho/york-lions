from ...models.user import User
from ...extensions import db


def create_user(username, email, password):
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return {"message": f"User '{new_user.name}' created successfully"}, 200
