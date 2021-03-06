#!/usr/bin/env python
# -*- coding : utf-8 -*-


import time
import csv
from exportinfo import Ui_FormExport
from PyQt5 import QtWidgets, QtCore, QtGui
from Configuration import cursor


# 文件导出窗口主类.
class exportInfoWindows(QtWidgets.QWidget,Ui_FormExport):

    def __init__(self, parent=None):
        super(exportInfoWindows, self).__init__(parent)
        self.time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('login.ico'))

        # 默认致服务器导出选项为选择状态;
        self.radioButtonSelectServer.setChecked(True)

        # 导出按钮与函数绑定.
        self.pushButtonExport.clicked.connect(self.exportButton)

        # 点击取消按钮
        self.pushButtonCancel.clicked.connect(self.close)

    # 定义导出主函数.
    def exportButton(self):
        try:

            if self.radioButtonSelectServer.isChecked() == True:
                self.exportServers()

            elif self.radioButtonSelectDatabases.isChecked() == True:
                self.exportDatabases()

        except Exception as e:
            QtWidgets.QMessageBox.warning(self,'错误提示','导出信息失败\n{0}'.format(e),QtWidgets.QMessageBox.Ok)

        finally:
            pass


    # 导出服务器资产信息函数.
    def exportServers(self):
        # 获取保存路径.
        try:
            directory = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
            servers = cursor.execute("select * from t_server")
            with open('{0}/{1}-servers.csv'.format(directory,self.time),'w',newline='') as file:
                writer = csv.writer(file, dialect='excel')
                writer.writerow(['ID', 'IP地址','操作系统版本','用户名称','用户密码','描述','系统类型'])
                writer.writerows(servers)
            file.close()
            QtWidgets.QMessageBox.information(self, '提示信息', '导出服务器信息成功\n存放路径{0}'.format(directory),
                                              QtWidgets.QMessageBox.Cancel)

        except Exception as e:
            QtWidgets.QMessageBox.warning(self,'错误提示','导出服务器信息失败\n错误信息{0}'.format(e),QtWidgets.QMessageBox.Cancel)

        finally:
            self.close()

    # 导出数据库资产信息函数.
    def exportDatabases(self):
        # 获取保存路径.
        try:
            directory = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
            databases = cursor.execute("select * from t_database")

            with open('{0}/{1}-database.csv'.format(directory,self.time),'w',newline='') as file:
                writer = csv.writer(file,dialect='excel')
                writer.writerow(['ID', 'IP地址', '数据库类型', '数据库版本', '数据库库名', '账号','密码','描述'])
                writer.writerows(databases)
            file.close()
            QtWidgets.QMessageBox.information(self, '提示信息', '导出数据库信息成功\n存放路径{0}'.format(directory),
                                          QtWidgets.QMessageBox.Cancel)
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, '错误提示', '导出数据库信息失败\n错误信息{0}'.format(e), QtWidgets.QMessageBox.Cancel)

        finally:
            self.close()