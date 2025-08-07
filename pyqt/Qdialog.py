from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui
import sys
font = QtGui.QFont('times',20)

class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.setWindowTitle("Dialog box")
        self.ui()
    
    def ui(self):
        self.pushButton = qw.QPushButton('Enter',self)
        self.pushButton.move(150,150)
        self.pushButton.clicked.connect(self.abs)
    def abs(self):
        diag = qw.QDialog(self)
        diag.setWindowTitle("this is my dialog box")
        diag.exec_()
def main():
    app = qw.QApplication([])
    w = Window()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()