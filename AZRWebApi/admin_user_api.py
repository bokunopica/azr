from flask_restful import Resource, fields, marshal, reqparse

from AZRWebApi.models import User
from AZRWebApi.utils import admin_check

user_fields = {
    "id":fields.Integer,
    "u_name": fields.String,
    "u_email": fields.String,
    "u_email_check": fields.Boolean,
    "is_clan_member": fields.Boolean,
    "is_admin": fields.Boolean,
    "u_avater": fields.String,
    "u_sign": fields.String,
    "u_create_time":fields.Integer,
}
users_fields = {
    "msg": fields.String,
    "users": fields.List(fields.Nested(user_fields)),
}


class users(Resource):
    @admin_check
    def get(self):
        users = User.query.all()
        data = {"msg":"ok","users":users}
        return marshal(data,users_fields)


clan_parser = reqparse.RequestParser()
clan_parser.add_argument("action",type=int,required=True,help="choose a type : get:True or kick:False")

class user(Resource):
    @admin_check
    def get(self,user_id):
        user = User.query.get(user_id)
        if user:
            data = {"msg": "ok", "users": user}
        else:
            data = {"msg":"user not found"}
        return marshal(data,users_fields)

    @admin_check
    def put(self,user_id):
        user = User.query.get(user_id)
        if not user:
            return {"msg":"user not found"}
        action = clan_parser.parse_args().get("action")
        action = bool(action)
        user.is_clan_member = action
        user.save()
        data = {"msg":"changed ok","users":user}
        return marshal(data,users_fields)

    @admin_check
    def delete(self,user_id):
        user = User.query.get(user_id)
        user.delete()
        data = {"msg": "delete success", "users": user}
        return marshal(data,users_fields)