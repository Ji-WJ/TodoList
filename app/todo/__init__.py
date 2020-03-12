from flask import Blueprint

# BP1. 创建蓝图
    # "todo"是蓝图的名称
    # __name__是蓝图所在路径
todo = Blueprint('todo', __name__)

# 注意：导入包的实质是执行init文件,所以需要额外导入 views 文件
from . import views