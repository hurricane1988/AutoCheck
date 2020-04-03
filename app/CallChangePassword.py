#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################
# Create Time: 2020-03-15 下午 08:36
# Author: Hurricane1988
# FileName: CallChangePassword.py
######################################

import sqlite3
from PyQt5 import QtWidgets,QtGui,QtCore
from ChangePassword import Ui_ChangePassWord
from Configuration import md5Encrypt


# 处理数据主类.
class resetPassWord(QtWidgets.QDialog,Ui_ChangePassWord):

    def __init__(self, parent=None):
        super(resetPassWord, self).__init__(parent)
        self.database = sqlite3.connect("rundb.db")
        self.cursor = self.database.cursor()
        #self.setWindowTitle('修改密码')
        #self.setWindowFlags(Qt.FramelessWindowHint)  #设置无边框
        self.setupUi(self)

        self.pushButtonOK.clicked.connect(self.changePassword)
        self.pushButtonCancel.clicked.connect(self.close)

    def changePassword(self):
        passwdNew = self.lineEditPassWord.text()
        passwd = self.lineEditPassWordCheck.text()
        EncryptPassword = md5Encrypt(passwd)
        #print("第一次密码:" + passwdNew,'第二次密码:' + passwd)

        if passwdNew == passwd:
            try:
                if self.cursor.execute("update user set password = '{}' where username='admin'".format(EncryptPassword)):
                    self.database.commit()
                    self.cursor.close()
                    QtWidgets.QMessageBox.information(self, '消息提示', '密码修改成功!', QtWidgets.QMessageBox.Cancel)

            except Exception as e:
                print(e)
            finally:
                self.database.close()
                self.close()
        else:
            QtWidgets.QMessageBox.warning(self,'错误提示','两次密码输入不一致!',QtWidgets.QMessageBox.Cancel)