from flask_restful import Api
from .models import *
from AZRWebApi.admin_user_api import admin_user_api_resource
from AZRWebApi.user_api import user_api_resource, user_login_register, user_mail_check

azr_web_user_client_api = Api(prefix='/api/user')
azr_web_admin_client_api = Api(prefix='/api/admin')

# user_client
azr_web_user_client_api.add_resource(user_api_resource, '/')
azr_web_user_client_api.add_resource(user_login_register, '/login_register/')
azr_web_user_client_api.add_resource(user_mail_check, '/mail_check/')







azr_web_admin_client_api.add_resource(admin_user_api_resource, '/user/')