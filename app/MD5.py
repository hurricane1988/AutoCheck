# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MD5.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MD5(object):
    def setupUi(self, MD5):
        MD5.setObjectName("MD5")
        MD5.resize(512, 254)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MD5.sizePolicy().hasHeightForWidth())
        MD5.setSizePolicy(sizePolicy)
        self.groupBoxMD5 = QtWidgets.QGroupBox(MD5)
        self.groupBoxMD5.setGeometry(QtCore.QRect(10, 10, 491, 231))
        self.groupBoxMD5.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxMD5.setFont(font)
        self.groupBoxMD5.setStyleSheet("color: rgb(27, 27, 27);\n"
"background-color: lightgray;\n"
"border-radius:5px;")
        self.groupBoxMD5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxMD5.setObjectName("groupBoxMD5")
        self.labelInputString = QtWidgets.QLabel(self.groupBoxMD5)
        self.labelInputString.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.labelInputString.setStyleSheet("font: 11pt \"华文中宋\";")
        self.labelInputString.setObjectName("labelInputString")
        self.lineEditInput = QtWidgets.QLineEdit(self.groupBoxMD5)
        self.lineEditInput.setGeometry(QtCore.QRect(130, 30, 251, 21))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(10)
        self.lineEditInput.setFont(font)
        self.lineEditInput.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditInput.setClearButtonEnabled(True)
        self.lineEditInput.setObjectName("lineEditInput")
        self.pushButtonMD5 = QtWidgets.QPushButton(self.groupBoxMD5)
        self.pushButtonMD5.setGeometry(QtCore.QRect(400, 30, 75, 23))
        self.pushButtonMD5.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 11pt \"微软雅黑\";\n"
"border-radius:5px;")
        self.pushButtonMD5.setObjectName("pushButtonMD5")
        self.layoutWidget = QtWidgets.QWidget(self.groupBoxMD5)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 70, 451, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelString = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(11)
        self.labelString.setFont(font)
        self.labelString.setAlignment(QtCore.Qt.AlignCenter)
        self.labelString.setObjectName("labelString")
        self.gridLayout.addWidget(self.labelString, 0, 0, 1, 1)
        self.lineEditString = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditString.setBaseSize(QtCore.QSize(0, 2))
        self.lineEditString.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditString.setObjectName("lineEditString")
        self.gridLayout.addWidget(self.lineEditString, 0, 1, 1, 1)
        self.label16min = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(10)
        self.label16min.setFont(font)
        self.label16min.setAlignment(QtCore.Qt.AlignCenter)
        self.label16min.setObjectName("label16min")
        self.gridLayout.addWidget(self.label16min, 1, 0, 1, 1)
        self.lineEdit16min = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit16min.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.lineEdit16min.setObjectName("lineEdit16min")
        self.gridLayout.addWidget(self.lineEdit16min, 1, 1, 1, 1)
        self.label16max = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(10)
        self.label16max.setFont(font)
        self.label16max.setObjectName("label16max")
        self.gridLayout.addWidget(self.label16max, 2, 0, 1, 1)
        self.lineEdit16max = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit16max.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit16max.setObjectName("lineEdit16max")
        self.gridLayout.addWidget(self.lineEdit16max, 2, 1, 1, 1)
        self.label32min = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(10)
        self.label32min.setFont(font)
        self.label32min.setObjectName("label32min")
        self.gridLayout.addWidget(self.label32min, 3, 0, 1, 1)
        self.lineEdit32min = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit32min.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.lineEdit32min.setObjectName("lineEdit32min")
        self.gridLayout.addWidget(self.lineEdit32min, 3, 1, 1, 1)
        self.label32max = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(10)
        self.label32max.setFont(font)
        self.label32max.setObjectName("label32max")
        self.gridLayout.addWidget(self.label32max, 4, 0, 1, 1)
        self.lineEdit32max = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit32max.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.lineEdit32max.setObjectName("lineEdit32max")
        self.gridLayout.addWidget(self.lineEdit32max, 4, 1, 1, 1)

        self.retranslateUi(MD5)
        QtCore.QMetaObject.connectSlotsByName(MD5)

    def retranslateUi(self, MD5):
        _translate = QtCore.QCoreApplication.translate
        MD5.setWindowTitle(_translate("MD5", "MD5加密"))
        MD5.setWindowIcon(QtGui.QIcon('login.ico'))
        self.groupBoxMD5.setTitle(_translate("MD5", "MD5加密"))
        self.labelInputString.setText(_translate("MD5", "要加密的字符串:"))
        self.lineEditInput.setPlaceholderText(_translate("MD5", "请出入待加密的字符串！"))
        self.pushButtonMD5.setText(_translate("MD5", "加密"))
        self.labelString.setText(_translate("MD5", "字符串"))
        self.label16min.setText(_translate("MD5", "16位 小写"))
        self.label16max.setText(_translate("MD5", "16位 大写"))
        self.label32min.setText(_translate("MD5", "32位 小写"))
        self.label32max.setText(_translate("MD5", "32位 大写"))
