# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DNSResolute.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormDNS(object):
    def setupUi(self, FormDNS):
        FormDNS.setObjectName("FormDNS")
        FormDNS.resize(429, 158)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormDNS.sizePolicy().hasHeightForWidth())
        FormDNS.setSizePolicy(sizePolicy)
        self.groupBoxDNS = QtWidgets.QGroupBox(FormDNS)
        self.groupBoxDNS.setGeometry(QtCore.QRect(10, 10, 411, 141))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.groupBoxDNS.setFont(font)
        self.groupBoxDNS.setStyleSheet("border-radius:5px;\n"
"background-color: lightgray;")
        self.groupBoxDNS.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxDNS.setObjectName("groupBoxDNS")
        self.labelDNS = QtWidgets.QLabel(self.groupBoxDNS)
        self.labelDNS.setGeometry(QtCore.QRect(20, 30, 61, 19))
        self.labelDNS.setStyleSheet("font: 10pt \"华文中宋\";")
        self.labelDNS.setObjectName("labelDNS")
        self.lineEditDNS = QtWidgets.QLineEdit(self.groupBoxDNS)
        self.lineEditDNS.setGeometry(QtCore.QRect(80, 30, 221, 21))
        self.lineEditDNS.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditDNS.setClearButtonEnabled(True)
        self.lineEditDNS.setObjectName("lineEditDNS")
        self.textEditDNS = QtWidgets.QTextEdit(self.groupBoxDNS)
        self.textEditDNS.setGeometry(QtCore.QRect(20, 60, 371, 71))
        self.textEditDNS.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(255, 255, 255);")
        self.textEditDNS.setObjectName("textEditDNS")
        self.pushButtonDNS = QtWidgets.QPushButton(self.groupBoxDNS)
        self.pushButtonDNS.setGeometry(QtCore.QRect(310, 30, 79, 23))
        self.pushButtonDNS.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(0, 170, 255);\n"
"font: 75 10pt \"微软雅黑\";")
        self.pushButtonDNS.setObjectName("pushButtonDNS")

        self.retranslateUi(FormDNS)
        QtCore.QMetaObject.connectSlotsByName(FormDNS)

    def retranslateUi(self, FormDNS):
        _translate = QtCore.QCoreApplication.translate
        FormDNS.setWindowTitle(_translate("FormDNS", "域名解析"))
        self.groupBoxDNS.setTitle(_translate("FormDNS", "DNS域名解析"))
        self.labelDNS.setText(_translate("FormDNS", "域名输入"))
        self.lineEditDNS.setPlaceholderText(_translate("FormDNS", "请输入待解析域名"))
        self.textEditDNS.setPlaceholderText(_translate("FormDNS", "域名解析结果:"))
        self.pushButtonDNS.setText(_translate("FormDNS", "点击解析"))

