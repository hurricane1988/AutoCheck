#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################
# Create Time: 2020-03-14 下午 07:20
# Author: Hurricane1988
# FileName: CallenterInfo.py
########################################

import sys,socket,sqlite3
from Configuration import *
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
        self.version = self.comboBoxSelectVersion.currentText()
        self.IP = self.lineEditIP.text()
        self.username = self.lineEditUserName.text()
        self.password = self.lineEditPassWord.text()
        self.password_ensure = self.lineEditEnsure.text()
        self.description = self.plainTextEditDescription.toPlainText()  # 获取plainTextEdit值方法
        #self.plainTextEditDescription.setPlainText()  # 设置plainTextEdit值方法

        # 判断输入的IP格式是否正确.
        if self.password == self.password_ensure:
            try:
                socket.inet_pton(socket.AF_INET,self.IP)
                try:
                    cursor.execute("insert into t_server (ip,os,username,password,desc,type) values ('{}','{}','{}','{}','{}','{}')".format(self.IP,self.version,self.username,self.password,self.description,self.ostype))
                    connect.commit()
                    QtWidgets.QMessageBox.information(self,'消息提示','成功录入信息',QtWidgets.QMessageBox.Cancel)
                except Exception as e:
                    QtWidgets.QMessageBox.warning(self,'错误提示',"信息录入失败\n'{0}".format(e),QtWidgets.QMessageBox.Cancel)
                    pass
                finally:
                    pass
            except AttributeError:
                try:
                    socket.inet_aton(self.IP)
                except socket.error:
                    return False
            except socket.error:
                QtWidgets.QMessageBox.warning(self,'错误提示','输入的IP地址为非法格式',QtWidgets.QMessageBox.Cancel)

        elif self.password is not self.password_ensure:
            QtWidgets.QMessageBox.warning(self,'错误提示','两次输入的密码不一致',QtWidgets.QMessageBox.Cancel)

        elif self.version == '':
            QtWidgets.QMessageBox.warning(self, '错误提示', '系统版本未填写', QtWidgets.QMessageBox.Cancel)
        elif self.IP == '':
            QtWidgets.QMessageBox.warning(self, '错误提示', 'IP地址未填写', QtWidgets.QMessageBox.Cancel)
        elif self.username == '':
            QtWidgets.QMessageBox.warning(self, '错误提示', '账号未填写', QtWidgets.QMessageBox.Cancel)
        elif self.password == '' or self.password_ensure == '':
            QtWidgets.QMessageBox.warning(self, '错误提示', '密码为填写', QtWidgets.QMessageBox.Cancel)
        elif self.description == '':
            QtWidgets.QMessageBox.warning(self, '错误提示', '服务器用途未填写', QtWidgets.QMessageBox.Cancel)