# coding=utf-8
# Time    : 2020/5/7 23:17
# Author  : Ar3h

import sys
from PyQt5.QtWidgets import *


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('onclick to close windows')
        quit = QPushButton('Close', self)
        quit.setGeometry(10, 10, 60, 35)
        quit.setStyleSheet("background-color:red")
        quit.clicked.connect(self.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win=WinForm()
    win.show()
    sys.exit(app.exec_())