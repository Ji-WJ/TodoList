"""
File: views.py
Author: J
Date: 2020-03-07
Connect: 
Description: 
"""

# BP2. 应用蓝图，管理路由
from flask import render_template

from app.todo import todo


@todo.route('/')
def index():
    return render_template('todo/index.html')

@todo.route('/add/')
def add():
    return "todo add"


@todo.route('/delete/')
def delete():
    return "todo delete"