#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################
# Create Time: 2020-03-07 下午 10:25
# Author: Hurricane1988
# FileName: initdb.py
######################################


import sys,sqlite3
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

    def execSql(self,sql):

        try:
            self.query.exec(sql)
            QMessageBox.about(self,None,'执行SQL{0}成功'.format(sql))

        except Exception as e:
            QMessageBox.warning(self,'错误提示','执行SQL语句{0}失败,错误信息{1}'.format(sql,e))

        finally:
            self.db.close()




