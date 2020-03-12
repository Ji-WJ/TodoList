"""
File: model.py
Author: J
Date: 2020-03-07
Connect: 
Description:

    设计数据库模型:
        1). 用户信息： User
        2). 用户角色信息: Role
        3). 用户角色: 用户 = 1:n, 一对多关系，外键写在多的一端。

login_manager回调函数的作用:
    注册回调函数， 当没有session_id时， 通过装饰器指定的函数来读取用户到session中，
    达到前端可通过 current_user 获取当前用户的目的
"""
from datetime import datetime

from flask import current_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from . import login_manager


# Flask中一个Model子类就是数据库中的一个表。默认表名'User'.lower() ===> user
class User(UserMixin, db.Model):
    """
    Flask-Login 提供了一个 UserMixin 类,包含常用方法的默认实现,且能满足大多数需求。
    因为User继承了UserMixin，所以具有UserMixin的属性和方法

    1). is_authenticated    用户是否已经登录?
    2). is_active           是否允许用户登录?False代表用户禁用
    3). is_anonymous        是否匿名用户?
    4). get_id()            返回用户的唯一标识符
    """
    __tablename__ = 'users'  # 自定义数据表的表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=True)  # 数据库中需要存储加密过的密码
    # 电子邮件地址 email,相对于用户名而言,用户更不容易忘记自己的电子邮件地址。
    email = db.Column(db.String(64), unique=True, index=True)
    # 该字段主要用于标记用户是否通过邮箱验证
    confirmed = db.Column(db.Boolean, default=False)
    # 外键关联(一对多关系，外键写在多的一端)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # 新添加的用户资料
    name = db.Column(db.String(64))
    # 用户的真实姓名
    location = db.Column(db.String(64))  # 所在地
    about_me = db.Column(db.Text())  # 自我介绍
    # 注册日期
    # default 参数可以接受函数作为默认值,
    # 所以每次生成默认值时,db.Column() 都会调用指定的函数。
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    # 最后访问日期
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)

    def ping(self):
        """刷新用户的最后访问时间"""
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    # 规定密码“属性”：密码加密，不可查看，可以修改
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        # generate_password_hash(password, method= pbkdf2:sha1 , salt_length=8):密码加密的散列值。
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        # check_password_hash(hash, password) :密码散列值和用户输入的密码是
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        """生成一个包含用户id的安全令牌(对象),密钥：从配置文件中导入；有效期（expiration）默认为一小时。"""
        s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        """
        检验令牌和检查令牌中id和已登录用户id是否匹配?如果检验通过,则把新添加的 confirmed 属
        性设为 True
        """
        s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except Exception as e:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        db.session.commit()
        return True

    def __repr__(self):
        return "<User: %s>" % (self.username)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    # 做了两件事情: 1). Role添加属性users    2). User添加属性role
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return "<Role: %s>" % (self.name)


# 加载用户的回调函数;如果能找到用户,返回用户对象;否则返回 None 。
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


