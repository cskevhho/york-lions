from ...models.user import User
from ...extensions import db


def read_user(request):
    search_type = request.form['search_type']
    search_text = request.form['search_field']

    if search_type == "user_id":
        users = db.session.query(User).filter_by(id=search_text).all()
    elif search_type == "username":
        users = db.session.query(User).filter_by(username=search_text).all()
    elif search_type == "email":
        users = db.session.query(User).filter_by(email=search_text).all()
    else:
        users = db.session.query(User).all()

    if not users:
        return {"message": "No users found"}, 400

    user_data = [
        {
            "id": user.id,
            "email": user.email,
            "username": user.username,
        }
        for user in users
    ]  # note this is will return that json format response thing
    return {"users": user_data}, 200

def get_user(id):
    return db.session.query(User).filter_by(id=id).first()
