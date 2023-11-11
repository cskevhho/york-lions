from ...models.user import User
from ...extensions import db


def update_user(id):
    user = User.query.filter_by(id=id).first()

    if not user:
        return {"message": "User " + id + " not found"}, 400

    user.name = "Updated Name"

    db.session.commit()
    return {"message": "User " + id + " updated successfully"}, 200
