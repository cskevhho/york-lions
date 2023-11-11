from ...models.user import User
from ...extensions import db


def create_user(name):
    if not name:
        return {"message": "Name is required"}, 409

    new_user = User(name=name)

    if User.query.filter_by(name=name).first():
        return {"message": "User "+name+" already exists"}, 409

    db.session.add(new_user)
    db.session.commit()
    return {"message": "User "+name+" created successfully"}, 200