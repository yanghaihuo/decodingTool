#!/usr/local/bin/python3
# coding=utf-8
# Time    : 2020/5/8 00:08
# Author  : Ar3h
import hashlib
import sys
import time
import traceback

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from firstMainWin import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
import base64
import sys
from urllib import parse

"""
TODO：
✅标签页
替换文本高亮显示
正则替换

去换行，去空格

多线程
文件优化：模块化
可加载插件
吸取有点
"""


# 继承Ui_MainWindow
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # 判断编码还是解码
        self.ENCODE_METHOD = False if self.decode_rbtn.isChecked() else True
        self.ENCODING = "utf-8" if self.utf8_rbtn.isChecked() else "gbk"

    """base64"""

    @QtCore.pyqtSlot()
    def on_base64_btn_pressed(self):
        text = self.inputText.toPlainText()
        text_lines = text.splitlines()
        self.outputText.clear()

        try:
            if self.decode_rbtn.isChecked():
                # 解码 str -> byte -> str
                for line in text_lines:
                    text_decode = base64.b64decode(line.encode(encoding=self.ENCODING))
                    self.outputText.appendPlainText(text_decode.decode(encoding=self.ENCODING))
            else:
                # 编码 str -> byte -> str
                for line in text_lines:
                    text_decode = base64.b64encode(line.encode(encoding=self.ENCODING))
                    self.outputText.appendPlainText(text_decode.decode(encoding=self.ENCODING))
        except:
            # 打印异常
            self.outputText.setText(traceback.format_exc())

    """url"""

    @QtCore.pyqtSlot()
    def on_url_btn_pressed(self):
        text = self.inputText.toPlainText()
        text_lines = text.splitlines()
        self.outputText.clear()

        try:
            if self.encode_rbtn.isChecked():
                # 编码quote()
                print("url编码")
                for line in text_lines:
                    text_decode = parse.quote(line, encoding=self.ENCODING)
                    self.outputText.appendPlainText(text_decode)
            else:
                # 解码unquote()
                print("url解码")
                for line in text_lines:
                    text_decode = parse.unquote(line, encoding=self.ENCODING)
                    self.outputText.appendPlainText(text_decode)

        except:
            self.outputText.setText(traceback.format_exc())

    """hex"""

    @QtCore.pyqtSlot()
    def on_hex_btn_pressed(self):
        import binascii
        text = self.inputText.toPlainText()
        text_lines = text.splitlines()
        self.outputText.clear()

        try:
            if self.encode_rbtn.isChecked():
                # 编码
                print("hex编码")
                print(self.ENCODE_METHOD)
                for line in text_lines:
                    str_bin = line.encode(self.ENCODING)
                    hex_str = binascii.hexlify(str_bin).decode(self.ENCODING)
                    self.outputText.appendPlainText(hex_str)
            else:
                # 解码
                print("hex解码")
                for line in text_lines:
                    self.outputText.appendPlainText((binascii.unhexlify(line)).decode())
        except:
            self.outputText.appendPlainText(traceback.format_exc())

    """replace"""

    @QtCore.pyqtSlot()
    def on_replace_btn_pressed(self):
        str1 = self.str1_lineEdit.text().strip("\n")
        str2 = self.str2_lineEdit.text().strip("\n")
        text = self.inputText.toPlainText()
        text_lines = text.splitlines()
        self.outputText.clear()

        try:
            for line in text_lines:
                converted_str = line.replace(str1, str2)
                self.outputText.appendPlainText(converted_str)
        except:
            self.outputText.setText(traceback.format_exc())

    """html"""

    @QtCore.pyqtSlot()
    def on_html_btn_pressed(self):
        text = self.inputText.toPlainText()
        text_lines = text.splitlines()
        self.outputText.clear()

        try:
            import html
            if self.encode_rbtn.isChecked():
                # 编码
                print("html编码")
                for line in text_lines:
                    print(line)
                    self.outputText.appendPlainText(html.escape(line))
            else:
                print("html解码")
                # 解码
                for line in text_lines:
                    self.outputText.appendPlainText(html.unescape(line))
        except:
            self.outputText.setText(traceback.format_exc())

    """unicode"""

    @QtCore.pyqtSlot()
    def on_unicode_btn_pressed(self):
        text = self.inputText.toPlainText()
        text_lines = text.splitlines()
        self.outputText.clear()

        try:
            if self.encode_rbtn.isChecked():
                # 编码
                print("unicode编码")
                for line in text_lines:
                    line_unicode = ""
                    for eachChar in line:
                        line_unicode += "\\u" + hex(ord(eachChar))[2:].zfill(4)
                    self.outputText.appendPlainText(line_unicode)
            else:
                # 解码
                print("unicode解码")
                for line in text_lines:
                    self.outputText.appendPlainText(str(line))
        except:
            self.outputText.setText(traceback.format_exc())

    """时间戳
    """

    @QtCore.pyqtSlot()
    def on_timestamp_btn_pressed(self):
        text = self.inputText.toPlainText()
        text_lines = text.splitlines()
        self.outputText.clear()
        print("timestamp")

        try:
            for line in text_lines:
                timestamp = int(line)
                b = time.localtime(timestamp)
                dt = time.strftime('%Y-%m-%d %H:%M:%S', b)
                self.outputText.appendPlainText(dt)

        except:
            self.outputText.setText(traceback.format_exc())

    """md5"""

    @QtCore.pyqtSlot()
    def on_md5_btn_pressed(self):
        text = self.inputText.toPlainText()
        try:
            hash_str = hashlib.md5(text.encode()).hexdigest()
            self.outputText.setText(hash_str)
        except:
            self.outputText.setText(traceback.format_exc())

    """sha256"""

    def on_sha256_btn_pressed(self):
        text = self.inputText.toPlainText()
        try:
            hash_str = hashlib.sha256(text.encode()).hexdigest()
            self.outputText.setText(hash_str)
        except:
            self.outputText.setText(traceback.format_exc())

    """交换"""

    @QtCore.pyqtSlot()
    def on_exchange_btn_pressed(self):
        in_text = self.inputText.toPlainText()
        out_text = self.outputText.toPlainText()
        self.inputText.setText(out_text)
        self.outputText.setText(in_text)

    """清空"""

    @QtCore.pyqtSlot()
    def on_clear_btn_pressed(self):
        self.inputText.clear()
        self.inputText.clear()
        self.str1_lineEdit.clear()
        self.str2_lineEdit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon_path = '/Users/arch/Pictures/头像/Hack/6.png'
    app.setWindowIcon(QIcon(QPixmap(icon_path)))
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
