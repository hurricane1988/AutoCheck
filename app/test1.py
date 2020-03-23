#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib3
import geoip2.database

headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

#url = 'http://ip.taobao.com/service/getIpInfo.php'
url = 'http://ip-api.com/json/'
vaules = {'ip':'47.92.135.119'}

http = urllib3.PoolManager()
r = http.request(method='get',url=url,fields=vaules,headers=headers)
print(eval(r.data.decode()))


