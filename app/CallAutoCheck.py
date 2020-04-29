#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets, QtGui
from AutoCheck import Ui_UIAutoCheck


class MyAutoCheckWindow(QtWidgets.QWidget,Ui_UIAutoCheck):

    def __init__(self, parent=None):
        super(MyAutoCheckWindow, self).__init__(parent)

        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('login.ico'))
        self.setFixedSize(330,170)

        self.pushButtonCance.clicked.connect(self.close)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MyAutoCheckWindow()
    win.show()
    sys.exit(app.exec())