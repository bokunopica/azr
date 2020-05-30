from flask import Config

from AZRWeb import bp
from AZRWebApi import azr_web_user_client_api, azr_web_admin_client_api, azr_web_rent_house_api


def init_app(app):
    app.config.from_object(DevConfig)
    app.register_blueprint(bp)
    azr_web_user_client_api.init_app(app)
    azr_web_admin_client_api.init_app(app)
    azr_web_rent_house_api.init_app(app)




class DevConfig(Config):
    DEBUG = True

    TESTING = False

    THREAD = True

    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://XXXXXX:XXXXXX@XXXXX:XXXXX/XXXXX"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_TYPE = 'redis'

    SECRET_KEY = 'pyca'

    CACHE_TYPE = 'redis'


class OperationConfig(Config):
    DEBUG = False

    TESTING = False

    THREAD = True

    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://XXXXXX:XXXXXX@XXXXX:XXXXX/XXXXX"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_TYPE = 'redis'

    SECRET_KEY = 'pyca'

    CACHE_TYPE = 'redis'
