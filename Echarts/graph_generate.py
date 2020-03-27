#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Pie
from Configuration import *

# 获取SQLite3数据库中的操作系统版本.
def getVersionNumber(osversion):
    if query.exec("select count(*) from t_server where os='{0}'".format(osversion)):
        while query.next():
            number = query.value(0)
            result = {'osversion':osversion,'number':number}
            # print(result)
            return result

# 获取SQLite3数据库中的操作系统类型.
def getTypeNumber(ostype):
    if query.exec("select count(*) from t_server where type='{0}'".format(ostype)):
        while query.next():
            number = query.value(0)
            result = {'ostype':ostype,'number':number}
            # print(result)
            return result

# 获取指定关键字中的数量.
def getNumber(queryString):
    if query.exec("select {0} from t_server".format(queryString)):
        data = []
        while query.next():
            line = query.value(0)
            data.append(line)
        return set(data)

# 使用pyecharts生产可视化图表.
def generatePip(title):

