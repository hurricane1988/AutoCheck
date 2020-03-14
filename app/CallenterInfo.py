#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################
# Create Time: 2020-03-14 下午 07:20
# Author: Hurricane1988
# FileName: CallenterInfo.py
########################################

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from enterInfo import Ui_enterInfo


class enterWindow(QtWidgets.QWidget,Ui_enterInfo):
    def __init__(self, parent=None):
        super(enterWindow, self).__init__(parent)

        self.setupUi(self)

        self.pushButtonEntry.clicked.connect(self.ensureEntry)
        self.pushButtonQuit.clicked.connect(self.close)

    # 信息录入主函数.
    def ensureEntry(self):
        self.ostype = self.comboBoxSelectOS.currentText()
        self.version = self.lineEditVersion.text()
        self.IP = self.lineEditIP.text()
        self.username = self.lineEditUserName.text()
        self.password = self.lineEditPassWord.text()
        self.password_ensure = self.lineEditEnsure.text()
        #self.plainTextEditDescription.toPlainText()  # 获取plainTextEdit值方法
        #self.plainTextEditDescription.setPlainText()  # 设置plainTextEdit值方法


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = enterWindow()
    win.showMaximized()
    sys.exit(app.exec())
