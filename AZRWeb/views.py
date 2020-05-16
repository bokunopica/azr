from flask import render_template

from AZRWeb import bp


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/home/")
def home():
    return render_template("home.html")


@bp.route("/user/")
def user():
    return render_template("user.html")


@bp.route("/resume/")
def resume():
    return render_template("personal_info.html")


@bp.route("/register/")
def register():
    return render_template("register.html")


@bp.route("/login/")
def login():
    return render_template("login.html")


@bp.route("/userinfo/")
def userinfo():
    return render_template("userinfo.html")


@bp.route("/anonymous/")
def anonymous():
    return render_template("anonymous.html")


@bp.route("/anonymous/<int:a_id>/")
def anonymous_aid(a_id):
    return render_template("anonymous_aid.html", data={"a_id": a_id})

@bp.route("/rent_login/")
def rent_login():
    return render_template("rent_login.html")
