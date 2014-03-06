#!/usr/bin/env python
#-*- encoding: utf-8 -*-
#__author__ = 'qgw'
import tornado.web
# import mako.lookup
# import mako.template
from config import settings
from lib.pycket.session import SessionMixin
from helper import str_helper
import tenjin
# from mako import exceptions
from tenjin.helpers import *

engine = tenjin.Engine(path=[settings.settings['template_path']], cache=tenjin.MemoryCacheStorage(), preprocess=True)
class BaseHandler(tornado.web.RequestHandler, SessionMixin):
    def get_current_user(self):
        user = self.session.get('user')
        return user

    def get_arg(self, key, default=None, strip=True):
        val = self.get_argument(key, default, strip)
        return val

    def render(self, template, context=None, globals=None, layout=False):
        if not context:
            context = {'cust_title': '外勤通管理系统', }
        user = self.get_current_user()
        if None != user:
            # sql = 'select cust_title from wqt_cust where cust_key = %s'
            context = user
            if str_helper.is_null_or_empty(context['cust_title']):
                context['cust_title'] = '外勤通管理系统'
        if template != 'login.html':
            layout = '_layout.pyhtml'

        return engine.render(template, context, globals, layout)

    def echo(self, template, context=None, globals=None, layout=False):
        self.write(self.render(template, context, globals, layout))


