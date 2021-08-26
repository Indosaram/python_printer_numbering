import os
import sys
import pathlib

from PyQt5.QtWidgets import (
    QApplication,
    QLineEdit,
    QMessageBox,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt, QUrl, QEvent, QEventLoop
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QPainter

from html_writer import HTMLWriter

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


class Form(QWidget):
    def __init__(self):
        super().__init__()

        self.html_writer = HTMLWriter()
        self.html_writer.write()

        self.filepath = os.path.join(os.getcwd(), "index.html")
        windows_path = pathlib.PureWindowsPath(self.filepath)
        index_path = windows_path.as_uri()
        self.home = QUrl(index_path)

        self.text_input = QLineEdit()
        self.text_send = QPushButton('Search')
        self.text_send.clicked.connect(self.on_click_test_send_btn)

        hbox = QHBoxLayout()
        self.btn_prn = QPushButton('Print')
        hbox.addWidget(self.text_input)
        hbox.addWidget(self.text_send)
        hbox.addWidget(self.btn_prn)

        self.webview = QWebEngineView()
        self.webview.load(self.home)

        vbox = QVBoxLayout(self)
        vbox.addLayout(hbox)
        vbox.addWidget(self.webview)

        self.setWindowTitle('레이블 출력기')
        self.setLayout(vbox)
        self.vbox = vbox

        QApplication.instance().installEventFilter(self)
        self.btn_prn.clicked.connect(self.onPrint)

    def on_click_test_send_btn(self):
        if not self.html_writer.write(self.text_input.text()):
            QMessageBox.question(
                self,
                'Warning',
                '회원이 존재하지 않습니다.',
                QMessageBox.Ok,
                QMessageBox.NoButton,
            )
        self.webview.load(self.home)

    def onPrint(self):
        printer = QPrinter()
        printer.setResolution(120)
        printer.setPageSize(QPrinter.A4)
        loop = QEventLoop()
        result = False

        def printPreView(success):
            nonlocal result
            result = success
            loop.quit()

        page = self.webview.page()
        page.print(printer, printPreView)
        loop.exec_()

        if not result:
            qp = QPainter()
            if qp.begin(printer):
                font = qp.font()
                font.setPixelSize(20)
                qp.setFont(font)
                qp.drawText(10, 25, "Could not generate print preview")
                qp.end()

        self.html_writer.write("홍길동")
        self.webview.load(self.home)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
