from flask import Blueprint

# BP1. 创建蓝图
auth = Blueprint('auth', __name__)    # 'auth'是蓝图的名称， __name__是蓝图所在路径

# 注意：导入包的实质是执行init文件
from . import views