from flask_caching import Cache
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

migrate = Migrate()
db = SQLAlchemy()
cache =Cache()

def init_ext(app):
    db.init_app(app)
    migrate.init_app(app=app,db=db)
    cache.init_app(app)
