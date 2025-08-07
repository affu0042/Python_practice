from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui
import sys

font = QtGui.QFont("times",20)

class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("Grid Layout")
        self.ui()
    
    def ui(self):
        self.grid = qw.QGridLayout()
        self.btn1 = qw.QPushButton("1")
        self.btn1.setFont(font)
        self.btn2 = qw.QPushButton("2")
        self.btn2.setFont(font)
        self.btn3 = qw.QPushButton("3")
        self.btn3.setFont(font)
        self.btn4 = qw.QPushButton("4")
        self.btn4.setFont(font)
    
        self.grid.addWidget(self.btn1,0,0)
        self.grid.addWidget(self.btn2,0,1)
        self.grid.addWidget(self.btn3,1,0)
        self.grid.addWidget(self.btn4,1,1)

        self.setLayout(self.grid)

def main():
    app = qw.QApplication([])
    w = Window()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()