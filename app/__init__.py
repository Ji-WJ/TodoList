"""
程序工厂函数目的, 延迟创建程序实例
    1. 测试，可以使用多个应用程序的实例，为每个实例分配不同的配置，从而从事每一种不同的情况
    2. 多个实例，要同时运行在同一个应用的不同版本，可以在你的web服务器中配置多个实例并分配不同配置
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
# 导入配置信息
from config import config

# 实例化项目所需的插件
bootstrap = Bootstrap()  # 前端开发框架, 更简洁的 web 开发
mail = Mail()   # 邮件验证
db = SQLAlchemy()  # 数据库持久化存储用户信息
login_manager = LoginManager()  # 优化数据库存储，管理认证系统中用户的认证状态

# session_protection 属性提供不同的安全等级防止用户会话遭篡改。
# - None
# - 'basic'
# - 'strong' : 记录客户端 IP 地址和浏览器的用户代理信息,如果发现异动就登出用户
login_manager.session_protection = 'strong'
# login_view 属性设置登录页面的端点。
login_manager.login_view = 'auth.login'


def create_app(config_name='development'):
    """
    默认创建开发环境的 app 对象
    """
    """
        config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
        }
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    # 用户认证新加的扩展，用户登录程序后, 他们的认证状态要被记录下来, 这样浏览不同的页面时才能记住这个状态。
    # Flask - Login 是个非常有用的小型扩展, 专门用来管理用户认证系统中的认证状态, 且不依赖特定的认证机制。
    login_manager.init_app(app)

    # BP3. 注册蓝图，和 app 关联在一起
    from app.auth import auth
    app.register_blueprint(auth)

    from app.user import user
    app.register_blueprint(user)  # 注册蓝本

    from app.todo import todo
    app.register_blueprint(todo, url_prefix='/todo')   # url_prefix：指定访问该蓝图中定义的视图函数时需要添加的前缀， 没有指定则不加;

    # 附加路由和自定义的错误页面
    # .........后续还需完善， 补充视图和错误页面
    return app

