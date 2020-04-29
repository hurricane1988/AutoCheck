#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import time
import sys
import subprocess
import multiprocessing
from io import StringIO
from PyQt5 import QtWidgets, QtGui


# Ping连通性检查主类.
class myWindowPing(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(myWindowPing, self).__init__(parent)

        self.setWindowIcon(QtGui.QIcon('login.ico'))

    def _pingCheck(self):
        results = subprocess.call('ping -w 1000 -n 1 %s' %ip,stdout=subprocess.PIPE,shell=True)
