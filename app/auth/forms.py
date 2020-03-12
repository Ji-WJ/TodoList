"""
File: forms.py
Author: J
Date: 2020-03-07
Connect: 
Description: 
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError

from app.model import User


class RegistrationForm(FlaskForm):
    email = StringField('电子邮箱',
                        validators=[
                            DataRequired(),
                            Length(1, 64),
                            Email()],
                        # 给前端的标签添加下面的属性信息;
                        render_kw={
                            'class': "layui-input",
                            "placeholder": "电子邮箱"
                        })
    username = StringField('用户名',
                           validators=[
                               DataRequired(),
                               Length(1, 64),
                               # ^: 以什么开头， $以什么结尾。 \w代表单个字母数字或者下划线. *代表前一个字符出现0次或者多次
                               Regexp('^\w*$', message='用户名只能由字母数字以及下划线组成')],
                           render_kw={
                               'class': "layui-input",
                               "placeholder": "用户名"
                           })
    password = PasswordField('密码',
                             validators=[
                                 DataRequired()],
                             render_kw={
                                 'class': "layui-input",
                                 "placeholder": "密码"
                             })
    repassword = PasswordField('确认密码',
                               validators=[DataRequired(),
                                    EqualTo('password', message='密码不一致')],
                               render_kw={
                                   'class': "layui-input",
                                   "placeholder": "确认密码"
                               })
    submit = SubmitField('注册')

    # 两个自定义的验证函数, 以 validate_ 开头且跟着字段名的方法, 这个方法和常规的验证函数一起调用。
    def validate_email(self, field):
        # field是 email表单对象， field.data是 email表单里提交的数据信息.
        # ==> select * from users where email='xxxx' limit 1;
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("邮箱地址%s已经注册!" % (field.data))

    def validate_username(self, field):
        # field是 username 表单对象， field.data 是 username 表单里提交的数据信息.
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("用户名%s已经注册!" % (field.data))


class LoginForm(FlaskForm):
    """用户登录表单"""
    email = StringField('电子邮箱',
                        validators=[
                            DataRequired(),
                            Length(1, 64),
                            Email()],
                        # 给前端的标签添加下面的属性信息;
                        render_kw={
                            'class': "layui-input",
                            "placeholder": "电子邮箱"
                        })
    password = PasswordField('密码',
                             validators=[DataRequired()],
                             # 给前端的标签添加下面的属性信息;
                             render_kw={
                                 'class': "layui-input",
                                 "placeholder": "密码"
                             })
    submit = SubmitField('登录')