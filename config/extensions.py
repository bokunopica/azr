import os

from flask_caching import Cache
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

migrate = Migrate()
db = SQLAlchemy()
cache =Cache()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_FOLDER = 'static/img'
AVATER_FOLDER = 'static/img/avater'

def init_ext(app):
    db.init_app(app)
    migrate.init_app(app=app,db=db)
    cache.init_app(app)
