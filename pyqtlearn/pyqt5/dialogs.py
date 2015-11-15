#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication,QFrame, QColorDialog,
                             QVBoxLayout, QSizePolicy, QLabel, QFontDialog,
                             QTextEdit,QAction, QFileDialog, QMainWindow)
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        col = QColor(10, 10, 100)
        self.btn1 = QPushButton('Color Dialog', self)
        self.btn1.move(20, 20)
        self.btn1.clicked.connect(self.showColorDialog)
        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidget {background-color: %s }' % col.name())
        self.frm.setGeometry(130, 20, 100, 20)

        self.btn = QPushButton('input Dialog', self)
        self.btn.move(20, 50)
        self.btn.clicked.connect(self.showInputDialog)
        self.le = QLineEdit(self)
        self.le.move(130, 50)

        # vbox = QVBoxLayout()
        btn3 = QPushButton('Font Dialog', self)
        # btn3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn3.move(20, 80)
        # vbox.addWidget(btn3)
        btn3.clicked.connect(self.showFontDialog)
        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(110, 80)
        # vbox.addWidget(self.lbl)
        # self.setLayout(vbox)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle(' Dialog')
        self.show()

    def showInputDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.le.setText(text)

    def showColorDialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet('QWidget{ background-color: %s }' % col.name())

    def showFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

class Example1(QMainWindow):
    def __init__(self):
        super(Example1, self).__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction('open',self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showFileDialog)

        menuber = self.menuBar()
        fileMenu = menuber.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex1 = Example1()
    sys.exit(app.exec_())

