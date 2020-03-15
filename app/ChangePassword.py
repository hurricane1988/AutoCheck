# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChangePassword.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangePassWord(object):
    def setupUi(self, ChangePassWord):
        ChangePassWord.setObjectName("ChangePassWord")
        ChangePassWord.resize(320, 179)
        ChangePassWord.setMinimumSize(QtCore.QSize(250, 150))
        self.groupBox = QtWidgets.QGroupBox(ChangePassWord)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 301, 161))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(182, 179, 176);\n"
"border-radius:10px;")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.pushButtonOK = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonOK.setGeometry(QtCore.QRect(40, 120, 75, 25))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonOK.setFont(font)
        self.pushButtonOK.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"border-radius:5px;")
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.pushButtonCancel = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonCancel.setGeometry(QtCore.QRect(190, 120, 75, 25))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCancel.setFont(font)
        self.pushButtonCancel.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"border-radius:5px;")
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(31, 31, 240, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelPassWord = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelPassWord.setFont(font)
        self.labelPassWord.setObjectName("labelPassWord")
        self.horizontalLayout.addWidget(self.labelPassWord)
        self.lineEditPassWord = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditPassWord.setMinimumSize(QtCore.QSize(0, 3))
        self.lineEditPassWord.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.lineEditPassWord.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassWord.setObjectName("lineEditPassWord")
        self.horizontalLayout.addWidget(self.lineEditPassWord)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(31, 71, 240, 26))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelPassWordCheck = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelPassWordCheck.setFont(font)
        self.labelPassWordCheck.setObjectName("labelPassWordCheck")
        self.horizontalLayout_2.addWidget(self.labelPassWordCheck)
        self.lineEditPassWordCheck = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEditPassWordCheck.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.lineEditPassWordCheck.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassWordCheck.setObjectName("lineEditPassWordCheck")
        self.horizontalLayout_2.addWidget(self.lineEditPassWordCheck)

        self.retranslateUi(ChangePassWord)
        QtCore.QMetaObject.connectSlotsByName(ChangePassWord)

    def retranslateUi(self, ChangePassWord):
        _translate = QtCore.QCoreApplication.translate
        ChangePassWord.setWindowTitle(_translate("ChangePassWord", "密码修改"))
        ChangePassWord.setWindowIcon(QtGui.QIcon('login.ico'))
        self.groupBox.setTitle(_translate("ChangePassWord", "密码修改"))
        self.pushButtonOK.setText(_translate("ChangePassWord", "确认修改"))
        self.pushButtonCancel.setText(_translate("ChangePassWord", "取消修改"))
        self.labelPassWord.setText(_translate("ChangePassWord", "输入新密码"))
        self.lineEditPassWord.setPlaceholderText(_translate("ChangePassWord", "输入新密码"))
        self.labelPassWordCheck.setText(_translate("ChangePassWord", "新密码确认"))
        self.lineEditPassWordCheck.setPlaceholderText(_translate("ChangePassWord", "再次确认密码"))
