import threading

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

import HandTrackingModule


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self):
        g = HandTrackingModule.main()
        t = threading.Thread(target=g.start)
        t.start()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Tech With Tim")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me!")
        self.b1.clicked.connect(self.button_clicked)

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()