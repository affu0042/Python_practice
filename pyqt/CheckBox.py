from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui
import sys
font = QtGui.QFont('Times',20)

class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CheckBox')
        self.setGeometry(200,200,550,550)
        
        self.box = qw.QCheckBox('check me ',self)
        self.box.setFont(font)

app = qw.QApplication([])
w = Window()
w.show()
sys.exit(app.exec_())