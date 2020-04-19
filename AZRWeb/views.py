from flask import render_template

from AZRWeb import bp


@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/home")
def home():
    return render_template("innerContent.html")

@bp.route("/resume/")
def resume():
    return render_template("personal_info.html")