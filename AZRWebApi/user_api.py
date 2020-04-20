import hashlib
import os
import time
import uuid
from concurrent.futures.thread import ThreadPoolExecutor

from flask import g, request
from flask_restful import Resource, reqparse, fields, marshal

from AZRWebApi import User
from AZRWebApi.utils import sendEmail, valueOfSha256, login_check, image_format
from config.extensions import cache, BASE_DIR, UPLOAD_FOLDER

mail_executor = ThreadPoolExecutor()

user_action_parser = reqparse.RequestParser()
user_action_parser.add_argument("action", type=str, required=True,
                                   help="please input the correct action type,login or register")
user_login_parser = reqparse.RequestParser()
user_login_parser.add_argument("username", type=str, required=True, help="please input the correct username")
user_login_parser.add_argument("password", type=str, required=True, help="please input the correct password")

user_register_parser = user_login_parser.copy()
user_register_parser.add_argument("email", type=str, required=True, help="please input the correct email")

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
user_login_register_fields = {
    "msg": fields.String,
    "user": fields.Nested(user_fields),
    "access_token":fields.String,
}


class user_api_resource(Resource):
    @login_check
    def get(self):
        data = {"msg": "ok","user":g.user,"access_token":g.access_token}
        print(g.user.u_avater)
        return marshal(data,user_login_register_fields)


class user_login_register(Resource):
    def post(self):
        action = user_action_parser.parse_args().get('action')
        if action == 'register':
            args = user_register_parser.parse_args()
            u_name = args.get('username')
            source_pwd = args.get('password')
            email = args.get('email')
            password = valueOfSha256(source_pwd)
            create_time = int(time.time())
            user = User(u_name=u_name, u_password=password, u_email=email,u_create_time = create_time)
            try:
                user.save()
            except Exception as e:
                return {"msg":"failed","excepction":str(e)}
            data = {"msg":"register success","user":user}
            return marshal(data,user_login_register_fields)

        if action == 'login':
            args = user_login_parser.parse_args()
            u_name = args.get('username')
            source_pwd = args.get('password')
            hash_model = hashlib.sha256()
            hash_model.update(source_pwd.encode("utf-8"))
            password = hash_model.hexdigest()
            user = User.query.filter_by(u_name=u_name).first()
            if not user:
                return {"msg": "user not found"}
            if user.u_password == password:
                token = uuid.uuid4().hex
                cache.set(token, user.id, timeout=60 * 60)
                data = {"msg": "login success","user":user,"access_token":token}
                return marshal(data,user_login_register_fields)
            else:
                return {"msg": "login failed"}
        else:
            return {"msg": "请指定操作类型"}


mail_check_parser = reqparse.RequestParser()
mail_check_parser.add_argument("verify_code", type=str, required=True, help="please type your mail verify code")

class user_mail_check(Resource):
    @login_check
    def post(self):
        user = g.user
        if user.u_email_check==True:
            data = {"msg":"该用户的邮箱已激活","user":user}
            return marshal(data,user_login_register_fields)
        username = user.u_name
        email = user.u_email
        verify_code = uuid.uuid4().hex[0:4]
        cache.set(username,verify_code,timeout=60)
        content = "您的验证码为:"+verify_code
        mail_executor.submit(sendEmail(receivers=[email],title='邮箱验证',content=content))
        data = {"msg":"验证邮件已发送","user":user,"access_token":g.access_token}
        return marshal(data,user_login_register_fields)

    @login_check
    def put(self):
        user = g.user
        if user.u_email_check == True:
            data = {"msg": "该用户的邮箱已激活", "user": user}
            return marshal(data, user_login_register_fields)
        args = mail_check_parser.parse_args()
        verify_code = args.get("verify_code")
        username = user.u_name
        real_verify_code = cache.get(username)
        if verify_code == real_verify_code:
            user = g.user
            user.u_email_check = True
            user.save()
            data = {"msg":"邮箱验证成功","user":user,"access_token":g.access_token}
            return marshal(data,user_login_register_fields)
        else:
            data = {"msg":"邮箱验证失败"}
            return data


sign_change_parser = reqparse.RequestParser()
sign_change_parser.add_argument("sign", type=str, required=True, help="please type your new sign")

class user_sign_change(Resource):
    @login_check
    def put(self):
        user = g.user
        new_sign = sign_change_parser.parse_args().get("sign")
        try:
            user.u_sign = new_sign
            user.save()
            data = {"msg":"changed ok","user":user,"access_token":g.access_token}
            return marshal(data,user_login_register_fields)
        except Exception as e:
            data = {"msg":e,"user":user,"access_token":g.access_token}
            return marshal(data,user_login_register_fields)



class user_avater_change(Resource):
    @login_check
    def put(self):
        try:
            file = request.files['avater']
        except Exception as e:
            return {"msg":e}
        filename, file_format = file.filename.split(".")
        if file_format not in image_format:
            return {"msg":"错误的图片格式"}
        time_stamp_string = str(int(time.time()))
        filedir = valueOfSha256(filename)+time_stamp_string+"."+file_format
        save_dir = os.path.join(BASE_DIR, UPLOAD_FOLDER, filedir)
        file.save(save_dir)
        user = g.user
        user.u_avater = '/'+UPLOAD_FOLDER+'/'+filedir
        user.save()
        data = {'msg':"avater changed","user":user,"access_token":g.access_token}
        return marshal(data,user_login_register_fields)
