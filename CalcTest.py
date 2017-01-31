import sys
import random

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

import MainWindowUi

def f(i, v):
    if i < v:
        return 1
    else:
        return 0

def randsort_f(l, v):
    a = [0] * l
    for i in range(l):
        j = random.randint(0, i)
        if j != i:
            a[i] = a[j]
        a[j] = f(i, v)
    return a

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
        self.ui.bg.addButton(self.ui.radioButton_3)
        self.ui.horizontalSlider.setEnabled(False)
        self.ui.spinBox_4.setEnabled(False)
        self.ui.radioButton.clicked.connect(self.changeChecked)
        self.ui.radioButton_2.clicked.connect(self.changeChecked)
        self.ui.radioButton_3.clicked.connect(self.changeChecked)
        self.ui.horizontalSlider.valueChanged[int].connect(self.changeValueSlider)
        self.ui.spinBox_4.valueChanged[int].connect(self.changeValueSpinBox)
        self.ui.spinBox_3.setRange(0, 100)
        self.ui.spinBox_3.valueChanged[int].connect(self.changeValueNum)
        self.ui.pushButton.clicked.connect(self.submit)
        self.setWindowTitle('CalcTest')
        self.show()

    def changeChecked(self):
        if self.ui.radioButton_3.isChecked():
            self.ui.horizontalSlider.setEnabled(True)
            self.ui.spinBox_4.setEnabled(True)
        else:
            self.ui.horizontalSlider.setEnabled(False)
            self.ui.spinBox_4.setEnabled(False)

    def changeValueSlider(self, value):
        if self.ui.radioButton_3.isChecked():
            self.ui.spinBox_4.setValue(value)

    def changeValueSpinBox(self, value):
        if self.ui.radioButton_3.isChecked():
            self.ui.horizontalSlider.setValue(value)

    def changeValueNum(self, value):
        self.ui.horizontalSlider.setRange(0, value)
        self.ui.spinBox_4.setRange(0, value)

    def submit(self):
        if self.ui.radioButton.isChecked():
            f = 1
        elif self.ui.radioButton_2.isChecked():
            f = 0
        else:
            f = 2
        result_window = ResultWindow(self.ui.spinBox_2.value(),
                self.ui.spinBox.value(), self.ui.spinBox_3.value(), f,
                self.ui.horizontalSlider.value())
        winlist.append(result_window)

class ResultWindow(QTextEdit):
    def __init__(self, a, b, l, f, v):
        super(ResultWindow, self).__init__()
        self.resize(400, 600)
        if f == 2:
            far = randsort_f(l, v)
        else:
            far = [f] * l
        for i in range(l):
            r = mkitem(a, b, far[i])
            s = '(' + str(i) + ')    '
            s = s + str(r[0]) + ' ÷ ' + str(r[1])
            s = s + '  =  ' + str(r[2])
            if far[i] == 1 and r[3] != 0:
                s = s + '  あまり  ' + str(r[3])
            self.append(s)
        self.setWindowTitle('作成された問題')
        self.show()

if __name__ == '__main__':
    winlist = []
    app = QApplication(sys.argv)
    main_window = MainWindow()
    winlist.append(main_window)
    sys.exit(app.exec_())
