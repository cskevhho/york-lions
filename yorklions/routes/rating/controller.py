from flask import Blueprint, render_template, request, redirect, url_for, flash
from .services import *
from ...models.rating import Rating
from ...extensions import db
from ...wtform.rating_forms import CreateRatingForm

rating_ctrl = Blueprint("rating_ctrl", __name__)


@rating_ctrl.route("/rating/create/<v_make>/<v_model>/<v_year>", methods=["GET", "POST"])
def create(v_make, v_model, v_year):
    form = CreateRatingForm()

    if form.validate_on_submit():
        new_rating = Rating(
            make=v_make,
            model=v_model,
            year=v_year,
            f_name=form.f_name.data,
            l_initial=form.l_initial.data,
            rating=form.rating.data,
            review_body=form.review_body.data
        )
        db.session.add(new_rating)
        db.session.commit()
        flash("Review successfully added", "success")
        return redirect(url_for('main.main_index'))

    return render_template("create_review.html", form=form, make=v_make, model=v_model, year=v_year)

@rating_ctrl.route("/api/rating/read", methods=["GET", "POST"])
def read():
    if request.method == "POST":
        return read_user(request)

    return render_template("user/read.html")


@rating_ctrl.route("/api/rating/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        user_id = request.form.get("id")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Do not pass in objects to the route, pass the parameters in, ORM formalities stuff
        return update_user(
            user_id, {"username": username, "email": email, "password": password}
        )

    return render_template("user/update.html")


@rating_ctrl.route("/api/rating/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        return delete_all()

    return render_template("rating/delete.html")

