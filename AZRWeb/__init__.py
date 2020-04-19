from flask import Blueprint

bp = Blueprint("azr_web",__name__)

from .views import *