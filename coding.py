#!/usr/local/bin/python3
# coding=utf-8
# Time    : 2020/5/8 00:08
# Author  : Ar3h

from hashlib import md5, sha256
from time import strftime, localtime
from traceback import format_exc

# from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from firstMainWin import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from base64 import b64decode, b64encode
from sys import exit, argv
from urllib.parse import quote, unquote

"""

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
                    text_decode = b64decode(line.encode(encoding=self.ENCODING))
                    self.outputText.appendPlainText(text_decode.decode(encoding=self.ENCODING))
            else:
                # 编码 str -> byte -> str
                for line in text_lines:
                    text_decode = b64encode(line.encode(encoding=self.ENCODING))
                    self.outputText.appendPlainText(text_decode.decode(encoding=self.ENCODING))
        except:
            # 打印异常
            self.outputText.appendPlainText(format_exc())

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
                    text_decode = quote(line, encoding=self.ENCODING)
                    self.outputText.appendPlainText(text_decode)
            else:
                # 解码unquote()
                print("url解码")
                for line in text_lines:
                    text_decode = unquote(line, encoding=self.ENCODING)
                    self.outputText.appendPlainText(text_decode)

        except:
            self.outputText.appendPlainText(format_exc())

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
                    hex_str = ""
                    for i in line:
                        hex_str += str(hex(ord(i))[2:]) + ' '
                    self.outputText.appendPlainText(hex_str.strip(" "))
            else:
                # 解码
                print("hex解码")
                for line in text_lines:
                    decode_str = ""
                    for each_char in line.strip(" ").split(" "):
                        decode_char = chr(int(each_char, 16))
                        decode_str += decode_char + " "
                    self.outputText.appendPlainText(decode_str)

        except:
            self.outputText.appendPlainText(format_exc())

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
            self.outputText.appendPlainText(format_exc())

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
            self.outputText.appendPlainText(format_exc())

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
                    # line: str:"\\u0031\\u0032\\u0033" -> str:"123"
                    line_str = line.encode(self.ENCODING).decode("unicode_escape")
                    self.outputText.appendPlainText(line_str)
        except:
            self.outputText.appendPlainText(format_exc())

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
                b = localtime(timestamp)
                dt = strftime('%Y-%m-%d %H:%M:%S', b)
                self.outputText.appendPlainText(dt)

        except:
            self.outputText.appendPlainText(format_exc())

    """md5"""

    @QtCore.pyqtSlot()
    def on_md5_btn_pressed(self):
        print("md5")
        text = self.inputText.toPlainText()
        self.outputText.clear()
        try:
            hash_str = md5(text.encode()).hexdigest()
            self.outputText.appendPlainText(hash_str)
        except:
            self.outputText.appendPlainText(format_exc())

    """sha256"""

    def on_sha256_btn_pressed(self):
        print("sha256")
        text = self.inputText.toPlainText()
        self.outputText.clear()
        try:
            hash_str = sha256(text.encode()).hexdigest()
            self.outputText.appendPlainText(hash_str)
        except:
            self.outputText.appendPlainText(format_exc())

    """清除回车键"""

    @QtCore.pyqtSlot()
    def on_removeReturn_btn_pressed(self):
        print("清除回车")
        text = self.inputText.toPlainText()
        self.outputText.clear()
        self.outputText.appendPlainText(text.replace("\n", ""))

    """清除空格"""

    @QtCore.pyqtSlot()
    def on_removeSpace_btn_pressed(self):
        print("清除空格")
        text = self.inputText.toPlainText()
        self.outputText.clear()
        self.outputText.appendPlainText(text.replace(" ", ""))

    """交换"""

    @QtCore.pyqtSlot()
    def on_exchange_btn_pressed(self):
        in_text = self.inputText.toPlainText()
        out_text = self.outputText.toPlainText()
        self.inputText.clear()
        self.outputText.clear()
        self.inputText.appendPlainText(out_text)
        self.outputText.appendPlainText(in_text)

    """清空"""

    @QtCore.pyqtSlot()
    def on_clear_btn_pressed(self):
        self.inputText.clear()
        self.inputText.clear()
        self.str1_lineEdit.clear()
        self.str2_lineEdit.clear()


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(argv)
    # icon_path = '/Users/arch/Pictures/头像/Hack/6.png'
    # app.setWindowIcon(QIcon(QPixmap(icon_path)))
    myWin = MyMainWindow()
    myWin.show()
    exit(app.exec_())
