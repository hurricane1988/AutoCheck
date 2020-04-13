# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exportFiles.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormExport(object):
    def setupUi(self, FormExport):
        FormExport.setObjectName("FormExport")
        FormExport.resize(399, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormExport.sizePolicy().hasHeightForWidth())
        FormExport.setSizePolicy(sizePolicy)
        FormExport.setMaximumSize(QtCore.QSize(399, 180))
        self.groupBoxExport = QtWidgets.QGroupBox(FormExport)
        self.groupBoxExport.setGeometry(QtCore.QRect(10, 10, 381, 161))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(11)
        self.groupBoxExport.setFont(font)
        self.groupBoxExport.setStyleSheet("border-radius:10px;\n"
"background-color: lightgray;")
        self.groupBoxExport.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxExport.setObjectName("groupBoxExport")
        self.radioButtonSelectServer = QtWidgets.QRadioButton(self.groupBoxExport)
        self.radioButtonSelectServer.setGeometry(QtCore.QRect(20, 50, 121, 16))
        self.radioButtonSelectServer.setObjectName("radioButtonSelectServer")
        self.radioButtonSelectDatabases = QtWidgets.QRadioButton(self.groupBoxExport)
        self.radioButtonSelectDatabases.setGeometry(QtCore.QRect(160, 50, 111, 16))
        self.radioButtonSelectDatabases.setObjectName("radioButtonSelectDatabases")
        self.radioButtonSelectAll = QtWidgets.QRadioButton(self.groupBoxExport)
        self.radioButtonSelectAll.setGeometry(QtCore.QRect(290, 50, 81, 16))
        self.radioButtonSelectAll.setObjectName("radioButtonSelectAll")
        self.pushButtonExport = QtWidgets.QPushButton(self.groupBoxExport)
        self.pushButtonExport.setGeometry(QtCore.QRect(40, 110, 91, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButtonExport.setFont(font)
        self.pushButtonExport.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(85, 170, 255);\n"
"selection-background-color: rgb(255, 85, 0);\n"
"")
        self.pushButtonExport.setObjectName("pushButtonExport")
        self.pushButtonCancel = QtWidgets.QPushButton(self.groupBoxExport)
        self.pushButtonCancel.setGeometry(QtCore.QRect(260, 110, 81, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButtonCancel.setFont(font)
        self.pushButtonCancel.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(85, 170, 255);\n"
"selection-background-color: rgb(170, 0, 0);")
        self.pushButtonCancel.setObjectName("pushButtonCancel")

        self.retranslateUi(FormExport)
        QtCore.QMetaObject.connectSlotsByName(FormExport)

    def retranslateUi(self, FormExport):
        _translate = QtCore.QCoreApplication.translate
        FormExport.setWindowTitle(_translate("FormExport", "导出"))
        self.groupBoxExport.setTitle(_translate("FormExport", "选择导出信息"))
        self.radioButtonSelectServer.setText(_translate("FormExport", "导出服务器系信息"))
        self.radioButtonSelectDatabases.setText(_translate("FormExport", "导出数据库信息"))
        self.radioButtonSelectAll.setText(_translate("FormExport", "导出全部"))
        self.pushButtonExport.setText(_translate("FormExport", "点击导出"))
        self.pushButtonCancel.setText(_translate("FormExport", "点击取消"))

