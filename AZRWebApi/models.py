from config.extensions import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(BaseModel):
    __tablename__ = 'user'
    u_name = db.Column(db.String(30), nullable=False, unique=True, comment='用户名')
    u_password = db.Column(db.String(256), nullable=False, comment='密码')
    u_email = db.Column(db.String(100), nullable=False, comment='邮箱',unique=True)
    u_email_check = db.Column(db.Boolean, default=False, comment='邮箱验证')
    is_clan_member = db.Column(db.Boolean, default=False, comment='是否是战队成员 1是 0否')
    is_admin = db.Column(db.Boolean, default=False, comment='是否是管理员 1是 0否')
    u_avater = db.Column(db.String(150), default='/static/defaultImg/default_avater.png', comment='头像')
    u_sign = db.Column(db.String(100), nullable=True, default="", comment='签名')
    is_delete = db.Column(db.Boolean, default=False, comment='是否被删除 1是 0否')
    u_create_time = db.Column(db.Integer, nullable=False,comment='创建时间')


class Anonymous(BaseModel):
    __tablename__ = 'anonymous'
    a_title = db.Column(db.String(50), nullable=False, comment='匿名信息标题')
    a_content = db.Column(db.String(150), nullable=False, comment='匿名信息内容')
    a_timestamp = db.Column(db.BigInteger, nullable=False, comment='发帖时间戳')
    a_max_floor = db.Column(db.Integer,nullable=False,default=1,comment='目前楼层')


class AnonymousMessage(BaseModel):
    __tablename__ = 'anonymous_message'
    a_id = db.Column(db.Integer, nullable=False, comment='匿名信息所属帖子id')
    am_floor = db.Column(db.Integer,nullable=True, comment='匿名信息在该帖的楼层')
    am_content = db.Column(db.String(50), nullable=False, comment='匿名信息内容')
    am_refer_to = db.Column(db.Integer, nullable=True, comment='匿名信息回复指向楼层')
    am_timestamp = db.Column(db.Integer, nullable=False, comment='匿名信息回复时间戳')


class Rent(BaseModel):
    __tablename__ = 'rent'
    date = db.Column(db.String(10), nullable=False, comment='付款日')
    year = db.Column(db.Integer, nullable=False, comment='付款日-年')
    month = db.Column(db.Integer, nullable=False, comment='付款日-月')
    day = db.Column(db.Integer, nullable=False, comment='付款日-日')
    house_num = db.Column(db.Integer, nullable=False, comment='房号')
    meter_reading_last_month = db.Column(db.Float, nullable=False, comment='电表读数(上月)')
    meter_reading_this_month = db.Column(db.Float, nullable=False, comment='电表读数(本月)')
    electricity_consumption = db.Column(db.Float, nullable=False, comment='用电量')
    electricity_expense = db.Column(db.Float, nullable=False, comment='电费')
    water_meter_reading_last_month = db.Column(db.Float, nullable=False, comment='水表读数(上月)')
    water_meter_reading_this_month = db.Column(db.Float, nullable=False, comment='水表读数(本月)')
    water_consumption = db.Column(db.Float, nullable=False, comment='用水量')
    water_expense = db.Column(db.Float, nullable=False, comment='水费')
    other_fee = db.Column(db.Float, nullable=True, default=0, comment='其他费用')
    rent_fee = db.Column(db.Float, nullable=False, comment='房租')
    total_fee = db.Column(db.Float, nullable=False, comment='合计')
    remark = db.Column(db.String(50), nullable=True, comment='备注')



