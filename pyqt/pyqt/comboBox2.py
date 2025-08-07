from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys

font = QtGui.QFont('Times', 20)

class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("CheckBox Example")

        self.box1 = qw.QCheckBox("One", self)
        self.box1.move(80, 80)
        self.box1.setFont(font)

        self.box2 = qw.QCheckBox("Two", self)
        self.box2.move(200, 80)
        self.box2.setFont(font)

        self.button = qw.QPushButton("Check", self)
        self.button.move(150, 150)
        self.button.clicked.connect(self.f)

        self.text = qw.QLabel("", self)
        self.text.setFont(font)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setGeometry(100, 220, 300, 50)  # Proper size and position

    def f(self):
        s1 = self.box1.isChecked()
        s2 = self.box2.isChecked()
        if s1 and s2:
            self.text.setText("Success")
        else:
            self.text.setText("Fails")

def main():
    app = qw.QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
