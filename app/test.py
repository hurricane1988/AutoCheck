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

import hashlib

s = '华信永道'
m = hashlib.md5(s.encode('utf-8'))
a = m.hexdigest()

byte16 = m.hexdigest()[8:-8]
print(a)
print(a.upper().lower())
print(byte16)