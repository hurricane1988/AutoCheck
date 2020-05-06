#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Pie
from Configuration import *

# 获取SQLite3数据库中的操作系统版本.
def getVersionNumber(osversion):
    if query.exec("select count(*) from t_server where os='{0}'".format(osversion)):
        while query.next():
            number = query.value(0)
            result = [osversion,number]
            return result

# 获取SQLite3数据库中的操作系统类型.
def getTypeNumber(ostype):
    if query.exec("select count(*) from t_server where type='{0}'".format(ostype)):
        while query.next():
            number = query.value(0)
            result = [ostype,number]
            return result

# 获取指定关键字中的数量.
def getNumber(queryString):
    if query.exec("select {0} from t_server".format(queryString)):
        data = []
        while query.next():
            line = query.value(0)
            data.append(line)
        return set(data)

# 操作系统饼图加载函数.
def osVersion():
    pip_data = []
    datas = getNumber(queryString='os')
    for line in datas:
        data = getVersionNumber(osversion=line)
        pip_data.append(data)
    return pip_data

# 操作系统版本饼图.
def osType():
    type_data = []
    datas = getNumber(queryString='type')
    for line in datas:
        data = getTypeNumber(line)
        type_data.append(data)
    return type_data

# 获取数据库
def getDBVersionNumber(dbversion):
    if query.exec("select count(*) from t_database where dbversion='{0}'".format(dbversion)):
        while query.next():
            number = query.value(0)
            result = [dbversion,number]
            return result

# 获取指定关键字中的数量.
def getDBNumber(queryString):
    if query.exec("select {0} from t_database".format(queryString)):
        data = []
        while query.next():
            line = query.value(0)
            data.append(line)
        return set(data)

# 获取数据库版本饼图.
def dbVersionPIP():
    pip_data = []
    datas = getDBNumber(queryString='dbversion')
    for line in datas:
        data = getDBVersionNumber(dbversion=line)
        pip_data.append(data)
    return pip_data

osVersionPip = (
    Pie()
    .add(
        "",
        osVersion(),
        radius=["60", "40%"],      # 设置饼图的内环半径
        center=["33%", "28%"],     # 设置饼图在画面中的位置
        label_opts=opts.LabelOpts(
            position="outside",
            #formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            formatter="{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=5,
            rich={
                #"a": {"color": "#999", "lineHeight": 5, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 1,
                    "height": 0,
                },
                "b": {"fontSize": 11, "lineHeight": 25},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
    # .set_global_opts(title_opts=opts.TitleOpts(title="操作系统版本信息"))
    .set_global_opts(
        title_opts=opts.TitleOpts(subtitle="[系统版本比例饼图]"),
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(pos_left="72%",orient="vertical"),
    )
    #.render("./templates/osVersionPip.html")
)

dbVersionPip = (
    Pie()
    .add(
        "",
        dbVersionPIP(),
        radius=["60", "40%"],
        center=["33%", "80%"],
        label_opts=opts.LabelOpts(
            position="outside",
            #formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            formatter="{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=5,
            rich={
                #"a": {"color": "#999", "lineHeight": 5, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 1,
                    "height": 0,
                },
                "b": {"fontSize": 11, "lineHeight": 25},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
    #.set_global_opts(title_opts=opts.TitleOpts(title="操作系统版本信息"))
    .set_global_opts(
        title_opts=opts.TitleOpts(subtitle="[数据库类型饼图]", pos_top="60%"),
        legend_opts=opts.LegendOpts(pos_top="65%" ,pos_left="72%",orient="vertical",is_show=True),
    )
    #.render("./templates/osVersionPip.html")
)


grid = (
    Grid(init_opts=opts.InitOpts(width="1200px",height="450px",theme="white",bg_color="red"))
    .add(dbVersionPip, grid_opts=opts.GridOpts(pos_top="20%"))
    .add(osVersionPip, grid_opts=opts.GridOpts(pos_top="70%"))
    .render("./templates/grid_horizontal.html")
)

def mainpip():
    grid
