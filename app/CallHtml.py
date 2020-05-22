#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Create Time: 2020-03-15 下午 09:35
# Author: Hurricane1988
# FileName: CallHtml.py

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from html_template import Ui_Form
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtSql
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType


db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName("rundb.db")
if db.open():
    print('连接数据库成功')
else:
    print(db.lastError().text())




def queryCount(str):
    query = QtSql.QSqlQuery("select count(*) from t_server where type='{0}'".format(str))
    while query.next():
    #ID = query.value(0)
    #IP = query.value(1)
    #Version = query.value(2)
    #SystemType = query.value(6)
        count = query.value(0)
        return count

def osType():
    query = QtSql.QSqlQuery("select * from t_server")
    oslist = []
    while query.next():
        SystemType = query.value(6)
        oslist.append(SystemType)
    return set(oslist)

for line in osType():
    c = (
        Bar({"theme": ThemeType.MACARONS})
            .add_xaxis(Faker.choose())
            .add_yaxis(line, queryCount(line))
            .set_global_opts(
            title_opts={"操作系统类型图": "Bar-通过 dict 进行配置", "subtext": "我也是通过 dict 进行配置的"}
        )
            .render("./templates/bar_base_dict_config.html")
    )



