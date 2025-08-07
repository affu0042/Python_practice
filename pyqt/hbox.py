import sys
from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui

font = QtGui.QFont("times", 20)
class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.setGeometry(100,100,500,500)
        self.ui()
    def ui(self):
        btn1 = qw.QPushButton("Button 1",self)
        btn1.setFont(font)
        btn2 = qw.QPushButton("Button 2",self)
        btn2.setFont(font)
        btn3 = qw.QPushButton("Button 3",self)
        btn3.setFont(font)

        hbox = qw.QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)

        self.setLayout(hbox)

def main():
    app = qw.QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
