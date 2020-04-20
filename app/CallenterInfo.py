#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################
# Create Time: 2020-03-14 下午 07:20
# Author: Hurricane1988
# FileName: CallenterInfo.py
########################################

import socket
from Configuration import connect,cursor
from PyQt5 import QtWidgets, QtCore, QtGui
from enterInfo import Ui_EnterInfo


# 信息录入主类.
class enterWindow(QtWidgets.QWidget,Ui_EnterInfo):
    def __init__(self, parent=None):
        super(enterWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('login.ico'))
        self.setFixedSize(489,359)

        # 加载图形化主函数.
        self.setupUi(self)
        # 服务器信息录入.
        self.pushButtonServerEntry.clicked.connect(self.ServersEntry)
        self.pushButtonServerQuit.clicked.connect(self.close)
        # 数据库信息录入.
        self.pushButtonDBEntry.clicked.connect(self.DatabaseEntry)
        self.pushButtonDBQuit.clicked.connect(self.close)

    # 信息录入主函数.
    def ServersEntry(self):
        self.ostype = self.comboBoxSelectServerOS.currentText()
        self.version = self.comboBoxSelectServerVersion.currentText()
        self.IP = self.lineEditServerIP.text()
        self.username = self.lineEditServerUserName.text()
        self.password = self.lineEditServerPassWord.text()
        self.password_ensure = self.lineEditServerEnsure.text()
        self.description = self.plainTextEditServerDescription.toPlainText()  # 获取plainTextEdit值方法

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
                    connect.close()

            except AttributeError:
                try:
                    socket.inet_aton(self.IP)
                except socket.error:
                    return False
            except socket.error:
                QtWidgets.QMessageBox.warning(self,'错误提示','输入的IP地址为非法格式',QtWidgets.QMessageBox.Cancel)

    # 数据库信息录入主函数.
    def DatabaseEntry(self):
        self.dbtype = self.comboBoxSelectDB.currentText()
        self.dbversion = self.comboBoxSelectDBVersion.currentText()
        self.dbip = self.lineEditDBIP.text()
        self.dbusername = self.lineEditDBUserName.text()
        self.dbname = self.lineEditDatabaseName.text()
        self.dbpassword = self.lineEditDBPassWord.text()
        self.dbpassword_ensure = self.lineEditDBEnsure.text()
        self.dbdescription = self.plainTextEditDBDescription.toPlainText()

        if self.dbpassword == self.dbpassword_ensure:
            try:
                socket.inet_pton(socket.AF_INET,self.dbip)
                try:
                    cursor.execute("insert into t_database (ip,dbtype,dbversion,dbname,username,password,desc) values ('{}','{}','{}','{}','{}','{}','{}')".format(self.dbip,self.dbtype,self.dbversion,self.dbname,self.dbusername,self.dbpassword,self.dbdescription))
                    connect.commit()
                    QtWidgets.QMessageBox.information(self, '消息提示', '成功录入信息', QtWidgets.QMessageBox.Cancel)
                except Exception as e:
                    QtWidgets.QMessageBox.warning(self,'错误提示',"信息录入失败\n'{0}".format(e),QtWidgets.QMessageBox.Cancel)
                    pass
                finally:
                    connect.close()

            except AttributeError:
                try:
                    socket.inet_aton(self.dbip)
                except socket.error:
                    return False
            except socket.error:
                QtWidgets.QMessageBox.warning(self,'错误提示','输入的IP地址为非法格式',QtWidgets.QMessageBox.Cancel)