#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################
# Create Time: 2020-03-08 下午 08:14
# Author: Hurricane1988
# FileName: Callmainwindow.py
##########################################


import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QMessageBox
from mainwindow import Ui_MainWindow
from CallMD5 import md5Encrypt
from CallPortScan import portScanWindow
from CallenterInfo import enterWindow
from CallChangePassword import resetPassWord
from Configuration import *


class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        self.setWindowTitle('自助巡检GUI工具')                                        # 设置窗口标题.
        self.setWindowIcon(QIcon('login.ico'))                                      # 设置窗口的图标.
        #self.setFixedSize()
        self.setupUi(self)                                                          # 调用显示窗口.
        self.actionAbout.triggered.connect(self.about_us)                           # 关于我们动作和about_us函数绑定.
        self.actionMD5.triggered.connect(self.md5Encryptshow)                       # MD5动作与MD5加密函数绑定.
        self.actionPortCheck.triggered.connect(self.portScanShow)
        #self.actionResetPassWord.triggered.connect(self.resetPassword)              # 密码重置动作和函数绑定.

        self.actionAddItem.triggered.connect(self.enterInfo)
        self.actionResetPassWord.triggered.connect(self.ResetPasswd)

    # 关于我们帮助文档说明.
    def about_us(self):
        QMessageBox.about(self,'关于我们',MSG)

    # 密码重置函数.
    def md5Encryptshow(self):
        self.MD5 = md5Encrypt()
        self.MD5.show()

    # 端口扫描主函数.
    def portScanShow(self):
        self.portscan = portScanWindow()
        self.portscan.show()

    # 信息录入主函数.
    def enterInfo(self):
        self.inputInfo = enterWindow()
        self.inputInfo.show()

    # 密码重置主函数.
    def ResetPasswd(self):
        self.resetpassword = resetPassWord()
        self.resetpassword.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec())
