# __author__ = 'liu'
import sys, math, traceback
from PyQt5.QtWidgets import ( QMainWindow, QApplication,QMessageBox, QInputDialog )
from cirle import Ui_MainWindow

# class Example(QMainWindow):
#     def __init__(self):
#         super(Example, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)

class Example(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.comput)
        # self.radiustextEdit.textEdited.connect(self.comput)
        self.radiustextEdit.returnPressed.connect(self.comput)
    def comput(self):
       try:
           result2 = math.pi * math.pow(float(self.radiustextEdit.text()), 2)
           self.arealabel.setText(str(result2))
           text = self.radiustextEdit.text()
           self.textBrowser.append("%s = <b>%s</b>" % (text,eval(text)))
       except ValueError:
           self.radiustextEdit.clear()
           QMessageBox.warning(self,'warning', '请输入数值',QMessageBox.StandardButtons(QMessageBox.Ok))
       except:
           traceback.print_exc()
    def msg(self):
        item = ['AT', 'MES', "IS", "DA"]
        result1, ok = QInputDialog.getItem(self, ("Item输入框"),("请输入或选择"), item,1,True)
        print(result1,ok)
        result = QMessageBox.warning(self,("警告"), ("fanhui判断"),
        QMessageBox.StandardButtons(QMessageBox.Ok | QMessageBox.No))
        if result:
            print('yes')
        else:
            print('no')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # widget = QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(widget)
    # widget.show()
    ex = Example()
    ex.show()
    sys.exit(app.exec_())