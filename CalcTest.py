import sys
import random

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

import MainWindowUi

def mkitem(a, b, f):
    x = random.randint(10 ** (a - 1), 10 ** a - 1)
    y = random.randint(10 ** (b - 1), 10 ** b - 1)
    if f == 0:
        x = int(x / y) * y
        if x < 10 ** (a - 1):
            x = int(x / y + 1) * y
        r = int(x / y)
        s = 0
    else:
        r = int(x / y)
        s = x - y * r
    return [x, y, r, s]

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = MainWindowUi.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.bg = QButtonGroup()
        self.ui.bg.addButton(self.ui.radioButton)
        self.ui.bg.addButton(self.ui.radioButton_2)
        self.ui.pushButton.clicked.connect(self.submit)
        self.setWindowTitle('CalcTest')
        self.show()

    def submit(self):
        if self.ui.radioButton.isChecked():
            f = 1
        else:
            f = 0
        result_window = ResultWindow(self.ui.spinBox_2.value(),
                self.ui.spinBox.value(), self.ui.spinBox_3.value(), f)
        winlist.append(result_window)

class ResultWindow(QTableWidget):
    def __init__(self, a, b, l, f):
        super(ResultWindow, self).__init__()
        self.resize(400, 600)
        theaders = ['問題', '答']
        self.clear()
        self.setRowCount(l)
        self.setColumnCount(len(theaders))
        self.setHorizontalHeaderLabels(theaders)
        for i in range(l):
            r = mkitem(a, b, f)
            s = str(r[0]) + ' ÷ ' + str(r[1])
            item = QTableWidgetItem(s)
#            item.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter)
            self.setItem(i, 0, item)
            s = str(r[2])
            if f == 1 and r[3] != 0:
                s = s + ' あまり ' + str(r[3])
            item = QTableWidgetItem(s)
#            item.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter)
            self.setItem(i, 1, item)
        self.setWindowTitle('作成された問題')
        self.show()

if __name__ == '__main__':
    winlist = []
    app = QApplication(sys.argv)
    main_window = MainWindow()
    winlist.append(main_window)
    sys.exit(app.exec_())
