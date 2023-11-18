import os
from flask import Blueprint, current_app, render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from ..forms import RegistrationForm, LoginForm, UpdateAccountForm
from ..extensions import db, bcrypt
from ..models.user import User
from .user.create import create_user
from .user.services import save_picture

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(
            url_for("main.main_index")
        )  # Redirect to home page if user is already logged in
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        create_user(form.username.data, form.email.data, hashed_password)
        flash(f"Account created, please login!", "success")
        return redirect(url_for("auth.login"))
    return render_template(
        "register.html", title="Register", form=form, errors=form.errors
    )


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get(
                "next"
            )  # Remember, args is a dict, get returns none if key not found
            return (
                redirect(next_page)
                if next_page
                else redirect(url_for("main.main_index"))
            )
            return redirect(url_for("main.main_index"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form, errors=form.errors)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.main_index"))


@auth.route("/account", methods=["POST", "GET"])
@login_required  # decorators, yum
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.profile_pic.data:
            pic_file = save_picture(form.profile_pic.data)
            remove_old_picture(current_user.image_file)
            current_user.image_file = pic_file
        
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        
        flash("Account updated!", "success")
        return redirect(url_for("auth.account"))
    elif request.method == "GET":  # populate form with current user info on
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for("static", filename="account/" + current_user.image_file)
    return render_template(
        "account.html", title="Account", image_file=image_file, form=form
    )

def remove_old_picture(file_name):
    account_static_folder = os.path.join(current_app.root_path, 'static', 'account')
    old_image_path = os.path.join(account_static_folder, file_name)
    if os.path.exists(old_image_path):
        os.remove(old_image_path)