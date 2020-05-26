#!/usr/bin/env python
# -*- coding: utf-8 -*-


import base64


open_icon = open('login.ico','rb')
b64str = base64.b16encode(open_icon.read())
open_icon.close()

write_data = 'logo = %s' % b64str

f = open("image.py",'w+')
f.write(write_data)
f.close()