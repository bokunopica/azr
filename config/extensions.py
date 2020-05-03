import logging
import os
import time

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
    log_dir = BASE_DIR+"/log/"+ "azr-start-"+time.strftime("%Y-%m-%d-%H-%M",time.localtime())+".log"
    handler = logging.FileHandler(log_dir, encoding='UTF-8')
    handler.setLevel(logging.WARNING)
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
