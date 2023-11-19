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

def delete_user(id):
    user = db.session.query(User).filter_by(id=id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return {"message": f"Successfully deleted user '{id}'"}, 200
    else:
        return {"message": f"User '{id}' not found"}, 404

def delete_guest_users():
    users = db.session.query(User).filter_by(is_guest=True).all()

    if not users:
        return {"message": "No users to delete"}, 400
    for user in users:
        db.session.delete(user)

    db.session.commit()
    return {"message": "All guest users deleted successfully"}, 200
