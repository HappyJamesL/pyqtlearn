#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication,
                             QLineEdit, QFrame, QSplitter, QStyleFactory,
                             QComboBox)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        # hbox = QHBoxLayout(self)
        #
        # pixmap = QPixmap("11.jpg")
        # lbl1 = QLabel(self)
        # lbl1.setPixmap(pixmap)

        # topleft = QFrame(self)
        # topleft.setFrameShape(QFrame.StyledPanel)
        # topright = QFrame(self)
        # topright.setFrameShape(QFrame.StyledPanel)
        # bottom = QFrame(self)
        # bottom.setFrameShape(QFrame.StyledPanel)
        #
        # spllitter1 = QSplitter(Qt.Horizontal)
        # spllitter1.addWidget(topleft)
        # spllitter1.addWidget(topright)
        # spllitter2 = QSplitter(Qt.Vertical)
        # spllitter2.addWidget(spllitter1)
        # spllitter2.addWidget(lbl1)
        #
        # hbox.addWidget(spllitter2)
        # self.setLayout(hbox)

        # 标签 文字
        self.lbl2 = QLabel(self)
        qle = QLineEdit(self)
        qle.move(10, 40)
        self.lbl2.move(10, 1)
        qle.textChanged[str].connect(self.onChanged)

        self.lbl3 = QLabel('Ubuntu',self)
        combo = QComboBox(self)
        combo.addItem('Ubuntu')
        combo.addItem('Madriva')
        combo.addItem('Fedora')
        combo.addItem('Arch')
        combo.addItem('Gentoo')
        combo.move(10, 70)
        self.lbl3.move(100, 75)
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Widget2')
        self.show()

    def onChanged(self, text):
        self.lbl2.setText(text)
        self.lbl2.adjustSize()

    def onActivated(self,text):
        self.lbl3.setText(text)
        self.lbl3.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
