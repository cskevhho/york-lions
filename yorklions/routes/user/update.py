from ...models.user import User
from ...extensions import db


def update_user(id, updated_data):
    user = User.query.get(id)
    if not user:
        return {"message": f"User with ID {id} not found"}, 404

    user.username = updated_data.get("username", user.username)
    user.email = updated_data.get("email", user.email)
    user.password = updated_data.get("password", user.password)

    db.session.commit()
    return {"message": f"User '{user.id}' updated successfully"}, 200
