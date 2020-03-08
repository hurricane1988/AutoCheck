#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################
# Create Time: 2020-03-08 下午 08:14
# Author: Hurricane1988
# FileName: Callmainwindow.py
##########################################


import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow
from mainwindow import Ui_MainWindow


class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        self.setWindowTitle('主页')
        self.setWindowIcon(QIcon('login.ico'))

        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec())
