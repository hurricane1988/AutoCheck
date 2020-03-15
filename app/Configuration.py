#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################
# Create Time: 2020-03-15 下午 07:51
# Author: Hurricane1988
# FileName: Configuration.py
########################################

import sqlite3


connect = sqlite3.connect("rundb.db")
cursor = connect.cursor()
MSG = '''
        PyCharm 2019.3 (Professional Edition)
        Build #PY-193.5233.109, built on November 28, 2019
        Licensed to https://zhile.io
        You have a perpetual fallback license for this version
        Subscription is active until July 8, 2089
        Runtime version: 11.0.4+10-b520.11 amd64
        VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
        Windows 10 10.0
        GC: ParNew, ConcurrentMarkSweep
        Memory: 1945M
        Cores: 8
        Registry: 
        Non-Bundled Plugins: ru.meanmail.plugin.requirements
        '''
