# www.azr-pro.top

## 功能需求

- 战队介绍
- 战队成员
  - 开车日
  - 内容定制
- 匿名黑人板块
- 道具教学
- 开车报名/机器人提醒
- 房租模块
  - 账单添加/修改/删除/查询

## 前端

- 战队介绍页面
- 用户页面/成员介绍页面
- 黑人板块页面
- 道具教学页面

## 后端

### 模型/实例

- 用户 user
  - id
  - u_name
    - string
  - u_password 
    - string
  - u_email
    - string
  - u_email_check
    - boolean
  - is_clan_member 战队成员
    - boolean
  - is_admin 管理员
    - boolean
  - u_avatar 头像
    - string
  - u_sign 签名
    - string
- 用户内容 user_info
  - id
  - u_id
    - integer
  - ui_title
    - string
  - ui_text
    - text
- 道具 nade
  - id
  - n_title
    - string
  - n_map
    - Integer
    - 0~10 每个数字对应一个map
  - n_type
    - 0 烟雾 default
    - 1 闪光
    - 2 燃烧弹
  - n_image
    - string
- 匿名信息 anoymous
  - id
  - a_check_id
  - a_title
  - a_content
  - a_timestamp
- 房租账单
  - 日期 date
  - 年 year
  - 月 month
  - 日 day
  - 房号 house_num
  - 电表读数(上月) meter_reading_last_month
  - 电表读数(本月) meter_reading_this_month
  - 用电量 electricity_consumption
  - 电费 electricity_expense
  - 水表读数(上月) water_meter_reading_last_month
  - 水表读数(本月) water_meter_reading_this_month
  - 用水量 water_consumption
  - 水费 water_expense
  - 其他 other_fee
  - 房租 rent_fee
  - 合计 total_fee
  - 备注 remark

### 客户端

- 战队介绍
  - 页面
- 战队成员
  - 页面
  - 用户 user
  - 用户接口 user_api
    - 注册(邮箱激活)
    - 登录
    - 修改头像
    - 修改签名
  - 用户内容 user_info
  - 用户内容接口 user_info_api
- 匿名黑人 
  - 匿名信息 anoymous
  - 匿名信息接口 anoymous_api
    - 发布信息
- 道具教学 
  - 道具 nade
  - 道具接口 nade_api

### 管理端

- user_api
  - 删除用户
  - 成为战队成员
- user_info_api
- anoymous_api
  - 删除帖子
  - 删除回复
- nade_api

