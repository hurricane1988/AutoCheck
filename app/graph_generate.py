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

osVersionPip = (
    Pie()
    .add(
        "",
        osVersion(),
        radius=["55", "40%"],
        center=["38%", "28%"],
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
        #title_opts=opts.TitleOpts(title="Pie-Legend 滚动"),
        legend_opts=opts.LegendOpts(type_="scroll",  pos_left="85%",orient="vertical"),
    )
    #.render("./templates/osVersionPip.html")
)

osTypePip = (
    Pie()
    .add(
        "",
        osType(),
        radius=["55", "40%"],
        center=["38%", "80%"],
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
        #title_opts=opts.TitleOpts(title="Pie-Legend 滚动"),
        legend_opts=opts.LegendOpts(type_="scroll", pos_top="55%" ,pos_left="85%",orient="vertical",is_show=True),
    )
    #.render("./templates/osVersionPip.html")
)


grid = (
    Grid()
    .add(osTypePip,grid_opts=opts.GridOpts(pos_bottom="60%"))
    .add(osVersionPip, grid_opts=opts.GridOpts(pos_top="60%"))
    .render("./templates/grid_horizontal.html")
)

def mainpip():
    grid

if __name__ == '__main__':
    mainpip()
