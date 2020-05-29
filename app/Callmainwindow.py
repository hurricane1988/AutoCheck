#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################
# Create Time: 2020-03-08 下午 08:14
# Author: Hurricane1988
# FileName: Callmainwindow.py
##########################################


import sys,re
import base64
from PyQt5.QtCore import Qt,QUrl
from PyQt5 import QtGui
from images.image import logo
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QDesktopWidget,QHeaderView,QTableView
from mainwindow import Ui_MainWindow
from CallMD5 import md5encrypt
from CallPortScan import portScanWindow
from CallenterInfo import enterWindow
from CallChangePassword import resetPassWord
from CallIpResolve import ipResolveWindow
from CallExportInfo import exportInfoWindows
from CallDNSResolute import MyWindowsDNS
from graph_generate import mainpip
# from CallTableView import propertyTableView
from Configuration import database,query,MSG,queryModelDB,queryModelServer


# 主窗口调用主类.
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        self.setWindowTitle('自助巡检GUI工具')
        icon = QtGui.QIcon()
        logo_image = base64.b16decode(logo)
        Pixmap = QtGui.QPixmap()
        Pixmap.loadFromData(logo_image)
        icon.addPixmap(Pixmap, QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        #self.setFixedSize()
        # 窗口显示居中主函数
        self._center()
        # 调用主窗口函数
        self.setupUi(self)
        # 关于我们槽与函数绑定
        self.actionAbout.triggered.connect(self._about_us)
        # MD5窗口的槽与函数绑定
        self.actionMD5.triggered.connect(self._md5Encryptshow)

        # 端口检查槽与函数绑定
        self.actionPortCheck.triggered.connect(self._portScanShow)
        #self.actionResetPassWord.triggered.connect(self.resetPassword)
        # 信息录入槽与函数绑定
        self.actionAddItem.triggered.connect(self._enterInfo)
        # 密码重置槽与函数绑定
        self.actionResetPassWord.triggered.connect(self._ResetPasswd)
        # 公网IP地址解析.
        self.actionPublicIP.triggered.connect(self._ipResolve)
        # 主窗口关闭选项.
        self.actionCancel.triggered.connect(self.close)
        # 域名解析窗口.
        self.actionDNS.triggered.connect(self._ShowDNS)
        # 主窗口文件导出槽与函数绑定.
        self.actionExport.triggered.connect(self._exportInfo)
        # 调用生产饼图函数.
        mainpip()
        # 调用服务器资产表格显示函数.
        self._setServerTableView()
        # 调用数据库资产表格显示函数.
        self._setDBTableView()
        # 调用图表显示函数.
        self._showgraph()

    # 窗口居中主函数.
    def _center(self):
        SCREEN = QDesktopWidget().screenGeometry()
        SIZE = self.geometry()
        self.move((SCREEN.width() - SIZE.width()) / 2, (SCREEN.height() - SIZE.height()) / 2)

    # 设置服务器表格表格
    def _setServerTableView(self):
        # 服务器资产清单Table显示
        # 总页数
        self.ServerTotalPage = 0
        # 每页显示记录数.
        self.ServerPageRecordCount = 8
        # 总记录数
        self.ServerTotalRecordCount = 0
        # 总记录标签.
        self.ServerTotalRecordLabel = None
        # 设置当前页
        self.ServerCurrentPage = 1
        # 得到总记录数
        self.ServerTotalRecrodCount = self._ServergetTotalRecordCount()
        # 得到总页数
        self.ServerTotalPage = self._getPageCount()
        # 刷新状态
        self._ServerupdateStatus()
        # 设置总页数文本
        self._ServersetTotalPageLabel()
        # 设置总记录数
        self._ServersetTotalRecordLabel()
        # 申明服务器查询模型.
        #self.queryModelServer = None
        #self.queryModelServer = QSqlQueryModel(self)
        # 记录查询
        self._recordQueryServer(0)
        # 设置模型
        self.tableViewServersProperty.setModel(queryModelServer)
        self.tableViewServersProperty.horizontalHeader().setStretchLastSection(True)
        self.tableViewServersProperty.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pushButtonServerPrevPage.clicked.connect(self._ServeronPrevButtonClick)
        self.pushButtonServerNextPage.clicked.connect(self._ServeronNextButtonClick)
        self.pushButtonGO.clicked.connect(self._ServeronSwitchPageButtonClick)

        # 设置表格表头
        queryModelServer.setHeaderData(0, Qt.Horizontal, "编号")
        queryModelServer.setHeaderData(1, Qt.Horizontal, "IP地址")
        queryModelServer.setHeaderData(2, Qt.Horizontal, "系统版本")
        queryModelServer.setHeaderData(3, Qt.Horizontal, "登录账号")
        queryModelServer.setHeaderData(4, Qt.Horizontal, "登录密码")
        queryModelServer.setHeaderData(5, Qt.Horizontal, "用途描述")
        queryModelServer.setHeaderData(6, Qt.Horizontal, "系统类型")

    # 得到记录数
    def _ServergetTotalRecordCount(self):
        queryModelServer.setQuery("select * from t_server")
        rowCount = queryModelServer.rowCount()
        return rowCount

    # 得到页数
    def _getPageCount(self):
        if self.ServerTotalRecrodCount % self.ServerPageRecordCount == 0:
            return (self.ServerTotalRecrodCount / self.ServerPageRecordCount)
        else:
            return (self.ServerTotalRecrodCount / self.ServerPageRecordCount + 1)

    # 记录查询
    def _recordQueryServer(self, limitIndex):
        SQLString = ("select * from t_server limit %d,%d" % (limitIndex, self.ServerPageRecordCount))
        queryModelServer.setQuery(SQLString)

    # 刷新状态
    def _ServerupdateStatus(self):
        szCurrentText = ("当前第%d页" % self.ServerCurrentPage)
        self.labelServerCurrentPage.setText(szCurrentText)

        # 设置按钮是否可用
        if self.ServerCurrentPage == 1:
            self.pushButtonServerPrevPage.setEnabled(False)
            self.pushButtonServerNextPage.setEnabled(True)
        elif self.ServerCurrentPage == self.ServerTotalPage:
            self.pushButtonServerPrevPage.setEnabled(True)
            self.pushButtonServerNextPage.setEnabled(False)
        else:
            self.pushButtonServerPrevPage.setEnabled(True)
            self.pushButtonServerNextPage.setEnabled(True)

    # 设置总数页文本
    def _ServersetTotalPageLabel(self):
        PageCountText = ("总共%d页" % self.ServerTotalPage)
        self.labelServerTotalPages.setText(PageCountText)

    # 设置总记录数
    def _ServersetTotalRecordLabel(self):
        TotalRecordText = ("共%d条" % self.ServerTotalRecrodCount)
        self.labelServerTotalItems.setText(TotalRecordText)

    # 前一页按钮按下
    def _ServeronPrevButtonClick(self):
        limitIndex = (self.ServerCurrentPage - 2) * self.ServerPageRecordCount
        self._recordQueryServer(limitIndex)
        self.ServerCurrentPage -= 1
        self._ServerupdateStatus()

    # 后一页按钮按下
    def _ServeronNextButtonClick(self):
        limitIndex = self.ServerCurrentPage * self.ServerPageRecordCount
        self._recordQueryServer(limitIndex)
        self.ServerCurrentPage += 1
        self._ServerupdateStatus()

    # 转到页按钮按下
    def _ServeronSwitchPageButtonClick(self):
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
        if pageIndex > self.ServerTotalPage or pageIndex < 1:
            QMessageBox.information(self, "提示", "没有指定的页面，请重新输入")
            return

        # 得到查询起始行号
        limitIndex = (pageIndex - 1) * self.ServerPageRecordCount

        # 记录查询
        self._recordQueryServer(limitIndex)
        # 设置当前页
        self.ServercurrentPage = pageIndex
        # 刷新状态
        self._ServerupdateStatus()
###############################################################
# 描述: 数据库表格视图函数                                       #
###############################################################
    def _setDBTableView(self):
        # 当前页.
        self.dbcurrentPage = 0
        # 总页数
        self.dbtotalPage = 0
        # 每页显示记录数.
        self.dbPageRecordCount = 8
        # 总记录数
        self.dbtotalRecordCount = 0
        # 总记录标签.
        self.dbtotalRecordLabel = None
        # 设置当前页
        self.dbcurrentPage = 1
        # 得到总记录数
        self.dbtotalRecrodCount = self._dbgetTotalRecordCount()
        # 得到总页数
        self.dbtotalPage = self._dbgetPageCount()
        # 刷新状态
        self._dbupdateStatus()
        # 设置总页数文本
        self._dbsetTotalPageLabel()
        # 设置总记录数
        self._dbsetTotalRecordLabel()
        # 记录查询
        self._dbrecordQuery(0)
        # 设置模型
        self.tableViewDBProperty.setModel(queryModelDB)
        self.tableViewDBProperty.horizontalHeader().setStretchLastSection(True)
        self.tableViewDBProperty.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pushButtonDBPrevPage.clicked.connect(self._dbonPrevButtonClick)
        self.pushButtonDBNextPage.clicked.connect(self._dbonNextButtonClick)
        self.pushButtonDBGO.clicked.connect(self._dbonSwitchPageButtonClick)

        # 设置表格表头
        queryModelDB.setHeaderData(0, Qt.Horizontal, "编号")
        queryModelDB.setHeaderData(1, Qt.Horizontal, "IP地址")
        queryModelDB.setHeaderData(2, Qt.Horizontal, "数据库类型")
        queryModelDB.setHeaderData(3, Qt.Horizontal, "数据库版本")
        queryModelDB.setHeaderData(4, Qt.Horizontal, "数据库名称")
        queryModelDB.setHeaderData(5, Qt.Horizontal, "数据库账号")
        queryModelDB.setHeaderData(6, Qt.Horizontal, "数据库密码")
        queryModelDB.setHeaderData(7, Qt.Horizontal, "数据库用途")

    # 得到记录数
    def _dbgetTotalRecordCount(self):
        queryModelDB.setQuery("select * from t_database")
        rowCount = queryModelDB.rowCount()
        return rowCount

    # 得到页数
    def _dbgetPageCount(self):
        if self.dbtotalRecrodCount % self.dbPageRecordCount == 0:
            return (self.dbtotalRecrodCount / self.dbPageRecordCount)
        else:
            return (self.dbtotalRecrodCount / self.dbPageRecordCount + 1)

    # 记录查询
    def _dbrecordQuery(self, limitIndex):
        Query = ("select * from t_database limit %d,%d" % (limitIndex, self.dbPageRecordCount))
        queryModelDB.setQuery(Query)

    # 刷新状态
    def _dbupdateStatus(self):
        szCurrentText = ("当前第%d页" % self.dbcurrentPage)
        self.labelDBCurrentPage.setText(szCurrentText)

        # 设置按钮是否可用
        if self.dbcurrentPage == 1:
            self.pushButtonDBPrevPage.setEnabled(False)
            self.pushButtonDBNextPage.setEnabled(True)
        elif self.dbcurrentPage == self.dbtotalPage:
            self.pushButtonDBPrevPage.setEnabled(True)
            self.pushButtonDBNextPage.setEnabled(False)
        else:
            self.pushButtonDBPrevPage.setEnabled(True)
            self.pushButtonDBNextPage.setEnabled(True)

    # 设置总数页文本
    def _dbsetTotalPageLabel(self):
        PageCountText = ("总共%d页" % self.dbtotalPage)
        self.labelDBTotalPages.setText(PageCountText)

    # 设置总记录数
    def _dbsetTotalRecordLabel(self):
        TotalRecordText = ("共%d条" % self.dbtotalRecrodCount)
        #print('*** setTotalRecordLabel szTotalRecordText=' + TotalRecordText)
        self.labelDBTotalItems.setText(TotalRecordText)

    # 前一页按钮按下
    def _dbonPrevButtonClick(self):
        limitIndex = (self.dbcurrentPage - 2) * self.dbPageRecordCount
        self._dbrecordQuery(limitIndex)
        self.dbcurrentPage -= 1
        self._dbupdateStatus()

    # 后一页按钮按下
    def _dbonNextButtonClick(self):
        #print('*** onNextButtonClick ')
        limitIndex = self.dbcurrentPage * self.dbPageRecordCount
        self._dbrecordQuery(limitIndex)
        self.dbcurrentPage += 1
        self._dbupdateStatus()

    # 转到页按钮按下
    def _dbonSwitchPageButtonClick(self):
        # 得到输入字符串
        szText = self.lineEditDBPageNumber.text()
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
        if pageIndex > self.dbtotalPage or pageIndex < 1:
            QMessageBox.information(self, "提示", "没有指定的页面，请重新输入")
            return

        # 得到查询起始行号
        limitIndex = (pageIndex - 1) * self.dbPageRecordCount

        # 记录查询
        self._dbrecordQuery(limitIndex)
        # 设置当前页
        self.dbcurrentPage = pageIndex
        # 刷新状态
        self._dbupdateStatus()

    # 关于我们帮助文档说明.
    def _about_us(self):
        QMessageBox.about(self,'关于我们',MSG)

    # 密码重置函数.
    def _md5Encryptshow(self):
        self.MD5 = md5encrypt()
        self.MD5.show()

    # 端口扫描主函数.
    def _portScanShow(self):
        self.portscan = portScanWindow()
        self.portscan.show()

    # 公网IP地址解析.
    def _ipResolve(self):
        self.publicIP = ipResolveWindow()
        self.publicIP.show()

    # 信息录入主函数.
    def _enterInfo(self):
        self.inputInfo = enterWindow()
        self.inputInfo.show()

    # 密码重置主函数.
    def _ResetPasswd(self):
        self.resetpassword = resetPassWord()
        self.resetpassword.show()

    # 域名解析函数.
    def _ShowDNS(self):
        self.dnsWindow = MyWindowsDNS()
        self.dnsWindow.show()

    # 文件信息导出主函数.
    def _exportInfo(self):
        self.exportInformation = exportInfoWindows()
        self.exportInformation.show()

    # 网页图表加载函数.
    def _showgraph(self):
        self.widgetGraph.load(QUrl("file:///./templates/grid_horizontal.html"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec())
