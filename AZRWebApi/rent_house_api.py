import time

from flask_restful import Resource, reqparse, fields, marshal_with

from AZRWebApi.models import Rent
from AZRWebApi.utils import admin_check

rent_parser = reqparse.RequestParser()
rent_parser.add_argument("year", int, required=True, help="check year")
rent_parser.add_argument("month", int, required=True, help="check month")
rent_parser.add_argument("day", int, required=True, help="check day")
rent_parser.add_argument("house_num", int, required=True, help="check house_num")
rent_parser.add_argument("meter_reading_last_month", float, required=True, help="check meter_reading_last_month")
rent_parser.add_argument("meter_reading_this_month", float, required=True, help="check meter_reading_this_month")
rent_parser.add_argument("water_meter_reading_last_month", float, required=True, help="check "
                                                                                      "water_meter_reading_last_month")
rent_parser.add_argument("water_meter_reading_this_month", float, required=True, help="check "
                                                                                      "water_meter_reading_this_month")
rent_parser.add_argument("other_fee", float, required=False, help="check other_fee")
rent_parser.add_argument("rent_fee", float, required=True, help="check rent_fee")
rent_parser.add_argument("remark", str, required=False, help="check remark")

rent_record_fields = {
    "id": fields.Integer,
    "date": fields.String,
    "year": fields.Integer,
    "month": fields.Integer,
    "day": fields.String,
    "house_num": fields.Integer,
    "meter_reading_last_month": fields.Float,
    "meter_reading_this_month": fields.Float,
    "electricity_consumption": fields.Float,
    "electricity_expense": fields.Float,
    "water_meter_reading_last_month": fields.Float,
    "water_meter_reading_this_month": fields.Float,
    "water_consumption": fields.Float,
    "water_expense": fields.Float,
    "other_fee": fields.Float,
    "rent_fee": fields.Float,
    "total_fee": fields.Float,
    "remark": fields.String,
}

rent_create_fields = {
    "msg": fields.String,
    "status": fields.Integer,
    "record": fields.Nested(rent_record_fields),
}

rent_query_fields = {
    "msg": fields.String,
    "status": fields.Integer,
    "record": fields.List(fields.Nested(rent_record_fields)),
}


class RentRecord(Resource):
    @marshal_with(rent_query_fields)
    def get(self):
        all_rent_records = Rent.query.all()
        data = {
            "msg": "ok",
            "status": "200",
            "record": all_rent_records,
        }
        return data


# 电费1元1度,水费7元1吨
electricity_price = 1
water_price = 7


class RentHouse(Resource):
    # @admin_check
    @marshal_with(rent_create_fields)
    def post(self):
        args = rent_parser.parse_args()
        rent_record = Rent()
        rent_record.year = int(args["year"])
        rent_record.month = int(args["month"])
        rent_record.day = int(args["day"])
        date_struct_time = time.struct_time((rent_record.year, rent_record.month, rent_record.day, 0, 0, 0, 0, 0, 0))
        rent_record.date = time.strftime("%Y-%m-%d", date_struct_time)
        rent_record.house_num = args["house_num"]
        rent_record.meter_reading_last_month = float(args["meter_reading_last_month"])
        rent_record.meter_reading_this_month = float(args["meter_reading_this_month"])
        rent_record.electricity_consumption = rent_record.meter_reading_this_month - rent_record.meter_reading_last_month
        rent_record.electricity_expense = electricity_price * rent_record.electricity_consumption
        rent_record.water_meter_reading_last_month = float(args["water_meter_reading_last_month"])
        rent_record.water_meter_reading_this_month = float(args["water_meter_reading_this_month"])
        rent_record.water_consumption = rent_record.water_meter_reading_this_month - rent_record.water_meter_reading_last_month
        rent_record.water_expense = water_price * rent_record.water_consumption
        rent_record.other_fee = float(args["other_fee"])
        rent_record.rent_fee = float(args["rent_fee"])
        rent_record.total_fee = rent_record.electricity_expense + rent_record.water_expense + rent_record.other_fee + rent_record.rent_fee
        rent_record.remark = args["remark"]
        rent_record.save()
        data = {
            "msg": "ok",
            "status": 200,
            "record": rent_record,
        }
        return data


