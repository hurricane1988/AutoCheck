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


class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        self.setWindowTitle('自助巡检GUI工具')                                                 # 设置窗口标题.
        self.setWindowIcon(QIcon('login.ico'))                                      # 设置窗口的图标.

        self.setupUi(self)                                                          # 调用显示窗口.
        self.actionAbout.triggered.connect(self.about_us)                           # 关于我们动作和about_us函数绑定.
        self.actionMD5.triggered.connect(self.md5Encrypt)                           # MD5动作与MD5加密函数绑定.
        #self.actionResetPassWord.triggered.connect(self.resetPassword)              # 密码重置动作和函数绑定.

    # 关于我们帮助文档说明.
    def about_us(self):
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
        QMessageBox.about(self,'关于我们',MSG)

    # 密码重置函数.



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec())
