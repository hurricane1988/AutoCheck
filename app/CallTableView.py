#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
from PyQt5.QtSql import QSqlQueryModel,QSqlDatabase
from PyQt5.QtWidgets import QMessageBox,QHeaderView,QWidget
from PyQt5.QtCore import QThread,Qt
from mainwindow import Ui_MainWindow
from Configuration import database,query,queryModel
from CallenterInfo import enterWindow

# 定义表格主类.
class propertyTableView(QThread,QWidget,Ui_MainWindow):
    def __init__(self, parent=None):
        super(propertyTableView, self).__init__(parent)


        self.currentPage = 0
        self.totalPage = 0
        self.PageRecordCount = 8
        self.totalRecordCount = 0
        self.totalRecordLabel = None
        self.currentPage = 1


    # 设置服务器表格表格
    def setServerTableView(self):
        # 当前页.
        currentPage = 0
        # 总页数
        totalPage = 0
        # 每页显示记录数.
        PageRecordCount = 8
        # 查询模型
        #self.queryModel = None
        # 声明查询模型
        #self.queryModel = QSqlQueryModel(self)
        # 数据表
        #self.db = QSqlDatabase.addDatabase('QSQLITE')
        # 设置数据库名称
        #self.db.setDatabaseName('rundb.db')
        # 总记录数
        totalRecordCount = 0
        # 总记录标签.
        totalRecordLabel = None
        # 打开数据库
        #self.db.open()
        # 设置当前页
        currentPage = 1
        # 得到总记录数
        totalRecrodCount = self.getTotalRecordCount()
        # 得到总页数
        totalPage = self.getPageCount()
        # 刷新状态
        self.updateStatus()
        # 设置总页数文本
        self.setTotalPageLabel()
        # 设置总记录数
        self.setTotalRecordLabel()

        # 记录查询
        self.recordQuery(0)
        # 设置模型
        self.tableViewServersProperty.setModel(queryModel)

        # print('totalRecrodCount=' + str(self.totalRecrodCount))
        # print('totalPage=' + str(self.totalPage))

        self.tableViewServersProperty.horizontalHeader().setStretchLastSection(True)
        self.tableViewServersProperty.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pushButtonServerPrevPage.clicked.connect(self.onPrevButtonClick)
        self.pushButtonServerNextPage.clicked.connect(self.onNextButtonClick)
        self.pushButtonGO.clicked.connect(self.onSwitchPageButtonClick)

        # 设置表格表头
        queryModel.setHeaderData(0, Qt.Horizontal, "编号")
        queryModel.setHeaderData(1, Qt.Horizontal, "IP地址")
        queryModel.setHeaderData(2, Qt.Horizontal, "系统版本")
        queryModel.setHeaderData(3, Qt.Horizontal, "登录账号")
        queryModel.setHeaderData(4, Qt.Horizontal, "登录密码")
        queryModel.setHeaderData(5, Qt.Horizontal, "用途描述")
        queryModel.setHeaderData(6, Qt.Horizontal, "系统类型")

    # 得到记录数
    def getTotalRecordCount(self):
        queryModel.setQuery("select * from t_server")
        rowCount = queryModel.rowCount()
        # print('rowCount=' + str(rowCount))
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
        queryModel.setQuery(Query)

    # 刷新状态
    def updateStatus(self):
        szCurrentText = ("当前第%d页" % self.currentPage)
        self.labelServerCurrentPage.setText(szCurrentText)

        # 设置按钮是否可用
        if self.currentPage == 1:
            self.pushButtonServerPrevPage.setEnabled(False)
            self.pushButtonServerNextPage.setEnabled(True)
        elif self.currentPage == self.totalPage:
            self.pushButtonServerPrevPage.setEnabled(True)
            self.pushButtonServerNextPage.setEnabled(False)
        else:
            self.pushButtonServerPrevPage.setEnabled(True)
            self.pushButtonServerNextPage.setEnabled(True)

    # 设置总数页文本
    def setTotalPageLabel(self):
        PageCountText = ("总共%d页" % self.totalPage)
        self.labelServerTotalPages.setText(PageCountText)

    # 设置总记录数
    def setTotalRecordLabel(self):
        TotalRecordText = ("共%d条" % self.totalRecrodCount)
        # print('*** setTotalRecordLabel szTotalRecordText=' + TotalRecordText)
        self.labelServerTotalItems.setText(TotalRecordText)

    # 前一页按钮按下
    def onPrevButtonClick(self):
        # print('*** onPrevButtonClick ')
        limitIndex = (self.currentPage - 2) * self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage -= 1
        self.updateStatus()

    # 后一页按钮按下
    def onNextButtonClick(self):
        # print('*** onNextButtonClick ')
        limitIndex = self.currentPage * self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage += 1
        self.updateStatus()

    # 转到页按钮按下
    def onSwitchPageButtonClick(self):
        # 得到输入字符串
        szText = self.lineEditPageNumber.text()
        # 数字正则表达式
        # pattern = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
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

    # 定义数据库信息表显示主函数.
    def setDBTableView(self):
        """服务器资产清单Table显示"""
        # 当前页.
        self.currentPage = 0
        # 总页数
        self.totalPage = 0
        # 每页显示记录数.
        self.PageRecordCount = 8
        # 查询模型
        # self.queryModel = None
        # 声明查询模型
        # self.queryModel = QSqlQueryModel(self)
        # 数据表
        # self.db = QSqlDatabase.addDatabase('QSQLITE')
        # 设置数据库名称
        # self.db.setDatabaseName('rundb.db')
        # 总记录数
        self.totalRecordCount = 0
        # 总记录标签.
        self.totalRecordLabel = None
        # 打开数据库
        # self.db.open()
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
        self.tableViewDBProperty.setModel(queryModel)
        self.tableViewDBProperty.horizontalHeader().setStretchLastSection(True)
        self.tableViewDBProperty.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pushButtonDBPrevPage.clicked.connect(self.onPrevButtonClick)
        self.pushButtonDBNextPage.clicked.connect(self.onNextButtonClick)
        self.pushButtonDBGO.clicked.connect(self.onSwitchPageButtonClick)

        # 设置表格表头
        queryModel.setHeaderData(0, Qt.Horizontal, "编号")
        queryModel.setHeaderData(1, Qt.Horizontal, "IP地址")
        queryModel.setHeaderData(2, Qt.Horizontal, "数据库类型")
        queryModel.setHeaderData(3, Qt.Horizontal, "数据库版本")
        queryModel.setHeaderData(4, Qt.Horizontal, "数据库库名")
        queryModel.setHeaderData(5, Qt.Horizontal, "数据库用户")
        queryModel.setHeaderData(6, Qt.Horizontal, "数据库密码")
        queryModel.setHeaderData(7, Qt.Horizontal, "数据库用途")

    # 得到记录数
    def getDBTotalRecordCount(self):
        queryModel.setQuery("select * from t_database")
        rowCount = queryModel.rowCount()
        # print('rowCount=' + str(rowCount))
        return rowCount

    # 得到页数
    def getDBPageCount(self):
        if self.totalRecrodCount % self.PageRecordCount == 0:
            return (self.totalRecrodCount / self.PageRecordCount)
        else:
            return (self.totalRecrodCount / self.PageRecordCount + 1)

    # 记录查询
    def recordDBQuery(self, limitIndex):
        Query = ("select * from t_database limit %d,%d" % (limitIndex, self.PageRecordCount))
        queryModel.setQuery(Query)

    # 刷新状态
    def updateDBStatus(self):
        szCurrentText = ("当前第%d页" % self.currentPage)
        self.labelDBCurrentPage.setText(szCurrentText)

        # 设置按钮是否可用
        if self.currentPage == 1:
            self.pushButtonDBPrevPage.setEnabled(False)
            self.pushButtonDBNextPage.setEnabled(True)
        elif self.currentPage == self.totalPage:
            self.pushButtonDBPrevPage.setEnabled(True)
            self.pushButtonDBNextPage.setEnabled(False)
        else:
            self.pushButtonDBPrevPage.setEnabled(True)
            self.pushButtonDBNextPage.setEnabled(True)

    # 设置总数页文本
    def setDBTotalPageLabel(self):
        PageCountText = ("总共%d页" % self.totalPage)
        self.labelDBTotalPages.setText(PageCountText)

    # 设置总记录数
    def setDBTotalRecordLabel(self):
        TotalRecordText = ("共%d条" % self.totalRecrodCount)
        # print('*** setTotalRecordLabel szTotalRecordText=' + TotalRecordText)
        self.labelServerTotalItems.setText(TotalRecordText)

    # 前一页按钮按下
    def onDBPrevButtonClick(self):
        # print('*** onPrevButtonClick ')
        limitIndex = (self.currentPage - 2) * self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage -= 1
        self.updateStatus()

    # 后一页按钮按下
    def onNextDBButtonClick(self):
        # print('*** onNextButtonClick ')
        limitIndex = self.currentPage * self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage += 1
        self.updateStatus()

    # 转到页按钮按下
    def onDBSwitchPageButtonClick(self):
        # 得到输入字符串
        szText = self.lineEditDBPageNumber.text()
        # 数字正则表达式
        # pattern = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
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