change_parser = reqparse.RequestParser()
change_parser.add_argument("id", int, required=True, help="check id")
change_parser.add_argument("year", int, required=False, help="check year")
change_parser.add_argument("month", int, required=False, help="check month")
change_parser.add_argument("day", int, required=False, help="check day")
change_parser.add_argument("house_num", int, required=False, help="check house_num")
change_parser.add_argument("meter_reading_last_month", float, required=False, help="check meter_reading_last_month")
change_parser.add_argument("meter_reading_this_month", float, required=False, help="check meter_reading_this_month")
change_parser.add_argument("water_meter_reading_last_month", float, required=False, help="check "
                                                                                         "water_meter_reading_last_month")
change_parser.add_argument("water_meter_reading_this_month", float, required=False, help="check "
                                                                                         "water_meter_reading_this_month")
change_parser.add_argument("other_fee", float, required=False, help="check other_fee")
change_parser.add_argument("rent_fee", float, required=False, help="check rent_fee")
change_parser.add_argument("remark", str, required=False, help="check remark")


class RentChange(Resource):
    @marshal_with(rent_create_fields)
    def patch(self):
        args = change_parser.parse_args()
        id = args["id"]
        rent_record = Rent.query.get(id)
        if not rent_record:
            data = {
                "msg": "not found",
                "status": 404,
            }
            return data
        if args["year"]:
            rent_record.year = int(args["year"])
            print(rent_record.year)
        if args["month"]:
            rent_record.month = int(args["month"])
        if args["day"]:
            rent_record.day = int(args["day"])
        date_struct_time = time.struct_time((rent_record.year, rent_record.month, rent_record.day, 0, 0, 0, 0, 0, 0))
        rent_record.date = time.strftime("%Y-%m-%d", date_struct_time)
        if args["house_num"]:
            rent_record.house_num = args["house_num"]
        if args["meter_reading_last_month"]:
            rent_record.meter_reading_last_month = float(args["meter_reading_last_month"])
        if args["meter_reading_this_month"]:
            rent_record.meter_reading_this_month = float(args["meter_reading_this_month"])
        rent_record.electricity_consumption = rent_record.meter_reading_this_month - rent_record.meter_reading_last_month
        rent_record.electricity_expense = electricity_price * rent_record.electricity_consumption
        if args["water_meter_reading_last_month"]:
            rent_record.water_meter_reading_last_month = float(args["water_meter_reading_last_month"])
        if args["water_meter_reading_this_month"]:
            rent_record.water_meter_reading_this_month = float(args["water_meter_reading_this_month"])
        rent_record.water_consumption = rent_record.water_meter_reading_this_month - rent_record.water_meter_reading_last_month
        rent_record.water_expense = water_price * rent_record.water_consumption
        if args["other_fee"]:
            rent_record.other_fee = float(args["other_fee"])
        if args["rent_fee"]:
            rent_record.rent_fee = float(args["rent_fee"])
        rent_record.total_fee = rent_record.electricity_expense + rent_record.water_expense + rent_record.other_fee + rent_record.rent_fee
        if args["remark"]:
            rent_record.remark = args["remark"]
        rent_record.save()
        data = {
            "msg": "changed",
            "status": 200,
            "record": rent_record,
        }
        return data

    # @admin_check
    @marshal_with(rent_create_fields)
    def delete(self):
        id = change_parser.parse_args().get("id")
        record = Rent.query.get(id)
        if not record:
            data = {
                "msg": "not found",
                "status": 404,
            }
            return data
        record.delete()
        data = {
            "msg": "deleted",
            "status": 204,
            "record": record,
        }
        return data
