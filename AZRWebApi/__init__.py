from flask_restful import Api

from AZRWebApi.anonymous_api import anonymous_query_create, anonymous_message_query_create
from .models import *
from AZRWebApi.admin_user_api import users, user
from AZRWebApi.user_api import user_api_resource, user_login_register, user_mail_check, user_sign_change, \
    user_avater_change

azr_web_user_client_api = Api(prefix='/api/user')
azr_web_admin_client_api = Api(prefix='/api/admin')

# user_client
azr_web_user_client_api.add_resource(user_api_resource, '/')
azr_web_user_client_api.add_resource(user_login_register, '/login_register/')
azr_web_user_client_api.add_resource(user_mail_check, '/mail_check/')
azr_web_user_client_api.add_resource(user_sign_change, '/sign_change/')
azr_web_user_client_api.add_resource(user_avater_change, '/avater_change/')
azr_web_user_client_api.add_resource(anonymous_query_create, '/amsg/')
azr_web_user_client_api.add_resource(anonymous_message_query_create, '/amsg/<int:a_id>/')





# admin_client
azr_web_admin_client_api.add_resource(users, '/user/')
azr_web_admin_client_api.add_resource(user, '/user/<int:user_id>/')
