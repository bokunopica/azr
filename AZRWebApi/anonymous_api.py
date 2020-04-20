import time

from flask_restful import Resource, reqparse, fields, marshal_with

from AZRWebApi.models import Anonymous, AnonymousMessage
from AZRWebApi.utils import login_check

anonymous_parser = reqparse.RequestParser()
anonymous_parser.add_argument("a_title", str, required=True, help="请输入您要发布的标题")
anonymous_parser.add_argument("a_content", str, required=True, help="请输入您要发布的内容")

anonymous_fields = {
    "id": fields.Integer,
    "a_title": fields.String,
    "a_content": fields.String,
    "a_timestamp": fields.Integer,
    "a_max_floor": fields.Integer,
}

ans_fields = {
    "msg": fields.String,
    "anonymous": fields.List(fields.Nested(anonymous_fields)),
}

am_fields = {
    "id": fields.Integer,
    "a_id": fields.Integer,
    "am_floor": fields.Integer,
    "am_content": fields.String,
    "am_refer_to": fields.Integer,
    "am_timestamp": fields.Integer,
}
an_am_fields = {
    "msg": fields.String,
    "anonymous": fields.Nested(anonymous_fields),
    "replies": fields.List(fields.Nested(am_fields)),
}


class anonymous_query_create(Resource):
    # 获取所有匿名帖子
    @marshal_with(ans_fields)
    @login_check
    def get(self):
        ans = Anonymous.query.all()
        data = {"msg": "ok", "anonymous": ans}
        return data

    # 创建匿名贴
    @marshal_with(ans_fields)
    @login_check
    def post(self):
        args = anonymous_parser.parse_args()
        timestamp = int(time.time())
        an = Anonymous(a_title=args.a_title, a_content=args.a_content, a_timestamp=timestamp)
        try:
            an.save()
        except Exception as e:
            return {"msg": str(e)}
        data = {"msg": "created success", "anonymous": an}
        return data


am_parser = reqparse.RequestParser()
am_parser.add_argument("am_content", int, required=True, help="请输入您要回复的内容")
am_parser.add_argument("am_refer_to", int, required=False, help="回复楼层")


class anonymous_message_query_create(Resource):
    @marshal_with(an_am_fields)
    @login_check
    def get(self, a_id):
        an = Anonymous.query.get(a_id)
        ams = AnonymousMessage.query.filter_by(a_id=a_id)
        data = {"msg": "query ok", "anonymous": an, "replies": ams, }
        return data

    @marshal_with(an_am_fields)
    @login_check
    def post(self, a_id):
        args = am_parser.parse_args()
        an = Anonymous.query.get(a_id)
        old_ams = AnonymousMessage.query.filter_by(a_id=a_id).all()
        am_floor = an.a_max_floor
        new_ams = AnonymousMessage(a_id=a_id, am_floor=am_floor + 1, am_content=args.get("am_content"),
                                   am_refer_to=args.get("am_refer_to"), am_timestamp=int(time.time()))
        an.a_max_floor += 1
        new_ams.save()
        an.save()
        old_ams.append(new_ams)
        data = {"msg": "replied success", "anonymous": an, "replies": old_ams}
        return data
