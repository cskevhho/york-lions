from flask import Blueprint, render_template

index = Blueprint('index', __name__)

@index.route('/')
def main_index():
    return render_template("index.html")

@index.route('/user/')
def home():
    return render_template("user/user.html")
