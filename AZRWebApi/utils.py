import hashlib
import smtplib
from email.mime.text import MIMEText

from flask import request, g
from flask_restful import reqparse

from AZRWebApi.models import User
from config.extensions import cache


def valueOfSha256(source, *args):
    hash_model = hashlib.sha256()
    for arg in args:
        source += str(arg)
    hash_model.update(source.encode("utf-8"))
    return hash_model.hexdigest()


def sendEmail(receivers, title, content):
    mail_host = "smtp.163.com"  # SMTP服务器
    mail_user = "qqboolean@163.com"  # 用户名
    mail_pass = "HYSJEASWJTFBKLAB"  # 授权密码，非登录密码
    sender = 'qqboolean@163.com'  # 发件人邮箱(最好写全, 不然会失败)
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        return True
    except smtplib.SMTPException as e:
        print(e)
        return False

token_parser = reqparse.RequestParser()
token_parser.add_argument("access_token", type=str, required=True, help="please login")


def login_check(func):
    def wrapper(*args,**kwargs):
        token = token_parser.parse_args().get("access_token")
        user_id = cache.get(token)
        user = User.query.get(user_id)
        g.user = user
        g.access_token = token
        if not user:
            return {"msg": "登录验证失败"}
        return func(*args, **kwargs)
    return wrapper

def admin_check(func):
    def wrapper(*args,**kwargs):
        token = token_parser.parse_args().get("access_token")
        user_id = cache.get(token)
        user = User.query.get(user_id)
        g.user = user
        g.access_token = token
        if not user.is_admin:
            return {"msg": "非管理员,无法操作"}
        return func(*args, **kwargs)
    return wrapper

image_format = ['png','jpg','jpeg']