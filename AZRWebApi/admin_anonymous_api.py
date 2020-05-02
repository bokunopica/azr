import time

from flask_restful import Resource, reqparse, fields, marshal_with

from AZRWebApi.models import Anonymous, AnonymousMessage
from AZRWebApi.utils import admin_check

anonymous_parser = reqparse.RequestParser()
anonymous_parser.add_argument("a_id", str, required=True, help="请输入您删除的帖子id")

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
    "am": fields.Nested(am_fields),
}


class anonymous_delete(Resource):
    @marshal_with(ans_fields)
    @admin_check
    def delete(self):
        a_id = anonymous_parser.parse_args().get("a_id")
        an = Anonymous.query.get(a_id)
        try:
            an.delete()
        except Exception as e:
            return {"msg": str(e)}
        data = {"msg": "delete success", "anonymous": an}
        return data


am_parser = reqparse.RequestParser()
am_parser.add_argument("am_id", int, required=True, help="请输入您删除的回复id")


class anonymous_message_delete(Resource):
    @marshal_with(an_am_fields)
    @admin_check
    def delete(self):
        am_id = am_parser.parse_args().get("am_id")
        am = AnonymousMessage.query.get(am_id)
        am.delete()
        data = {"msg": "replied success", "am":am}
        return data
