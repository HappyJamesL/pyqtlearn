# __author__ = 'liu'
#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction,qApp, QTextEdit,QLabel
from PyQt5.QtGui import QIcon
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        lbl1 = QLabel('PyQt5', self)
        lbl1.move(15,10)
        lbl2 = QLabel('tutorial',self)
        lbl2.move(35, 40)
        lbl3 = QLabel('for Programmers', self)
        lbl3.move(55, 70)

        exitAction = QAction(QIcon('20070420141711640.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.exittoolbar = self.addToolBar('FileExit')
        self.exittoolbar.addAction(exitAction)
        self.editbar = self.addToolBar('Edit')
        # self.editbar.addAction(exitAction)

        self.statusBar().showMessage('Ready')
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
