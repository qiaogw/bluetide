#!/usr/bin/env python
# coding: utf-8

import os.path

# from tornado.options import define, options



settings = dict(
    cookie_secret="32oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    static_path=os.path.join(os.path.dirname(__file__), "./../static"),
    template_path=os.path.join(os.path.dirname(__file__), "./../templates"),
    #系统调试模式，服务器可设置为False
    debug=True,
    logout_url='/logout',
    login_url='/',
)




#系统数据库配置，根据实际情况修改
db = {
    'host' : '127.0.0.1',
    'port' : 3306,
    'user' : 'root',
    'passwd' : '',
    'db' : 'wqt',
    'charset' : "utf8"
}

settings['pycket']={
        'engine': 'redis',
        'storage': {
            'host': 'localhost',
            'port': 6379,
            'db_sessions': 10,
            'db_notifications': 11,
            'max_connections': 2 ** 31,
        },
        'cookies': {
            'expires_days': 120,
        },
}


