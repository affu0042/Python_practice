from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui
import sys

font = QtGui.QFont("times", 20)

class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.setWindowTitle("Combo Box")
        self.ui()
    
    def ui(self):
        self.box = qw.QComboBox(self)
        self.box.setFont(font)
        self.box.addItems(['apple','orange','mosambi','banana'])
        self.box.currentIndexChanged.connect(self.ab)
    def ab(self, a):
        print(a)
def main():
    app = qw.QApplication([])
    w = Window()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()