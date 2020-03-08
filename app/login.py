# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys,base64,logging
from PyQt5.QtWidgets import QDesktopWidget,QApplication,QWidget,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QPixmap, QImage,QIcon
from database.initdb import SQLiteOperate


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
class Ui_loginUi(object):
    def setupUi(self, loginUi):
        loginUi.setObjectName("loginUi")
        loginUi.resize(400, 169)
        loginUi.setMinimumSize(QtCore.QSize(400, 150))
        loginUi.setWindowIcon(QIcon('login.ico'))

        self.pushButtonLogin = QtWidgets.QPushButton(loginUi)
        self.pushButtonLogin.setGeometry(QtCore.QRect(190, 120, 75, 23))
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:10px;")
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.pushButtonCancel = QtWidgets.QPushButton(loginUi)
        self.pushButtonCancel.setGeometry(QtCore.QRect(300, 120, 75, 23))
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonCancel.setFont(font)
        self.pushButtonCancel.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:10px;")
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.widget = QtWidgets.QWidget(loginUi)
        self.widget.setGeometry(QtCore.QRect(190, 30, 189, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelUser = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(11)
        self.labelUser.setFont(font)
        self.labelUser.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color: rgb(166, 166, 166);")
        self.labelUser.setObjectName("labelUser")
        self.horizontalLayout.addWidget(self.labelUser)
        self.lineEditUser = QtWidgets.QLineEdit(self.widget)
        self.lineEditUser.setObjectName("lineEditUser")
        self.horizontalLayout.addWidget(self.lineEditUser)
        self.widget1 = QtWidgets.QWidget(loginUi)
        self.widget1.setGeometry(QtCore.QRect(190, 70, 189, 22))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelPassword = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(11)
        self.labelPassword.setFont(font)
        self.labelPassword.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color: rgb(166, 166, 166);")
        self.labelPassword.setObjectName("labelPassword")
        self.horizontalLayout_2.addWidget(self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(self.widget1)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.horizontalLayout_2.addWidget(self.lineEditPassword)

        self.retranslateUi(loginUi)
        QtCore.QMetaObject.connectSlotsByName(loginUi)

    def retranslateUi(self, loginUi):
        _translate = QtCore.QCoreApplication.translate
        self.pushButtonLogin.setText(_translate("loginUi", "登陆"))
        self.pushButtonCancel.setText(_translate("loginUi", "关闭"))
        self.labelUser.setText(_translate("loginUi", "用户名称"))
        self.labelPassword.setText(_translate("loginUi", "用户密码"))


class loginWindow(QWidget,Ui_loginUi):
    def __init__(self, parent=None):
        super(loginWindow, self).__init__(parent)
        self.setWindowTitle('欢迎使用自动巡检工具')

        self.dbClient = SQLiteOperate()
        #self.cursor = self.dbClient.execSql()
        self.setupUi(self)
        self.center()

        self.pushButtonLogin.clicked.connect(self.mainWindow)
        self.pushButtonCancel.clicked.connect(self.close)

    # 窗口居中主函数.
    def center(self):
        SCREEN = QDesktopWidget().screenGeometry()
        SIZE = self.geometry()
        self.move((SCREEN.width() - SIZE.width()) /2,
                  (SCREEN.height() - SIZE.height()) /2)

    # 初始化用户登录表.
    def createUserTable(self):
        createUser = '''
        create table if not exists user
        (id int primary key,
        username varchar(20),
        password varchar(20));
        '''
        try:
            cursor = self.dbClient.execSql()
            cursor.execute(createUser)
            logging.info('create table user successfully!')
            cursor.close()

        except Exception as e:
            logging.error('create table user failed,{0}'.format(e))

        finally:
            pass

    def mainWindow(self):
        inputUserName = self.lineEditUser.text()              # 获取lineEdit当前的值,即输入的用户名称.
        inputPassWord = self.dbClient.md5Encrypt(self.lineEditPassword.text())        # 获取lineEdit当前的值,并使用MD5加密.

        try:
            self.createUserTable()
            cursor = self.dbClient.execSql()
            password = cursor.execute("select password from user where username='admin'").fetchone()[0]
            if inputUserName == "admin" and inputPassWord == password:
                QMessageBox.about(self,'欢迎登陆',MSG)
                self.close()
            else:
                QMessageBox.warning(self,'错误提示','输入的账号密码错误!',QMessageBox.Cancel)
            cursor.close()

        except Exception as e:
            QMessageBox.warning(self,'错误提示',"数据库读取密码失败,{0}".format(e))

        finally:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = loginWindow()
    win.show()
    sys.exit(app.exec())