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
