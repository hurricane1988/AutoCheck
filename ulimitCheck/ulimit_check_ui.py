# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ulimitCheck.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ulimitCheck(object):
    def setupUi(self, ulimitCheck):
        ulimitCheck.setObjectName("ulimitCheck")
        ulimitCheck.resize(586, 240)
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        ulimitCheck.setFont(font)
        self.groupBoxOutside = QtWidgets.QGroupBox(ulimitCheck)
        self.groupBoxOutside.setGeometry(QtCore.QRect(4, 4, 577, 231))
        self.groupBoxOutside.setStyleSheet("border-radius:5px;\n"
"background-color: lightgray;")
        self.groupBoxOutside.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxOutside.setObjectName("groupBoxOutside")
        self.labelCheck = QtWidgets.QLabel(self.groupBoxOutside)
        self.labelCheck.setGeometry(QtCore.QRect(10, 42, 81, 21))
        self.labelCheck.setStyleSheet("border-radius:5px;\n"
"font: 75 11pt \"微软雅黑\";\n"
"background-color: white;")
        self.labelCheck.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCheck.setObjectName("labelCheck")
        self.pushButtonOK = QtWidgets.QPushButton(self.groupBoxOutside)
        self.pushButtonOK.setGeometry(QtCore.QRect(110, 190, 81, 23))
        self.pushButtonOK.setStyleSheet("border-radius:5px;\n"
"font: 75 11pt \"微软雅黑\";\n"
"background-color: gold;\n"
"selection-background-color: rgb(170, 255, 127);")
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.pushButtonCance = QtWidgets.QPushButton(self.groupBoxOutside)
        self.pushButtonCance.setGeometry(QtCore.QRect(430, 190, 75, 23))
        self.pushButtonCance.setStyleSheet("border-radius:5px;\n"
"font: 75 11pt \"微软雅黑\";\n"
"background-color: gold;")
        self.pushButtonCance.setObjectName("pushButtonCance")
        self.groupBoxInside = QtWidgets.QGroupBox(self.groupBoxOutside)
        self.groupBoxInside.setGeometry(QtCore.QRect(100, 40, 421, 121))
        self.groupBoxInside.setStyleSheet("border-radius:5px;\n"
"background-color: white;")
        self.groupBoxInside.setTitle("")
        self.groupBoxInside.setObjectName("groupBoxInside")
        self.checkBoxUlimit = QtWidgets.QCheckBox(self.groupBoxInside)
        self.checkBoxUlimit.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.checkBoxUlimit.setObjectName("checkBoxUlimit")

        self.retranslateUi(ulimitCheck)
        QtCore.QMetaObject.connectSlotsByName(ulimitCheck)

    def retranslateUi(self, ulimitCheck):
        _translate = QtCore.QCoreApplication.translate
        ulimitCheck.setWindowTitle(_translate("ulimitCheck", "系统内核参数检查"))
        self.groupBoxOutside.setTitle(_translate("ulimitCheck", "系统内核参数检查工具"))
        self.labelCheck.setText(_translate("ulimitCheck", "选项检查"))
        self.pushButtonOK.setText(_translate("ulimitCheck", "开始检查"))
        self.pushButtonCance.setText(_translate("ulimitCheck", "点击取消"))
        self.checkBoxUlimit.setText(_translate("ulimitCheck", "ulimit参数"))

