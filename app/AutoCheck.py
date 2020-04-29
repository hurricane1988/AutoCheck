# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutoCheck.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UIAutoCheck(object):
    def setupUi(self, UIAutoCheck):
        UIAutoCheck.setObjectName("UIAutoCheck")
        UIAutoCheck.resize(330, 169)
        self.groupBoxAutoCheck = QtWidgets.QGroupBox(UIAutoCheck)
        self.groupBoxAutoCheck.setGeometry(QtCore.QRect(4, 4, 321, 161))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.groupBoxAutoCheck.setFont(font)
        self.groupBoxAutoCheck.setStyleSheet("border-radius:5px;\n"
"background-color:lightgray;")
        self.groupBoxAutoCheck.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxAutoCheck.setObjectName("groupBoxAutoCheck")
        self.checkBoxServer = QtWidgets.QCheckBox(self.groupBoxAutoCheck)
        self.checkBoxServer.setGeometry(QtCore.QRect(30, 70, 121, 16))
        self.checkBoxServer.setStyleSheet("border-radius:5px;\n"
"font: 10pt \"华文中宋\";\n"
"selection-background-color: rgb(0, 255, 127);")
        self.checkBoxServer.setObjectName("checkBoxServer")
        self.checkBoxDatabase = QtWidgets.QCheckBox(self.groupBoxAutoCheck)
        self.checkBoxDatabase.setGeometry(QtCore.QRect(210, 70, 91, 16))
        self.checkBoxDatabase.setStyleSheet("border-radius:5px;\n"
"font: 10pt \"华文中宋\";\n"
"selection-background-color: rgb(0, 255, 127);")
        self.checkBoxDatabase.setObjectName("checkBoxDatabase")
        self.progressBar = QtWidgets.QProgressBar(self.groupBoxAutoCheck)
        self.progressBar.setGeometry(QtCore.QRect(30, 30, 281, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.progressBar.setObjectName("progressBar")
        self.pushButtonScan = QtWidgets.QPushButton(self.groupBoxAutoCheck)
        self.pushButtonScan.setGeometry(QtCore.QRect(30, 120, 90, 23))
        self.pushButtonScan.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(85, 170, 255);\n"
"font: 11pt \"微软雅黑\";")
        self.pushButtonScan.setObjectName("pushButtonScan")
        self.pushButtonCance = QtWidgets.QPushButton(self.groupBoxAutoCheck)
        self.pushButtonCance.setGeometry(QtCore.QRect(200, 120, 90, 23))
        self.pushButtonCance.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(85, 170, 255);\n"
"font: 11pt \"微软雅黑\";")
        self.pushButtonCance.setObjectName("pushButtonCance")

        self.retranslateUi(UIAutoCheck)
        QtCore.QMetaObject.connectSlotsByName(UIAutoCheck)

    def retranslateUi(self, UIAutoCheck):
        _translate = QtCore.QCoreApplication.translate
        UIAutoCheck.setWindowTitle(_translate("UIAutoCheck", "系统自动巡检"))
        self.groupBoxAutoCheck.setTitle(_translate("UIAutoCheck", "系统自动巡检"))
        self.checkBoxServer.setText(_translate("UIAutoCheck", "操作系统巡检"))
        self.checkBoxDatabase.setText(_translate("UIAutoCheck", "数据库巡检"))
        self.pushButtonScan.setText(_translate("UIAutoCheck", "点击开始"))
        self.pushButtonCance.setText(_translate("UIAutoCheck", "点击取消"))

