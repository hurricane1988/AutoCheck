#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import dns.resolver
from DNSResolute import Ui_FormDNS
from PyQt5 import QtWidgets, QtGui, QtCore


# DNS域名解析主类.
class MyWindowsDNS(QtWidgets.QWidget,Ui_FormDNS):
    
    def __init__(self, parent=None):
        super(MyWindowsDNS, self).__init__(parent)

        self.setWindowIcon(QtGui.QIcon('login.ico'))
        self.setFixedSize(430, 158)
        self.setupUi(self)

        # 域名解析按钮槽与函数绑定.
        self.pushButtonDNS.clicked.connect(self._dnsResolve)

    # 域名解析主函数.
    def _dnsResolve(self):
        domain = self.lineEditDNS.text()

        try:
            A = dns.resolver.query(domain, 'A')
            dns_list = []
            for i in A.response.answer:
                for j in i:
                    if j.rdtype == 1:
                        dns_list.append('IP地址: '+j.address)
            self.textEditDNS.setPlainText("\n".join(dns_list))
            # print(dns_list)

        except dns.resolver.NoAnswer:
            QtWidgets.QMessageBox.warning(self,'错误提示','域名:{0}\nDNS无响应',QtWidgets.QMessageBox.Cancel)
