from flask_restful import Resource


class admin_user_api_resource(Resource):
    def get(self):
        return {"msg":"ok"}