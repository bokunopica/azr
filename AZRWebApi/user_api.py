import hashlib
import time

from flask import request
from flask_restful import Resource, reqparse, fields, marshal

from AZRWebApi import User

user_login_reg_parser = reqparse.RequestParser()
user_login_reg_parser.add_argument("action", type=str, required=True,
                                   help="please input the correct action type,login or register")
user_login_reg_parser.add_argument("username", type=str, required=True, help="please input the correct username")
user_login_reg_parser.add_argument("password", type=str, required=True, help="please input the correct password")
user_login_reg_parser.add_argument("email", type=str, required=True, help="please input the correct email")

user_fields = {
    "u_name": fields.String,
    "u_email": fields.String,
    "u_email_check": fields.Boolean,
    "is_clan_member": fields.Boolean,
    "is_admin": fields.Boolean,
    "u_avatar": fields.String,
    "u_sign": fields.String,
    "u_create_time":fields.Integer,
}
user_login_register_fields = {
    "msg": fields.String,
    "user": fields.Nested(user_fields),
}


class user_api_resource(Resource):
    def get(self):
        return {"msg": "ok"}


class user_login_register(Resource):
    def post(self):
        args = user_login_reg_parser.parse_args()
        action = args.get('action')
        if action == 'register':
            u_name = args.get('username')
            source_pwd = args.get('password')
            email = args.get('email')
            hash_model = hashlib.sha256()
            hash_model.update(source_pwd.encode("utf-8"))
            password = hash_model.hexdigest()
            create_time = int(time.time())
            user = User(u_name=u_name, u_password=password, u_email=email,u_create_time = create_time)
            try:
                user.save()
            except Exception as e:
                return {"msg":"failed","excepction":e}
            data = {"msg":"register success","user":user}
            return marshal(data,user_login_register_fields)

        if action == 'login':
            u_name = args.get('username')
            source_pwd = args.get('password')
            hash_model = hashlib.sha256()
            hash_model.update(source_pwd.encode("utf-8"))
            password = hash_model.hexdigest()
            user = User.query.filter_by(u_name=u_name).first()
            if not user:
                return {"msg": "user not found"}
            if user.u_password == password:
                data = {"msg": "login success","user":user}
                return marshal(data,user_login_register_fields)
            else:
                return {"msg": "login failed"}
        else:
            return {"msg": "请指定操作类型"}


class user_mail_check(Resource):
    def get(self):
        pass