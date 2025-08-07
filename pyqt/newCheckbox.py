from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui
import sys

font = QtGui.QFont("times",20)
class window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CheckBox")
        self.setGeometry(100,100,500,500)
        self.ui()

    def ui(self):
        self.box = qw.QCheckBox('check me ', self)
        self.box.setFont(font)
        self.box.setChecked(True)
        self.box.stateChanged.connect(self.state_change)
    def state_change(self,s):
        print(s)

def main():
    app = qw.QApplication([])
    w = window()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()