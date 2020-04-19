from flask_restful import Api

from AZRWebApi.admin_user_api import admin_user_api_resource
from AZRWebApi.user_api import user_api_resource

azr_web_user_client_api = Api(prefix='/api/user')
azr_web_admin_client_api = Api(prefix='/api/admin')

azr_web_user_client_api.add_resource(user_api_resource, '/user/')
azr_web_admin_client_api.add_resource(admin_user_api_resource, '/user/')