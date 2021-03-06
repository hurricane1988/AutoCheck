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
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.faker import Faker

def pie_rosetype() -> Pie:
    v = Faker.choose()
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["75%", "50%"],
            rosetype="area",
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图示例"))
    )
    return c

def page_simple_layout():
    page = Page(layout=Page.SimplePageLayout)
    page.add(
        pie_rosetype(),
    )
    page.render("./templates/page_simple_layout.html")


if __name__ == '__main__':
    page_simple_layout()