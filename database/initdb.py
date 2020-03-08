#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################
# Create Time: 2020-03-07 下午 10:25
# Author: Hurricane1988
# FileName: initdb.py
######################################


import sys,sqlite3,hashlib,logging
from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox


# 初始化SQLite3数据库类.
class SQLiteOperate(object):
    def __init__(self, dbname='rundb.db'):
        self.dbname = dbname
        self.query = QSqlQuery()
        try:
            # 加载QSQLITE数据库驱动.
            self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
            self.db.setDatabaseName(self.dbname)         # 设置数据库名称为rundb.

            if not self.db.open():
                QMessageBox.critical(self,'操作数据库错误',
                                 '无法连接rundb数据库,请检查数据库配置',QMessageBox.Cancel)

        except Exception as e:
            QMessageBox.warning(self,'错误提示','初始化rundb数据库失败,{0}'.format(e))

    # 定义连接.
    def connect(self):
        try:
            connect = sqlite3.connect("rundb.db")
            return connect

        except Exception as e:
            pass

        finally:
            pass

    # 定义SQLite3的游标.
    def execSql(self):
        connect = self.connect()
        try:
           cursor = connect.cursor()
           print('connect to database rundb successfully')
           return cursor

        except Exception as e:
           print('connect to database rundb failed,{0}'.format(e))
           return False

        finally:
            pass

    # MD5加密函数,用于对密码进行加密处理.
    def md5Encrypt(self,msg):
        try:
            plainText = hashlib.md5(msg.encode())
            cipherText = plainText.hexdigest()
            return cipherText

        except Exception as e:
            logging.error('加密字符串{0}失败，{1}'.format(msg,e))

        finally:
            pass





