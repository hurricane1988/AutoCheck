# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PortScan.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PortScan(object):
    def setupUi(self, PortScan):
        PortScan.setObjectName("PortScan")
        PortScan.resize(563, 300)
        self.groupBox = QtWidgets.QGroupBox(PortScan)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 541, 281))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("border-radius:5px;\n"
"background-color: lightgray;")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.labelInput = QtWidgets.QLabel(self.groupBox)
        self.labelInput.setGeometry(QtCore.QRect(20, 30, 131, 16))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelInput.setFont(font)
        self.labelInput.setStyleSheet("font: 11pt \"华文中宋\";")
        self.labelInput.setObjectName("labelInput")
        self.lineEditInput = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditInput.setGeometry(QtCore.QRect(150, 30, 271, 20))
        self.lineEditInput.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Courier\";")
        self.lineEditInput.setClearButtonEnabled(True)
        self.lineEditInput.setObjectName("lineEditInput")
        self.pushButtonStart = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonStart.setGeometry(QtCore.QRect(440, 30, 81, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"border-radius:5px;\n"
"font: 75 11pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);")
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.textEditScanResult = QtWidgets.QTextEdit(self.groupBox)
        self.textEditScanResult.setGeometry(QtCore.QRect(20, 110, 501, 161))
        self.textEditScanResult.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.textEditScanResult.setObjectName("textEditScanResult")
        self.labelScanIP = QtWidgets.QLabel(self.groupBox)
        self.labelScanIP.setGeometry(QtCore.QRect(20, 70, 131, 16))
        self.labelScanIP.setStyleSheet("font: 11pt \"华文中宋\";")
        self.labelScanIP.setObjectName("labelScanIP")
        self.lineEditScanIP = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditScanIP.setGeometry(QtCore.QRect(150, 70, 271, 20))
        self.lineEditScanIP.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Courier\";")
        self.lineEditScanIP.setClearButtonEnabled(True)
        self.lineEditScanIP.setObjectName("lineEditScanIP")
        self.pushButtonScanIP = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonScanIP.setGeometry(QtCore.QRect(440, 70, 81, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButtonScanIP.setFont(font)
        self.pushButtonScanIP.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"font: 75 11pt \"微软雅黑\";\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);")
        self.pushButtonScanIP.setObjectName("pushButtonScanIP")

        self.retranslateUi(PortScan)
        QtCore.QMetaObject.connectSlotsByName(PortScan)

    def retranslateUi(self, PortScan):
        _translate = QtCore.QCoreApplication.translate
        PortScan.setWindowTitle(_translate("PortScan", "端口扫描"))
        PortScan.setWindowIcon(QtGui.QIcon('login.ico'))
        self.groupBox.setToolTip(_translate("PortScan", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">格式为:IP/协议/端口</span></p><p><span style=\" font-size:11pt; font-weight:600;\">【Sample】</span></p><p><span style=\" font-size:11pt;\">1. 192.168.10.100/TCP/80 #扫描该IP的TCP协议的80端口</span></p><p><span style=\" font-size:11pt;\">2. 192.168.10.100/UDP/53 #扫描该IP的UDP协议的53端口</span><br/></p></body></html>"))
        self.groupBox.setTitle(_translate("PortScan", "端口扫描"))
        self.labelInput.setText(_translate("PortScan", "输入扫检测址信息:"))
        self.lineEditInput.setPlaceholderText(_translate("PortScan", "请输入待扫描IP地址"))
        self.pushButtonStart.setText(_translate("PortScan", "点击检查"))
        self.textEditScanResult.setPlaceholderText(_translate("PortScan", "结果信息输出"))
        self.labelScanIP.setText(_translate("PortScan", "输入扫描地址信息："))
        self.lineEditScanIP.setPlaceholderText(_translate("PortScan", "请输入IP地址,如192.168.10.100"))
        self.pushButtonScanIP.setText(_translate("PortScan", "点击扫描"))
