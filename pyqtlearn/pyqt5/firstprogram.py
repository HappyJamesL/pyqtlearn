#! /usr/bin/python3
# -*- coding:utf-8 -*-
#  __author__ = 'liu'

import sys

from PyQt5.QtWidgets import QApplication,QWidget, QToolTip, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 13))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('Button', self)
        btn.setToolTip('this is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        qbtn = QPushButton('Quit',self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 100)

        self.setGeometry(300,300, 300, 320)
        self.setWindowTitle('Tooltips')
        # self.setWindowIcon(QIcon('20070420141711640.png'))

        self.show()
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',"Are you sure to quit?",QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
        if reply ==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # w = QWidget()
    # w.resize(250, 150)
    # w.move(1, 300)
    # w.setWindowTitle('Simple')
    # w.show()

    ex = Example()
    sys.exit(app.exec_())

