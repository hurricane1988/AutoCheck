#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########################################
# Create Time: 2020-05-23 下午 08:36
# Author: Hurricane1988
# FileName: ulimit_check_window.py
#########################################


import sys
from PyQt5 import QtGui,QtCore,QtWidgets
from ulimit_check_ui import Ui_ulimitCheck
from main_ulimit_check import ulimitworkThread


# 定义主窗口类.
class checkWindow(QtWidgets.QWidget, Ui_ulimitCheck,QtCore.QThread):

    def __init__(self, parent=None):
        super(checkWindow, self).__init__(parent)

        self.setupUi(self)
        self.setFixedSize(585, 239)
        self.setWindowIcon(QtGui.QIcon("login.ico"))

        self.work_thread = ulimitworkThread()                              # 初始化线程函数
        self.pushButtonOK.clicked.connect(self.ulimit_thread_slot)         # 信号与槽函数绑定
        self.pushButtonCance.clicked.connect(self.close)

    # 带有启动线程的槽函数.
    def ulimit_thread_slot(self):
        if self.checkBoxUlimit.isChecked():
            self.pushButtonOK.setEnabled(True)                                # 开始按钮不可点击
            self.work_thread.start()                                          # 线程开始
        else:
            QtWidgets.QMessageBox.warning(self,'提示信息','请勾选检查项',QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = checkWindow()
    win.show()
    sys.exit(app.exec())


