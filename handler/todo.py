#!/usr/bin/env python
# coding: utf-8

from handler.base_handler import BaseHandler
import tornado
from logic import user_logic
from helper import str_helper
from common import log
import datetime


# class BaseHandler(tornado.web.RequestHandler, SessionMixin):
#     def get_current_user(self):
#         user = self.session.get('user')
#         if not user:
#             return None
#         return user
#
#     def get_arg(self, key, default=None, strip=True):
#         val = self.get_argument(key, default, strip)
#         # if val != None and isinstance(val, str):
#         #     val = val.encode('utf-8')
#         # print("222233332",val)
#         return val


class Main(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        # if not user:
        #     self.redirect('/')
        # log.logger.debug(SessionManager.keys())
        self.echo('main.html', context={})
        return

class Jqgrid(BaseHandler):
    def get(self):
        self.echo('jqgrid.pyhtml', {})


class Login(BaseHandler):

    def get(self):
        # user = self.get_current_user()
        # if not user:
        #     self.redirect('/main')
        self.echo('login.html')

    def post(self):
        # log.logger.debug("4545")
        username = self.get_arg("Username")
        password = self.get_arg("Password")
        if username == '' or password == '':
            self.redirect('/')
            return
        user = user_logic.login(username, password)
        if None == user:
            self.redirect('/')
            return
        log.logger.debug(user)
        self.session.set("user", user)
        self.redirect('/main')


class Logout(BaseHandler):
    def get(self):
        self.session.delete('user')
        self.redirect('/')


class UeserManage(BaseHandler):
    def get(self):
        self.echo('userManage.html', {})


class UeserManageList(BaseHandler):
    def get(self):
        users = user_logic.query_page()
        # users.append({'user_key': self.session.get('user_key')})
        print("*********", users)
        user = str_helper.json_encode(users)
        print("++++++++", user)
        self.write(user)

    def post(self, *args, **kwargs):
        # self.get()
        action = self.get_argument('action')
        msg = self.request.body_arguments
        tel4 = self.request.query
        print(self.request)
        # print(self.request)
        print('+++++++++++++++++', msg)
        try:
            print(self.get_arg('data'))
        except Exception as e:
            print('error is :  ', e)
        sid = self.get_arg('id')

        print('id:---------:', sid, 'action', self.get_arg('action'))
        rt = {
            "id": '-1',
            "fieldErrors": [
            {
                "name": "user_id",
                "status": "该项不能为空"
            }
            ],
            "sError": "有错误发生,请联系系统管理员",
            "aaData": []
        }
        srt = str_helper.json_encode(rt)
        print('-----------', srt)
        self.write(srt)
        # users = args
        # # users = str_helper.json_decode(users)
        # user = kwargs
        # # user = str_helper.json_decode(user)
        # print(users, user)
        # self.redirect('/main')


class Test(BaseHandler):
    def get(self):
        self.echo('test.html', {})

