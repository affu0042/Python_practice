import sys
from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui
font = QtGui.QFont("times",20)
class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("hello world")
        self.setGeometry(750,400,400,300)
        self.ui()
    def ui(self):
        enterbtn = qw.QPushButton("enter",self)
        enterbtn.move(200,200)
        enterbtn.clicked.connect(self.func_enter)
    def func_enter(self):
        diag = qw.QDialog(self)
        QBtn = qw.QDialogButtonBox.Ok | qw.QDialogButtonBox.Cancel
        diag.setWindowTitle("Dialog Box")
        diag.buttonBox = qw.QDialogButtonBox(QBtn)
        diag.layout = qw.QVBoxLayout()
        message = qw.QLabel("Something happened, is that OK?")
        diag.layout.addWidget(message)
        diag.layout.addWidget(diag.buttonBox)
        diag.setLayout(diag.layout)
        diag.exec_()
def main():
    app = qw.QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
