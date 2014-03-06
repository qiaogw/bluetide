#!/usr/bin/env python
# coding: utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import options, define
# noinspection PyUnresolvedReferences,PyUnresolvedReferences
# from config.settings import options as opti
from config import settings, url

define("port", default=8888, help="Count Run server on a specific port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url.handlers, **(settings.settings))


def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    tornado.options.parse_command_line()
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
if __name__ == "__main__":
    main()