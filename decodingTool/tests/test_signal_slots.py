# coding=utf-8
# Time    : 2020/7/9 18:05
# Author  : Ar3h

import sys

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore

app = QApplication(sys.argv)
widget = QWidget()


# 槽类
class CustSlots(QObject):
    def __init__(self):
        super(CustSlots, self).__init__()

    def callSlots(self):
        print("Call callSlots()")



# 信号类
class CustSignal(QObject):
    # 定义信号
    signal1 = pyqtSignal()

    def __init__(self, parent=None):
        super(CustSignal, self).__init__(parent)
        self.setObjectName("custSignal")
        QtCore.QMetaObject.connectSlotsByName(self)


    @QtCore.pyqtSlot()
    def on_custSignal_signal1(self):
        print('装饰器的槽函数被调用')


if __name__ == '__main__':
    # QtCore.QMetaObject.connectSlotsByName(QObject)
    # 信号对象
    custSignal = CustSignal()
    # 槽对象
    custSlots = CustSlots()
    # 信号 connect to 槽函数
    custSignal.signal1.connect(custSlots.callSlots)
    # 发送信号对象
    custSignal.signal1.emit()
