# # -*- coding:utf-8 -*-
# """演示程序"""
# import sys
# from PyQt5 import QtWidgets
#
#
# class GeoQuery(QtWidgets.QWidget):
#     def __init__(self):
#         super(GeoQuery, self).__init__()
#
#         self.setWindowTitle("演示程序")
#
#         self.flag = 1  # 用来控制while循环的结束
#         grid = QtWidgets.QGridLayout()
#
#         # 添加开始按钮并设定点击它出发start函数
#         start_button = QtWidgets.QPushButton("开始")
#         start_button.clicked.connect(self.start)
#         grid.addWidget(start_button, 0, 3)
#
#         # 添加停止按钮并设定点击它出发stop函数
#         start_button = QtWidgets.QPushButton("停止")
#         start_button.clicked.connect(self.stop)
#         grid.addWidget(start_button, 1, 3)
#
#         # 添加信息显示框用来显示一些必要的信息
#         self.list_edit = QtWidgets.QListWidget()
#         grid.addWidget(self.list_edit, 0, 0, 3, 3)
#
#         self.setLayout(grid)
#
#     def start(self):
#         import time
#         i = 0
#         while self.flag == 1:
#             i += 1
#             time.sleep(1)
#             # 把这个语句换为你的程序任务处理
#             self.list_edit.addItem("正在处理第{}个文件".format(i))
#             QtWidgets.QApplication.processEvents()
#
#          # 把这个语句换为你打断程序循环之后需要程序进行的任务（如保存上下文）
#         self.list_edit.addItem("正在记录处理位置")
#         self.list_edit.addItem("处理到了第{}个数据,并结束".format(i))
#
#     def stop(self):
#             self.flag = 0
#
# app = QtWidgets.QApplication(sys.argv)
# geo_query = GeoQuery()
# geo_query.show()
# sys.exit(app.exec_())






# __author__ = 'liu'
#!/usr/bin/python3
# -*- coding:utf-8 -*-

import string,sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.checkio(self)

    def checkio(text):
        text = text.lower()
        print(type(text))
        return max(string.ascii_lowercase, key=text.count)
    # str.ascii_lowercase
    ax = checkio('saasada11111111!!!!!!!!f')
    print(ax)
    print(checkio('fgFdhasaf'))

# print(max('ah', 'bj', key=lambda x: x[1]))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # widget = QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(widget)
    # widget.show()
    ex = Example()
    ex.show()
    sys.exit(app.exec_())