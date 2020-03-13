#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,hashlib,logging
from PyQt5 import QtCore, QtGui, QtWidgets
from MD5 import Ui_MD5

class md5Encrypt(QtWidgets.QWidget,Ui_MD5):
    def __init__(self, parent=None):
        super(md5Encrypt, self).__init__(parent)
        self.setupUi(self)
        self.pushButtonMD5.clicked.connect(self.showCipher)

    # md5字符加密函数.
    def showCipher(self):
        try:
            if self.lineEditInput.text().strip() == '':
                QtWidgets.QMessageBox.warning(self,'错误提示','要加密的字符串不能为空',QtWidgets.QMessageBox.Cancel)
            else:
                convertBytes = hashlib.md5(self.lineEditInput.text().encode('utf-8'))
                Cypher32_lower = convertBytes.hexdigest()
                Cypher32_upper = convertBytes.hexdigest().upper()
                Cypher16_lower = convertBytes.hexdigest()[8:-8]
                Cypher16_upper = convertBytes.hexdigest()[8:-8].upper()
                self.lineEditString.setText(self.lineEditInput.text())
                self.lineEdit16min.setText(Cypher16_lower)
                self.lineEdit16max.setText(Cypher16_upper)
                self.lineEdit32min.setText(Cypher32_lower)
                self.lineEdit32max.setText(Cypher32_upper)

        except Exception as e:
            logging.error('MD5加密错误，{0}'.format(e))

        finally:
            pass