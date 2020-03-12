"""
用于启动应用程序及其他的程序任务
"""
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.model import User, Role


app = create_app()
manager = Manager(app)
# 将数据库迁移插件与数据库db和app关联
migrate = Migrate(app, db)


@manager.command
def test():
    """
    执行Flask项目的测试用例
    调用： python manage.py test
    :return:
    """
    import unittest
    # 发现所有的测试用例（TestCase）绑定一个测试集合（TestSuite），
    tests = unittest.TestLoader().discover('tests')
    # verbosity是测试结果的信息复杂度，具有0，1，2三个复杂度
    unittest.TextTestRunner(verbosity=2).run(tests)

def make_shell_context():
    return dict(app=app, db=db, Role=Role, User=User)


if __name__ == '__main__':
    # 初始化 Flask-Script、Flask-Migrate 和为 Python shell 定义的上下文。
    manager.add_command("shell", Shell(make_context=make_shell_context))
    manager.add_command("db", MigrateCommand)
    manager.run()

    # app = create_app()
    # # 0.0.0.0 代表任意，可以绑定本机的所有的ip
    # app.run(host='0.0.0.0', port='8888')
