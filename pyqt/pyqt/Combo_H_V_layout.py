import sys
from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui
font = QtGui.QFont("times",30)
class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Combination of horizontal and vertovsl layput")
        self.setGeometry(200,200,500,500)
        self.ui()
    
    def ui(self):
        self.hbox = qw.QHBoxLayout()
        self.text1 = qw.QLabel("Hello")
        self.text1.setFont(font)

        self.text2 = qw.QLabel("World")
        self.text2.setFont(font)

        self.hbox.addWidget(self.text1)
        self.hbox.addWidget(self.text2)

        self.vbox = qw.QVBoxLayout()
        self.b1 = qw.QPushButton("button 1",self)
        self.b1.setFont(font)
        self.b2 = qw.QPushButton("button 2",self)
        self.b2.setFont(font)

        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)

        self.mainlayout = qw.QVBoxLayout()
        self.mainlayout.addLayout(self.hbox)
        self.mainlayout.addLayout(self.vbox)

        self.setLayout(self.mainlayout)

def main():
    app = qw.QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()