#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########################################
# Create Time: 2020-05-23 下午 08:36
# Author: Hurricane1988
# FileName: ulimit_check_window.py
#########################################


import sys,os
import base64
from image import logo
from PyQt5 import QtGui,QtCore,QtWidgets
from ulimit_check_ui import Ui_ulimitCheck
from main_ulimit_check import ulimitworkThread


# 定义主窗口类.
class checkWindow(QtWidgets.QWidget, Ui_ulimitCheck, QtCore.QThread):

    def __init__(self, parent=None):
        super(checkWindow, self).__init__(parent)


        self.setupUi(self)
        self.setFixedSize(585, 239)
        icon = QtGui.QIcon()                                                     # 设置icon图标
        logo_image = base64.b16decode(logo)                                      # base64解析二进制文件
        Pixmap = QtGui.QPixmap()                                                 # 用于绘制图像的类
        Pixmap.loadFromData(logo_image)                                          # 加载图像二进制数据
        icon.addPixmap(Pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)                                                 # 设置GUI图标
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)                      # 设置无边框窗口
        # self.setWindowIcon(QtGui.QIcon("login.ico"))

        self.work_thread = ulimitworkThread()                                    # 初始化线程函数
        #self.ulimit_check_slot = ulimitCheckSlot()
        self.pushButtonOK.clicked.connect(self.ulimit_thread_slot)               # 信号与槽函数绑定
        self.pushButtonCance.clicked.connect(self.close)

    # 带有启动线程的槽函数.
    def ulimit_thread_slot(self):

        if os.path.exists('checkhosts.csv'):
            if self.checkBoxUlimit.isChecked():
                self.pushButtonOK.setEnabled(True)                                 # 开始按钮不可点击
                self.work_thread.start()                                           # 线程开始
                self.work_thread.finshSignal.connect(self.resutl_notice)

            else:
                QtWidgets.QMessageBox.warning(self,'提示信息','请勾选检查项',QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(self,'提示信息','未查找到checkhosts.csv配置文件',QtWidgets.QMessageBox.Ok)


    def resutl_notice(self):
        result_path = os.getcwd()
        QtWidgets.QMessageBox.information(self, '消息提示',
                                          '状态: 系统ulimit检查结束\n检查结果存放路径: {0}\系统内核参数检查结果.csv'.format(result_path),
                                          QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = checkWindow()
    win.show()
    sys.exit(app.exec())


