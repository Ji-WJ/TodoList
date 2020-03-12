from threading import Thread

from flask import current_app, render_template
from flask_mail import Mail, Message


def thread_task(app, mail, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(to, subject, filename, **kwargs):
    """
    发送邮件的封装
    :param to: 收件人
    :param subject: 邮件主题
    :param filename: 邮件正文对应的html名称
    :param kwargs: 关键字参数, 模版中需要的变量名
    :return:
    """
    app = current_app._get_current_object()
    # 初始化mail对象, 一定要先配置邮件信息;
    mail = Mail(app)
    msg = Message(subject=subject,
                  sender='huadoukaihaole0611@163.com',
                  recipients=to)
    # msg.body = "info"
    msg.html = render_template(filename + '.html', **kwargs)
    # with app.app_context():
    #     mail.send(msg)
    thread = Thread(target=thread_task, args=(app, mail, msg))
    thread.start()
    return thread