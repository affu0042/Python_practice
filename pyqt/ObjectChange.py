import sys
from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui

font = QtGui.QFont('times',34)

class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello bantai")
        self.setGeometry(300,300,500,500)
        self.ui()
    
    def ui(self):
        self.t1 = qw.QLabel("hello world",self)
        self.t1.setFont(font)
def main():
    app = qw.QApplication([])
    window = Window()
    window.show()
    sys(app.exec_())

if __name__ == "__main__":
    main()