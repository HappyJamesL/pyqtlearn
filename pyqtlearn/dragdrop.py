#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
修改按钮文字
右键拖动按钮
"""
import sys
from PyQt5.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication)
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag


class Button(QPushButton):
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)
        self.setAcceptDrops(True)

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            return
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        # QPushButton.mousePressEvent(self, e)
        if e.button() == Qt.LeftButton:
            print('press')

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 35)

        button = Button("Button", self)
        button.move(190, 35)

        self.setAcceptDrops(True)
        self.button = Button('Click or Move', self)
        self.button.move(100, 100)

        self.setWindowTitle('drag & drop')
        self.setGeometry(300, 300, 300, 150)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)
        e.setDropAction(Qt.MoveAction)
        e.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
