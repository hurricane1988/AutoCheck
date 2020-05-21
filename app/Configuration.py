#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################
# Create Time: 2020-03-15 下午 07:51
# Author: Hurricane1988
# FileName: Configuration.py
########################################

import sqlite3,hashlib,logging
from PyQt5.QtSql import QSqlDatabase,QSqlQueryModel,QSqlQuery

# 初始化数据库连接信息.
#connect = sqlite3.connect("rundb.db")
#cursor = connect.cursor()

# 初始化数据库连接.
database = QSqlDatabase.addDatabase('QSQLITE')
database.setDatabaseName('rundb.db')
database.open()
query = QSqlQuery()
queryModelServer = QSqlQueryModel()
queryModelDB = QSqlQueryModel()

connect = sqlite3.connect('rundb.db')
cursor = connect.cursor()
# 定义帮助信息文本.
MSG = '''
        所属部门: 华信永道运维与客户服务部
        创建日期: 2020年5月18日
        运行环境: Windows10 64位
        '''


def md5Encrypt(msg):
    try:
        plainText = hashlib.md5(msg.encode())
        cipherText = plainText.hexdigest()
        return cipherText

    except Exception as e:
        logging.error('加密字符串{0}失败，{1}'.format(msg, e))

    finally:
        pass