#!/usr/bin/env python
#-*- encoding: utf-8 -*-
#__author__ = 'qgw'
# import errno
# import functools
# import socket
# from tornado import ioloop, iostream
#
#
# class Connection(object):
#     def __init__(self, connection):
#         self.stream = iostream.IOStream(connection)
#         self._read()
#
#     def _read(self):
#         self.stream.read_until('\r\n', self._eol_callback)
#
#     def _eol_callback(self, data):
#         self.handle_data(data)
#
#
# def connection_ready(sock, fd, events):
#     while True:
#         try:
#             connection, address = sock.accept()
#         except socket.error, e:
#             if e[0] not in (errno.EWOULDBLOCK, errno.EAGAIN):
#                 raise
#             return
#         else:
#             connection.setblocking(0)
#             CommunicationHandler(connection)
#
#
# class CommunicationHandler(Connection):
#     """Put your app logic here"""
#     def handle_data(self, data):
#         self.stream.write(data)
#         self._read()
#
#
# if __name__ == '__main__':
#
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     sock.setblocking(0)
#     sock.bind(("127.0.0.1", 8888))
#     sock.listen(128)
#
#     io_loop = ioloop.IOLoop.instance()
#     callback = functools.partial(connection_ready, sock)
#     io_loop.add_handler(sock.fileno(), callback, io_loop.READ)
#
#     try:
#         io_loop.start()
#     except KeyboardInterrupt:
#         io_loop.stop()
#         print "exited cleanly"
import tornado.ioloop
import tornado.iostream
import socket

def send_request():
    stream.write(b"GET / HTTP/1.0\r\nHost: friendfeed.com\r\n\r\n")
    stream.read_until(b"\r\n\r\n", on_headers)

def on_headers(data):
    headers = {}
    for line in data.split(b"\r\n"):
       parts = line.split(b":")
       if len(parts) == 2:
           headers[parts[0].strip()] = parts[1].strip()
    stream.read_bytes(int(headers[b"Content-Length"]), on_body)

def on_body(data):
    print data
    stream.close()
    tornado.ioloop.IOLoop.instance().stop()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
stream = tornado.iostream.IOStream(s)
stream.connect(("friendfeed.com", 80), send_request)
tornado.ioloop.IOLoop.instance().start()