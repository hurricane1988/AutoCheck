#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
from threading import Thread
from PyQt5 import QtWidgets,QtGui,QtCore
from PortScan import Ui_PortScan


# 端口扫描主类.
class portScanWindow(QtWidgets.QWidget,Ui_PortScan):
    def __init__(self, parent=None):
        super(portScanWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('login.ico'))
        self.setupUi(self)

        self.ports_list = []

        self.pushButtonStart.clicked.connect(self.portCheck)
        self.pushButtonScanIP.clicked.connect(self.scanPorts)

    # TCP端口开启状态检查.
    def tcp_Port(self,ip,port,timeout):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server.settimeout(timeout)
            server.connect((ip,int(port)))
            self.ports_list.append(port)
            return True
        except Exception as e:
            return False
        finally:
            server.close()

    # UDP端口开启状态检查.
    def udp_Port(self,ip,port,timeout):
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            server.settimeout(timeout)
            server.connect((ip,int(port)))
            return True
        except Exception as e:
            return False
        finally:
            server.close()

    # 端口开启状态检查函数.
    def portCheck(self):
        try:
            INPUT = self.lineEditInput.text().split('/')
            IP = INPUT[0]
            PRO = INPUT[1]
            PORT = INPUT[2]

            if PRO == 'tcp' or 'TCP':
                result = self.tcp_Port(IP,PORT,2)
                if result is True:
                    self.textEditScanResult.setText('IP地址: '+IP+'\n'+'协议: '+PRO+'\n'+'端口: '+PORT+'\n'+'端口状态: '+'开启')
                else:
                    self.textEditScanResult.setText(
                        'IP地址: '+IP+'\n'+'协议: '+PRO+'\n'+'端口: '+PORT+'\n'+'端口状态: '+'关闭')

            elif PRO == 'udp' or  'UDP':
                result = self.udp_Port(IP,PORT,2)
                if result is True:
                    self.textEditScanResult.setText(
                        'IP地址: ' + IP + '\n' + '协议: ' + PRO + '\n' + '端口: ' + PORT + '\n' + '端口状态: ' + '开启')
                else:
                    self.textEditScanResult.setText(
                        'IP地址: ' + IP + '\n' + '协议: ' + PRO + '\n' + '端口: ' + PORT + '\n' + '端口状态: ' + '关闭')
        except Exception as e:
            QtWidgets.QMessageBox.warning(self,'错误提示','输入的扫描信息错误')
        finally:
            pass

    # 端口扫描检查
    def scanPorts(self):
        pass

        """
        try:
            IP  = self.lineEditScanIP.text()

            for port in range(1,65536):
                result = Thread(target=self.tcp_Port, args=(IP,port,2))
                result.start()
            self.textEditScanResult.setText('IP地址: '+ IP +'\n' +'协议: ' + 'TCP' + '\n' + '开启端口: ' + " ".join(self.ports_list))
        except Exception as e:
            pass
        finally:
            pass
        """


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = portScanWindow()
    win.show()
    sys.exit(app.exec())

