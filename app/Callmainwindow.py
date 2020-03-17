#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################
# Create Time: 2020-03-08 下午 08:14
# Author: Hurricane1988
# FileName: Callmainwindow.py
##########################################


import sys,re
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QDesktopWidget,QHeaderView,QTableView
from mainwindow import Ui_MainWindow
from CallMD5 import md5Encrypt
from CallPortScan import portScanWindow
from CallenterInfo import enterWindow
from CallChangePassword import resetPassWord
from Configuration import *


class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        self.setWindowTitle('自助巡检GUI工具')                                        # 设置窗口标题.
        self.setWindowIcon(QIcon('login.ico'))                                      # 设置窗口的图标.
        #self.setFixedSize()

        """窗口显示居中主函数"""
        self.center()

        """调用主窗口函数"""
        self.setupUi(self)

        """关于我们槽与函数绑定"""
        self.actionAbout.triggered.connect(self.about_us)                           # 关于我们动作和about_us函数绑定.

        """MD5窗口的槽与函数绑定"""
        self.actionMD5.triggered.connect(self.md5Encryptshow)                       # MD5动作与MD5加密函数绑定.

        """端口检查槽与函数绑定"""
        self.actionPortCheck.triggered.connect(self.portScanShow)
        #self.actionResetPassWord.triggered.connect(self.resetPassword)             # 密码重置动作和函数绑定.

        """信息录入槽与函数绑定"""
        self.actionAddItem.triggered.connect(self.enterInfo)

        """密码重置槽与函数绑定"""
        self.actionResetPassWord.triggered.connect(self.ResetPasswd)

        """调用资产表格显示函数"""
        self.setTableView()


    # 窗口居中主函数.
    def center(self):
        SCREEN = QDesktopWidget().screenGeometry()
        SIZE = self.geometry()
        self.move((SCREEN.width() - SIZE.width()) / 2, (SCREEN.height() - SIZE.height()) / 2)

    # 设置表格
    def setTableView(self):
        """服务器资产清单Table显示"""
        # 当前页.
        self.currentPage = 0
        # 总页数
        self.totalPage = 0
        # 每页显示记录数.
        self.PageRecordCount = 8
        # 查询模型
        self.queryModel = None
        # 声明查询模型
        self.queryModel = QSqlQueryModel(self)
        # 数据表
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        # 设置数据库名称
        self.db.setDatabaseName('rundb.db')
        # 总记录数
        self.totalRecordCount = 0
        # 总记录标签.
        self.totalRecordLabel = None
        # 打开数据库
        self.db.open()
        # 设置当前页
        self.currentPage = 1
        # 得到总记录数
        self.totalRecrodCount = self.getTotalRecordCount()
        # 得到总页数
        self.totalPage = self.getPageCount()
        # 刷新状态
        self.updateStatus()
        # 设置总页数文本
        self.setTotalPageLabel()
        # 设置总记录数
        self.setTotalRecordLabel()

        # 记录查询
        self.recordQuery(0)
        # 设置模型
        self.tableViewProperty.setModel(self.queryModel)

        #print('totalRecrodCount=' + str(self.totalRecrodCount))
        #print('totalPage=' + str(self.totalPage))

        self.tableViewProperty.horizontalHeader().setStretchLastSection(True)
        self.tableViewProperty.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pushButtonPrevPage.clicked.connect(self.onPrevButtonClick)
        self.pushButtonNextPage.clicked.connect(self.onNextButtonClick)
        self.pushButtonGO.clicked.connect(self.onSwitchPageButtonClick)

        # 设置表格表头
        self.queryModel.setHeaderData(0, Qt.Horizontal, "编号")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "IP地址")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "系统版本")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "登录账号")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "登录密码")
        self.queryModel.setHeaderData(5, Qt.Horizontal, "用途描述")
        self.queryModel.setHeaderData(6, Qt.Horizontal, "系统类型")

    # 得到记录数
    def getTotalRecordCount(self):
        self.queryModel.setQuery("select * from t_server")
        rowCount = self.queryModel.rowCount()
        #print('rowCount=' + str(rowCount))
        return rowCount

    # 得到页数
    def getPageCount(self):
        if self.totalRecrodCount % self.PageRecordCount == 0:
            return (self.totalRecrodCount / self.PageRecordCount)
        else:
            return (self.totalRecrodCount / self.PageRecordCount + 1)

    # 记录查询
    def recordQuery(self, limitIndex):
        Query = ("select * from t_server limit %d,%d" % (limitIndex, self.PageRecordCount))
        self.queryModel.setQuery(Query)
        #print('query sql=' + Query)

    # 刷新状态
    def updateStatus(self):
        szCurrentText = ("当前第%d页" % self.currentPage)
        self.labelCurrentPage.setText(szCurrentText)

        # 设置按钮是否可用
        if self.currentPage == 1:
            self.pushButtonPrevPage.setEnabled(False)
            self.pushButtonNextPage.setEnabled(True)
        elif self.currentPage == self.totalPage:
            self.pushButtonPrevPage.setEnabled(True)
            self.pushButtonNextPage.setEnabled(False)
        else:
            self.pushButtonPrevPage.setEnabled(True)
            self.pushButtonNextPage.setEnabled(True)

    # 设置总数页文本
    def setTotalPageLabel(self):
        PageCountText = ("总共%d页" % self.totalPage)
        self.labelTotalPages.setText(PageCountText)

    # 设置总记录数
    def setTotalRecordLabel(self):
        TotalRecordText = ("共%d条" % self.totalRecrodCount)
        #print('*** setTotalRecordLabel szTotalRecordText=' + TotalRecordText)
        self.labelTotalItems.setText(TotalRecordText)

    # 前一页按钮按下
    def onPrevButtonClick(self):
        #print('*** onPrevButtonClick ')
        limitIndex = (self.currentPage - 2) * self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage -= 1
        self.updateStatus()

    # 后一页按钮按下
    def onNextButtonClick(self):
        #print('*** onNextButtonClick ')
        limitIndex = self.currentPage * self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage += 1
        self.updateStatus()

    # 转到页按钮按下
    def onSwitchPageButtonClick(self):
        # 得到输入字符串
        szText = self.lineEditPageNumber.text()
        # 数字正则表达式
        #pattern = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
        pattern = re.compile(r'^[0-9]+\.[0-9]+$')
        match = pattern.match(szText)

        # 判断是否为数字
        if not match:
            QMessageBox.information(self, "提示", "请输入数字")
            return

        # 是否为空
        if szText == '':
            QMessageBox.information(self, "提示", "请输入跳转页面")
            return

        # 得到页数
        pageIndex = int(szText)
        # 判断是否有指定页
        if pageIndex > self.totalPage or pageIndex < 1:
            QMessageBox.information(self, "提示", "没有指定的页面，请重新输入")
            return

        # 得到查询起始行号
        limitIndex = (pageIndex - 1) * self.PageRecordCount

        # 记录查询
        self.recordQuery(limitIndex)
        # 设置当前页
        self.currentPage = pageIndex
        # 刷新状态
        self.updateStatus()

    # 关于我们帮助文档说明.
    def about_us(self):
        QMessageBox.about(self,'关于我们',MSG)

    # 密码重置函数.
    def md5Encryptshow(self):
        self.MD5 = md5Encrypt()
        self.MD5.show()

    # 端口扫描主函数.
    def portScanShow(self):
        self.portscan = portScanWindow()
        self.portscan.show()

    # 信息录入主函数.
    def enterInfo(self):
        self.inputInfo = enterWindow()
        self.inputInfo.show()

    # 密码重置主函数.
    def ResetPasswd(self):
        self.resetpassword = resetPassWord()
        self.resetpassword.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec())
