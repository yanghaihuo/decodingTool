#!/usr/local/bin/python3
# coding = utf-8
# Time    : 2020/7/10 02:00
# Author  : Ar3h

import functools
from hashlib import md5, sha256
from time import strftime, localtime
from traceback import format_exc

from PyQt5.QtWidgets import *

from decodingTool.gui.mainWindow import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from base64 import b64decode, b64encode
from sys import exit, argv
from urllib.parse import quote, unquote


def intiText():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                func(self)
                self.outputText.repaint()
            except:
                self.outputText.setPlainText(format_exc())
            # 刷新output框（可能是pyqt的bug）

        return wrapper

    return decorator


# 继承Ui_MainWindow
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app: QApplication, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # 判断编码还是解码
        self.ENCODE_METHOD = False if self.decode_rbtn.isChecked() else True
        self.ENCODING = "utf-8" if self.utf8_rbtn.isChecked() else "gbk"
        self.app = app

    # base64
    @intiText()
    @QtCore.pyqtSlot()
    def on_base64_btn_pressed(self):
        text = self.inputText.toPlainText()
        text_lines = text.splitlines()
        if self.decode_rbtn.isChecked():
            for line in text_lines:  # 解码 str -> byte -> str
                text_decode = b64decode(line.encode(encoding=self.ENCODING))
                self.outputText.setPlainText(text_decode.decode(encoding=self.ENCODING))
        else:
            for line in text_lines:  # 编码 str -> byte -> str
                text_decode = b64encode(line.encode(encoding=self.ENCODING))
                self.outputText.setPlainText(text_decode.decode(encoding=self.ENCODING))

    # url
    @intiText()
    @QtCore.pyqtSlot()
    def on_url_btn_pressed(self):
        text = self.inputText.toPlainText()
        text_lines = text.splitlines()

        if self.encode_rbtn.isChecked():
            print("url编码")
            for line in text_lines:  # 编码quote()

                text_decode = quote(line, encoding=self.ENCODING)
                self.outputText.setPlainText(text_decode)
        else:
            print("url解码")
            for line in text_lines:  # 解码unquote()
                text_decode = unquote(line, encoding=self.ENCODING)
                self.outputText.setPlainText(text_decode)

    # hex
    @intiText()
    @QtCore.pyqtSlot()
    def on_hex_btn_pressed(self):
        text = self.inputText.toPlainText()
        text_lines = text.splitlines()

        if self.encode_rbtn.isChecked():
            print("hex编码")
            for line in text_lines:  # 编码
                hex_str = ""
                for i in line:
                    hex_str += str(hex(ord(i))[2:]) + ' '
                self.outputText.setPlainText(hex_str.strip(" "))
        else:
            print("hex解码")
            for line in text_lines:  # 解码
                decode_str = ""
                for each_char in line.strip(" ").split(" "):
                    decode_char = chr(int(each_char, 16))
                    decode_str += decode_char
                self.outputText.setPlainText(decode_str)

    # replace
    @intiText()
    @QtCore.pyqtSlot()
    def on_replace_btn_pressed(self):
        str1 = self.str1_lineEdit.text().strip("\n")
        str2 = self.str2_lineEdit.text().strip("\n")
        text = self.inputText.toPlainText()
        text_lines = text.splitlines()

        for line in text_lines:
            converted_str = line.replace(str1, str2)
            self.outputText.setPlainText(converted_str)

    # html
    @intiText()
    @QtCore.pyqtSlot()
    def on_html_btn_pressed(self):
        text = self.inputText.toPlainText()
        text_lines = text.splitlines()
        self.outputText.clear()

        import html
        if self.encode_rbtn.isChecked():
            print("html编码")
            for line in text_lines:  # 编码
                print(line)
                self.outputText.setPlainText(html.escape(line))
        else:
            print("html解码")
            for line in text_lines:  # 解码
                self.outputText.setPlainText(html.unescape(line))

    # unicode
    @intiText()
    @QtCore.pyqtSlot()
    def on_unicode_btn_pressed(self):
        text = self.inputText.toPlainText()
        text_lines = text.splitlines()

        if self.encode_rbtn.isChecked():
            print("unicode编码")
            for line in text_lines:  # 编码
                line_unicode = ""
                for eachChar in line:
                    line_unicode += "\\u" + hex(ord(eachChar))[2:].zfill(4)
                self.outputText.setPlainText(line_unicode)
        else:
            print("unicode解码")
            for line in text_lines:  # 解码
                # line = "\\u0031\\u0032\\u0033":str -> "123":str
                line_str = line.encode(self.ENCODING).decode("unicode_escape")
                self.outputText.setPlainText(line_str)

    # timestamp
    @intiText()
    @QtCore.pyqtSlot()
    def on_timestamp_btn_pressed(self):
        text = self.inputText.toPlainText()
        text_lines = text.splitlines()
        print("timestamp")

        for line in text_lines:
            timestamp = int(line)
            b = localtime(timestamp)
            dt = strftime('%Y-%m-%d %H:%M:%S', b)
            self.outputText.setPlainText(dt)

    # md5
    @intiText()
    @QtCore.pyqtSlot()
    def on_md5_btn_pressed(self):
        print("md5")
        text = self.inputText.toPlainText()
        if text.startswith("file:///"):  # 文件
            fp = open(text.replace("file:///", "/"), "rb")
            hash_str = md5(fp.read()).hexdigest()
        else:
            hash_str = md5(text.encode()).hexdigest()
        self.outputText.setPlainText(hash_str)

    # sha256
    @intiText()
    @QtCore.pyqtSlot()
    def on_sha256_btn_pressed(self):
        print("sha256")
        text = self.inputText.toPlainText()
        if text.startswith("file:///"):  # 文件
            fp = open(text.replace("file:///", "/"), "rb")
            hash_str = sha256(fp.read()).hexdigest()
        else:
            hash_str = sha256(text.encode()).hexdigest()
        self.outputText.setPlainText(hash_str)

    # 二维码
    @intiText()
    @QtCore.pyqtSlot()
    def on_qr_btn_pressed(self):
        print("二维码识别")
        from pyzbar.pyzbar import decode
        from pyzbar.pyzbar import ZBarSymbol
        from PIL import Image
        text = self.inputText.toPlainText()
        file_path = text.replace("file:///", "/")
        print(file_path)
        img = Image.open(file_path)
        barcodes = decode(img, symbols=[ZBarSymbol.QRCODE])
        for barcode in barcodes:
            url = barcode.data.decode("utf-8")
            self.outputText.setPlainText(url)
            print(url)

    # 清除回车
    @intiText()
    @QtCore.pyqtSlot()
    def on_removeReturn_btn_pressed(self):
        print("清除回车")
        text = self.inputText.toPlainText()
        self.outputText.setPlainText(text.replace("\n", ""))

    # 清除空格
    @intiText()
    @QtCore.pyqtSlot()
    def on_removeSpace_btn_pressed(self):
        print("清除空格")
        text = self.inputText.toPlainText()
        self.outputText.clear()
        self.outputText.setPlainText(text.replace(" ", ""))

    # exchange
    @intiText()
    @QtCore.pyqtSlot()
    def on_exchange_btn_pressed(self):
        in_text = self.inputText.toPlainText()
        out_text = self.outputText.toPlainText()
        self.inputText.setPlainText(out_text)
        self.outputText.setPlainText(in_text)

    # clear all
    @intiText()
    @QtCore.pyqtSlot()
    def on_clear_btn_pressed(self):
        self.inputText.clear()
        self.inputText.clear()
        self.str1_lineEdit.clear()
        self.str2_lineEdit.clear()


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(argv)
    myWin = MyMainWindow(app)
    myWin.show()
    exit(app.exec_())
