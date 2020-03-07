#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########################################
# Create Time: 2020-03-07 下午 09:12
# Author: Hurricane1988
# FileName: callLogin.py
########################################


import sys
from PyQt5.QtWidgets import QDesktopWidget,QApplication,QWidget
from login import Ui_loginUi


class loginWindow(QWidget,Ui_loginUi):
    def __init__(self, parent=None):
        super(loginWindow, self).__init__(parent)
        self.setWindowTitle('欢迎使用自动巡检工具')

        self.setupUi(self)
        self.center()

    def center(self):
        SCREEN = QDesktopWidget().screenGeometry()
        SIZE = self.geometry()
        self.move((SCREEN.width() - SIZE.width()) /2,
                  (SCREEN.height() - SIZE.height()) /2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = loginWindow()
    win.show()
    sys.exit(app.exec())
