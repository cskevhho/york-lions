from ...models.user import User
from ...extensions import db


def create_user(username, email, password, is_guest=False):
    existing_users = User.query.all()
    new_user = User(username=username, email=email, password=password, is_guest=is_guest)
    if not existing_users:  # TO CREATE ADMIN ACCOUNT ON FIRST RUN, COMMENT OUT AFTER
        new_user.is_admin = True
    db.session.add(new_user)
    db.session.commit()
    return {"message": f"User '{new_user.id}' created successfully", "new_user_id": new_user.id}, 200
