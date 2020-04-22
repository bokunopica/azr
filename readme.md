# AZR战队主页

## 工作日志
- 2020/4/22
  - 前端注册/登录页面
    - 注册/登录ajax请求 设置cookie
    - 仍未完成:
      - 导航条用户信息交互
      - 注册/登录 输入密码时的***

- 2020/4/19

  - api(客户端/管理端)
    - userapi
    - anoymousapi
    - test
  
- 2020/4/14

  - 前端页面
    - 导航条鼠标移入移出字体变色
    - 简历页面截图保存简历按钮
    - a标签样式

- 2020/4/13
  
  - 部分前端页面搭建
    - index.html
    - innerContent.html
    - 简历.html
    - 动画    未完成
  
- 2020/4/11
  
  - 需求文档
  - 实例构建 10%
  - 主页面 10%
  
- 2020/4/10
  
  - 项目架构搭建
  - 需求文档细节50%
  
  







## 功能需求

- 战队介绍
- 战队成员
  - 开车日
  - 内容定制
- 匿名黑人板块
- 道具教学
- 开车报名/机器人提醒

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

