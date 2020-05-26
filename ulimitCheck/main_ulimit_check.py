#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 加载python库函数.
import csv
import time
import logging
import os
import threading
from PyQt5 import QtCore, QtWidgets
from ulimit_check_ui import Ui_ulimitCheck
from paramiko import SSHClient
from paramiko import AutoAddPolicy
from logging.handlers import TimedRotatingFileHandler

# 设置打印时间
TIME = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
# DATE = time.strftime('%Y-%m-%d', time.localtime())

# 设置日志路径以及各式.
if not os.path.exists('log'):                                                # 创建日志存储路径.
    os.makedirs('log')
filename = './log/systeminfo.log'
logger = logging.getLogger()
logger.setLevel(logging.INFO)
LogHandler = TimedRotatingFileHandler(filename=filename, when='midnight', interval=1, backupCount=7)
format = ('%(asctime)s %(levelname)s %(message)s')
datefmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(format, datefmt)
LogHandler.setFormatter(formatter)
logger.addHandler(LogHandler)


# 内核ulimit参数检查主类.
class systemCheck(object):
    def __init__(self,host, port, username, password):

        self.host = host
        self.port = port
        self.username = username
        self.password = password

        try:
            self.client = SSHClient()
            self.client.set_missing_host_key_policy(AutoAddPolicy())
            self.client.load_system_host_keys()
            self.client.connect(hostname=self.host, port=self.port, username=self.username, password=self.password, timeout=2,compress=True)
            logging.info('连接主机{0}成功'.format(self.host))

        except Exception as e:
            logging.error('connect to {0} failed, reason {1}'.format(self.host, e))

        finally:
            pass

    # 定义执行命令函数.
    def run_command(self, command):
        try:
            stdin, stdout, stderr = self.client.exec_command(command,bufsize=-1,timeout=2)
            result = stdout.read().decode("utf-8")
            logging.info('主机{0}执行命令{1}成功'.format(self.host,command))
            return result

        except Exception as e:
            logging.error('执行命令{0}失败,原因{1}'.format(command,e))
            return None

        finally:
            self.client.close()

    # 定义内核检查槽函数.
    def kernel_check(self):
        results = self.run_command(command="echo $(hostname;ulimit -n;ulimit -u;uname)")
        if results is None:
            # print(None)
            return None
        else:
            # print(results.split())
            return results.split()

# 定义遍历检查函数.
def call_kernel_check(hostfile='checkhosts.csv'):

    try:
        with open('系统内核参数检查结果.csv','w',newline='',encoding='gbk') as file:
            writer = csv.writer(file, dialect='excel')
            writer.writerow(['检查时间','中心名称','IP地址', '操作系统版本', '主机名称','当前用户','单进程最大句柄数', '单用户最大进程数','巡检人员','用途'])
            try:
                reader = csv.DictReader(open(file=hostfile, encoding='utf-8'))
                for row in reader:
                    site = row['site']
                    host = row['host']
                    port = int(row['port'])
                    user = row['user']
                    password = row['password']
                    operator = row['operator']
                    description = row['description']
                    if site.startswith("#"):
                        continue
                    else:
                        collect = systemCheck(host=host, port=port, username=user, password=password)
                        results = collect.kernel_check()
                        if results is None:
                            continue
                        else:
                            hostname = results[0]
                            open_files = results[1]
                            max_processes = results[2]
                            system_type = results[3]
                            writer.writerow([TIME,site,host,system_type,hostname,user,open_files,max_processes,operator,description])

            except Exception as e:
                    logging.error('读取配置文件失败,{0}'.format(e))

            finally:
                    pass

    except Exception as e:
            logging.error('写入文件系统内核参数检查结果.csv错误,{0}'.format(e))

    finally:
            file.close()


# 定义UI工作线程类.
class ulimitworkThread(QtCore.QThread, QtWidgets.QWidget, QtCore.QObject):
    finshSignal = QtCore.pyqtSignal(object)                                 # 自定义信号finshSignal

    def __init__(self, parent=None):
        super(ulimitworkThread, self).__init__(parent)
        self.flag = 1

# 定义多线程执行主函数.
    def run(self):
            t = threading.Thread(target=call_kernel_check, name='多线程检查执行')
            t.start()
            t.join()
            # print('当前线程ID {0}'.format(QtCore.QThread.currentThreadId()))
            self.finshSignal.emit("ulimit检查结束")
        # self.finshSignal.connect(self.resutl_notice)

# 定义多线程退出函数.
    def stop(self):
        self.flag = 0
        print('线程退出')


"""
# 定义检查结束Slot槽函数.
class ulimitCheckSlot(QtWidgets.QWidget, QtCore.QObject):

    def __init__(self, parent=None):
        super(ulimitCheckSlot, self).__init__(parent)
        #self.setupUi(self)

    def resutl_notice(self):
        result_path = os.getcwd()
        QtWidgets.QMessageBox.information(self,'消息提示','状态: 系统ulimit检查结束\n检查结果存放路径: {0}\系统内核参数检查结果.csv'.format(result_path),QtWidgets.QMessageBox.Ok)
"""


if __name__ == '__main__':
    ulimitworkThread().run()

    """ 
    t = threading.Thread(target=call_kernel_check, name='多线程检查执行')  # 将主函数拉入多线程中
    t.start()                                                            # 启动多线程
    t.join()                                                             # 线程同步,即主线程任务结束之后,进入阻塞状态,一直等待其他的子线程执行结束之后,主线程在终止
    from time import time
    for i in range(10):
        t1 = time()                                                      # 定义t1执行开始时间
        t = threading.Thread(target=call_kernel_check, name='LoopThread')
        t.start()
        t.join()
        # call_kernel_check()
        t2 = time()                                                      # 定义t2执行结束时间
        print('序号:{0}'.format(i) +' '+ f"耗时:{t2 - t1}秒")              # 打印整个程序执行时间 
    """

