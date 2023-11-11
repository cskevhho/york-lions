from flask import Blueprint, render_template

index = Blueprint('index', __name__)

@index.route('/')
def main_index():
    return render_template("index.html")

@index.route('/user/')
def home():
    return render_template("user/user.html")

# @index.route('/')
# def create():
#     return render_template("index.html")

# @index.route('/')
# def read():
#     return render_template("index.html")

# @index.route('/')
# def update():
#     return render_template("index.html")

# @index.route('/')
# def delete():
#     return render_template("index.html")

