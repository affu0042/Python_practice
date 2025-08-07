import sys
from PyQt5 import QtWidgets as qw

class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,500,500,500)
        self.show()

app = qw.QApplication([])
window = Window()
sys.exit(app.exec_())