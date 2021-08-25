import os
import sys
import pathlib

from PyQt5.QtWidgets import (
    QApplication,
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
        self.html_writer.write("홍길동")

        self.filepath = os.path.join(os.getcwd(), "index.html")
        windows_path = pathlib.PureWindowsPath(self.filepath)
        index_path = windows_path.as_uri()
        self.home = QUrl(index_path)

        hbox = QHBoxLayout()
        self.btn_prn = QPushButton('Print')
        hbox.addWidget(self.btn_prn)

        self.webview = QWebEngineView()
        self.webview.load(self.home)

        vbox = QVBoxLayout(self)
        vbox.addLayout(hbox)
        vbox.addWidget(self.webview)

        self.setWindowTitle('레이블 출력기')
        self.setLayout(vbox)

        QApplication.instance().installEventFilter(self)
        self.btn_prn.clicked.connect(self.onPrint)

    def eventFilter(self, obj, e):
        if e.type() == QEvent.KeyPress and e.key() == Qt.Key_Return:
            self.onMove()
            return True
        return super().eventFilter(obj, e)

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
