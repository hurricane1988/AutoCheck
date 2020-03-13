#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
from PyQt5 import QtWidgets,QtGui,QtCore
from PortScan import Ui_PortScan


# 端口扫描主类.
class portScanWindow(QtWidgets.QWidget,Ui_PortScan):
    def __init__(self, parent=None):
        super(portScanWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('login.ico'))
        self.setupUi(self)

        self.pushButtonStart.clicked.connect(self.portCheck)
        self.pushButtonScanIP.clicked.connect(self.scanCheck)

    # 端口开启状态检查函数.
    def portCheck(self):
        try:
            INPUT = self.lineEditInput.text().split('/')
            IP = INPUT[0]
            PRO = INPUT[1]
            PORT = INPUT[2]
            if PRO == 'tcp' or PRO == 'TCP':
                server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                try:
                    server.connect((IP,PORT))
                    self.textEditScanResult.setText(
                        'IP地址: '+IP+'\n'+'协议: '+PRO+'\n'+'端口: '+PORT+'\n'+'端口状态: '+'开启')
                except Exception as e:
                    self.textEditScanResult.setText(
                        'IP地址: '+IP+'\n'+'协议: '+PRO+'\n'+'端口: '+PORT+'\n'+'端口状态: '+'关闭')
                finally:
                    server.close()
            elif PRO == 'udp' or PRO == 'UDP':
                server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                try:
                    server.connect((IP,PORT))
                    self.textEditScanResult.setText(
                        'IP地址: ' + IP + '\n' + '协议: ' + PRO + '\n' + '端口: ' + PORT + '\n' + '端口状态: ' + '开启')
                except Exception as e:
                    self.textEditScanResult.setText(
                        'IP地址: ' + IP + '\n' + '协议: ' + PRO + '\n' + '端口: ' + PORT + '\n' + '端口状态: ' + '关闭')
                finally:
                    server.close()
        except Exception as e:
            QtWidgets.QMessageBox.warning(self,'错误提示','输入的扫描信息错误')
        finally:
            pass

    # 端口扫描检查
    def scanCheck(self):
        try:
            ports_list = []
            IP  = self.lineEditScanIP.text()
        except Exception as e:
            pass
        finally:
            pass




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = portScanWindow()
    win.show()
    sys.exit(app.exec())

