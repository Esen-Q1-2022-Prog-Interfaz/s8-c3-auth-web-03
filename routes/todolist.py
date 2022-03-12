from flask import Blueprint, render_template
from flask_login import current_user
from models.user import User

todolist = Blueprint("todolist", __name__, url_prefix="/todolist")


@todolist.route("/")
def home():
    currentUser = current_user
    userList = None
    if "admin" in currentUser.rank:
        # es un admin
        userList = User.query.all()
    else:
        # es un user
        userList = list((User.query.filter_by(id=currentUser.id).first(),))
    return render_template("todolist/home.html", user=currentUser, userList=userList)
