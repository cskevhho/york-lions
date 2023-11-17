import secrets, os
from flask import current_app
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

# takes in image, saves it, creates a hex name for it, returns the name of the file
def save_picture(form_profile_pic):
    rand_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_profile_pic.filename) # _ is an unused var name since we're only using the extension?
    pic_filename = rand_hex + file_ext
    pic_path = os.path.join(current_app.root_path, "static/account", pic_filename)
    form_profile_pic.save(pic_path)
    
    return pic_filename