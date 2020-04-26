from flask import render_template

from AZRWeb import bp


@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/home/")
def home():
    return render_template("home.html")

@bp.route("/resume/")
def resume():
    return render_template("personal_info.html")

@bp.route("/register/")
def register():
    return render_template("register.html")

@bp.route("/login/")
def login():
    return render_template("login.html")

@bp.route("/user/")
def user():
    return render_template("user.html")