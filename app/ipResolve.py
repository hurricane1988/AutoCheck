# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ipResolve.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IpResolve(object):
    def setupUi(self, IpResolve):
        IpResolve.setObjectName("IpResolve")
        IpResolve.resize(570, 260)
        self.groupBoxIPResolve = QtWidgets.QGroupBox(IpResolve)
        self.groupBoxIPResolve.setGeometry(QtCore.QRect(10, 20, 551, 231))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(11)
        self.groupBoxIPResolve.setFont(font)
        self.groupBoxIPResolve.setStyleSheet("color: rgb(0, 85, 127);\n"
"border-radius:5px;\n"
"background-color: lightgray;")
        self.groupBoxIPResolve.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxIPResolve.setObjectName("groupBoxIPResolve")
        self.labelInputIP = QtWidgets.QLabel(self.groupBoxIPResolve)
        self.labelInputIP.setGeometry(QtCore.QRect(40, 30, 111, 16))
        self.labelInputIP.setStyleSheet("font: 11pt \"华文中宋\";\n"
"color: rgb(0, 0, 0);")
        self.labelInputIP.setObjectName("labelInputIP")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBoxIPResolve)
        self.lineEdit.setGeometry(QtCore.QRect(160, 30, 231, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"font: 11pt \"Cambria\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButtonResolve = QtWidgets.QPushButton(self.groupBoxIPResolve)
        self.pushButtonResolve.setGeometry(QtCore.QRect(430, 30, 75, 23))
        self.pushButtonResolve.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 11pt \"微软雅黑\";\n"
"selection-color: rgb(85, 170, 255);")
        self.pushButtonResolve.setObjectName("pushButtonResolve")
        self.textEditResolveResult = QtWidgets.QTextEdit(self.groupBoxIPResolve)
        self.textEditResolveResult.setGeometry(QtCore.QRect(40, 70, 471, 131))
        self.textEditResolveResult.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"font: 11pt \"Centaur\";\n"
"color: rgb(0, 0, 0);")
        self.textEditResolveResult.setObjectName("textEditResolveResult")

        self.retranslateUi(IpResolve)
        QtCore.QMetaObject.connectSlotsByName(IpResolve)

    def retranslateUi(self, IpResolve):
        _translate = QtCore.QCoreApplication.translate
        IpResolve.setWindowTitle(_translate("IpResolve", "公网IP地址解析"))
        self.groupBoxIPResolve.setTitle(_translate("IpResolve", "公网IP查询"))
        self.labelInputIP.setText(_translate("IpResolve", "输入公网IP地址:"))
        self.lineEdit.setPlaceholderText(_translate("IpResolve", "如47.92.135.119"))
        self.pushButtonResolve.setText(_translate("IpResolve", "点击解析"))
        self.textEditResolveResult.setPlaceholderText(_translate("IpResolve", "解析结果显示:"))

