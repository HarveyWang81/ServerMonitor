#!/usr/bin/env python
# coding:utf-8

__author__ = "学神IT-Python-1608-阳光"

import os, re
try:
    import SocketServer as socketserver # python 2.x
except Exception as e:
    import socketserver # python 3.x

from time import ctime

try:
    import MySQLdb as sql # python 2.x
except Exception as e:
    import pymysql as sql # python 3.x



class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class Server(object):
    def __init__(self):
        ip, port = "", 140127

        log_file_path = os.path.dirname(
            os.path.abspath(__file__)) + os.path.sep + "logs" + os.path.sep + "Server_SystemErr.log"
        try:
            self.log_file_error = open(log_file_path, "a+")  # 打开 SystemErr.log 日志
            self.sock = ThreadedTCPServer((ip, port),ThreadedTCPRequestHandler)
        except Exception as e:
            self.sock = None
            self.logger(e)

    def logger(self, content):
        self.log_file_error.write("[%s] %s" % (ctime(), content))  # 输出错误日志

    def recv_data(self):
        pass

    def save_data(self, data):
        user =
        passwd =
        host =
        port =



        conn = sql.connect()


    def __del__(self):
        self.sock.close()
        self.log_file_error.close()

    def main(self):
        self.recv_data()


if __name__ == '__main__':
    s = Server()
    s.main()
