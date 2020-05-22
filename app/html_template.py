# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'html_template.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(809, 417)
        self.tabWidgetBar = QtWidgets.QTabWidget(Form)
        self.tabWidgetBar.setGeometry(QtCore.QRect(10, 10, 791, 401))
        self.tabWidgetBar.setStyleSheet("background-color: lightgray;\n"
"border-radius:5px;")
        self.tabWidgetBar.setObjectName("tabWidgetBar")
        self.tabBar = QtWidgets.QWidget()
        self.tabBar.setObjectName("tabBar")
        self.tabWidgetBar.addTab(self.tabBar, "")
        self.tabLine = QtWidgets.QWidget()
        self.tabLine.setObjectName("tabLine")
        self.tabWidgetBar.addTab(self.tabLine, "")

        self.retranslateUi(Form)
        self.tabWidgetBar.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidgetBar.setTabText(self.tabWidgetBar.indexOf(self.tabBar), _translate("Form", "条形图"))
        self.tabWidgetBar.setTabText(self.tabWidgetBar.indexOf(self.tabLine), _translate("Form", "柱状图"))
