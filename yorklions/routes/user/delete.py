from ...models.user import User
from ...extensions import db


def delete_all():
    users = User.query.all()

    if not User.query.all():
        return {"message": "No users to delete"}, 400
    for user in users:
        db.session.delete(user)

    db.session.commit()
    return {"message": "All users deleted successfully"}, 200
