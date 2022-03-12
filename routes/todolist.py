from flask import Blueprint, render_template
from flask_login import current_user

todolist = Blueprint("todolist", __name__, url_prefix="/todolist")


@todolist.route("/")
def home():
    return render_template("todolist/home.html", user=current_user)
