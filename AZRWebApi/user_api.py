from flask_restful import Resource


class user_api_resource(Resource):
    def get(self):
        return {"msg":"ok"}


class user_login_register(Resource):
    def get(self):
        return {"msg":"ok"}