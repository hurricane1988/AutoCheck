#!/usr/bin/env python
# -*- coding: utf-8 -*-

import IPy
import urllib3
from PyQt5 import QtWidgets, QtGui
from ipResolve import Ui_IpResolve


class ipResolveWindow(QtWidgets.QWidget, Ui_IpResolve):
    def __init__(self, parent=None):
        super(ipResolveWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('login.ico'))
        self.setupUi(self)

        self.pushButtonResolve.clicked.connect(self.showResolveResults)

    # IP地址格式判断函数.
    def isIP(self,ip):
        try:
            IPy.IP(ip)
            return True
        except Exception as e:
            QtWidgets.QMessageBox.warning(self,'错误提示','你输入的IP地址格式错误!')
            return False

    # 公网IP地址信息查询结果函数.
    def showResolveResults(self):
        try:
            url = "http://ip-api.com/json/"
            IP = self.lineEdit.text()
            if self.isIP(IP) is True:
                headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                parameter = {'ip': IP}
                http = urllib3.PoolManager()
                response = http.request(method='get', url=url, fields=parameter, headers=headers, timeout=3)
                results = eval(response.data.decode())
                # print(response.data.decode())
                country = results['country']
                regionName = results['regionName']
                city = results['city']
                org = results['org']
                msg = 'IP地址 : '+IP+'\n'+'国  家: '+country+'\n'+'省  份: '+regionName+'\n'+'城  市: '+city+'\n'+'地  址: '+org
                self.textEditResolveResult.setText(msg)
            else:
                pass
        except Exception as e:
            QtWidgets.QMessageBox.warning(self,'错误提示','无法访问互联网,请检查网络连接!')
            pass

