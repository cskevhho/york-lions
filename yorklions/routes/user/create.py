from ...models.user import User
from ...extensions import db


def create_user(username, email, password):
    existing_users = User.query.all()
    new_user = User(username=username, email=email, password=password)
    if not existing_users:  # TO CREATE ADMIN ACCOUNT ON FIRST RUN, COMMENT OUT AFTER
        new_user.is_admin = True
    db.session.add(new_user)
    db.session.commit()
    return {"message": f"User '{new_user.id}' created successfully"}, 200
