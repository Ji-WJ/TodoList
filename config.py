import os
# 获取当前项目的绝对路径;
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    所有配置环境的基类, 包含通用的配置
    """
    # SECRET_KEY 尤其是在涉及（flask-wtf）登录注册里面提交敏感信息时一定要加
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my secret key'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[才华有限公司]'
    FLASKY_MAIL_SENDER = '137965306@qq.com'
    PER_PAGE = 2

    @staticmethod
    def init_app(app):
        """初始化app，用来添加第三方插件"""
        pass


class DevelopmentConfig(Config):
    """
    开发环境的配置信息
    """
    # 启用了调试支持，服务器会在代码修改后自动重新载入，并在发生错误时提供一个相当有用的调试器。
    DEBUG = True
    # 添加的发送邮件的配置信息
    MAIL_SERVER = 'smtp.163.com'
    # 指定端口, 默认25, 但qq邮箱默认为 端口号465或587;
    MAIL_PORT = 25
    # MAIL_USE_TLS = True or MAIL_USE_TLS = True 由于QQ邮箱不支持非加密的协议,那么使用加密协议, 分为两种加密协议,选择其中之一即可
    MAIL_USERNAME = 'huadoukaihaole0611@163.com'
    MAIL_PASSWORD = 'python123'  # 授权码非邮箱登陆密码
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    """
    测试环境的配置信息
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    """
    生产环境的配置信息
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
