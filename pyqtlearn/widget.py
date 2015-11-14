#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
勾选框，颜色混合，滚动条，进度条，日历
'''
import sys
from PyQt5.QtWidgets import (QWidget, QCheckBox, QApplication,
                             QPushButton, QFrame,
                             QSlider, QLabel,
                             QProgressBar, QCalendarWidget)
from PyQt5.QtCore import Qt, QBasicTimer, QDate
from PyQt5.QtGui import QColor, QPixmap


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # checkBox
        cb = QCheckBox('show title', self)
        cb.move(10, 10)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        # 颜色混合
        self.col = QColor(0, 0, 0)
        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 30)
        redb.clicked[bool].connect(self.setColor)

        grnb = QPushButton('Green', self)
        grnb.setCheckable(True)
        grnb.move(10, 60)
        grnb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 90)
        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 50, 50)
        self.square.setStyleSheet("QWidget { background-color: %s}" %
                                  self.col.name())

        # slider 滚动条
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(10, 120, 100, 10)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('1.png'))
        self.label.setGeometry(150, 90, 80, 80)

        # 进度条ProgressBar
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(10, 170, 200, 20)
        self.btn = QPushButton('Start', self)
        self.btn.move(10, 200)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        # Calendar 日历
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(10, 230)
        cal.clicked[QDate].connect(self.showDate)
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(80, 440)

        self.setGeometry(300, 200, 300, 500)
        self.setWindowTitle('Toggle')
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('Toogle')
        else:
            self.setWindowTitle(' ')

    def setColor(self, pressed):
        source = self.sender()
        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame {background-color: %s}" % self.col.name())

    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(QPixmap('1.png'))
        elif 0 < value <= 30:
            self.label.setPixmap(QPixmap('2.png'))
        elif 30 < value < 80:
            self.label.setPixmap(QPixmap('3.png'))
        else:
            self.label.setPixmap(QPixmap('4.png'))

    def timerEvent(self, *args, **kwargs):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step += 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')

    def showDate(self, date):
        self.lbl.setText(date.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
