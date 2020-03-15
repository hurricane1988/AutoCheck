#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Create Time: 2020-03-08 下午 02:57
# Author: Hurricane1988
# FileName: test.py


"""
import sqlite3

conn = sqlite3.connect('rundb.db')
c = conn.cursor()
print('Open database successfully!')

createUser = '''
        create table if not exists user
        (id int primary key,
        username varchar(20),
        password varchar(20));
        '''

insertUser = '''
        insert into user (id,username,password) 
        values (1,'admin','771998c12c56ba94db225f252d24127c');
        '''
c.execute(createUser)
c.execute(insertUser)
conn.commit()

password = c.execute("select password from user where username='admin'").fetchone()[0]
#password = [row[2]for row in data][0]
print(type(password))
c.close()
"""

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker

c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values(), category_gap="60%")
    .set_series_opts(
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(0, 244, 255, 1)'
            }, {
                offset: 1,
                color: 'yellow'
            }], false)"""
                ),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": "rgb(0, 160, 221)",
            }
        }
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-渐变圆柱"))
    .render("./templates/test.html")
)
