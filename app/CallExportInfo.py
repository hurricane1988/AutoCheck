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
        self.radioButtonSelectServer.setChecked(True)

        # 判断选项按钮选择的是服务器还是数据库.
        if self.radioButtonSelectServer.isChecked() == True:
            self.pushButtonExport.clicked.connect(self.exportServers)
        elif self.radioButtonSelectDatabases.isChecked() == True:
            self.pushButtonExport.clicked.connect(self.close)
        # 点击取消按钮
        self.pushButtonCancel.clicked.connect(self.close)

    def exportServers(self):
        # 获取保存路径
        try:
            directory = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
            servers = cursor.execute("select * from t_server")
            with open('{0}/{1}-servers.csv'.format(directory,self.time),'w',newline='') as file:
                writer = csv.writer(file, dialect='excel')
                writer.writerow(['ID', 'IP地址','操作系统版本','用户名称','用户密码','描述','系统类型'])
                writer.writerows(servers)
            file.close()
            QtWidgets.QMessageBox.information(self, '提示信息', '导出服务器信息成功\n存放路径{0}'.format(directory), QtWidgets.QMessageBox.Cancel)

        except Exception as e:
            QtWidgets.QMessageBox.warning(self,'错误提示','导出服务器信息失败\n错误信息{0}'.format(e),QtWidgets.QMessageBox.Cancel)

        finally:
            self.close()