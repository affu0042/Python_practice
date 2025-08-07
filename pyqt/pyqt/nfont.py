from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui 
import sys

font = QtGui.QFont('times',30)
class Window(qw.QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello Public")
        self.setGeometry(0,0,400,400)
        self.text1 = qw.QLabel("Affan Shaikh",self)
        self.text1.setFont(font)
        self.text1.move(120,120)

        self.text2 = qw.QLabel("Affan Shaikh",self)
        self.text2.setFont(font)
        self.text2.move(200,220)

def main():
    app = qw.QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()