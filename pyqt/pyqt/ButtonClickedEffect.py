from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui
import sys

class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Clicked Effect.")
        self.setGeometry(100,100,500,500)
        self.x = 200
        self.y = 200
        self.w = 200
        self.h = 50
        self.font_size = 15

        self.text1 = qw.QLabel("Omotec", self)
        self.text1.setFont(QtGui.QFont("times",self.font_size))
        self.text1.move(self.x,self.y)
        self.text1.resize(self.w,self.h)

        self.button = qw.QPushButton("Click",self)
        self.button.clicked.connect(self.func)

    def func(self):
        # Update position, size, and font
        self.x -= 2
        self.y -= 1
        self.w += 1
        self.h += 1
        self.font_size += 1

        self.text1.setFont(QtGui.QFont("times", self.font_size))
        self.text1.setGeometry(self.x, self.y, self.w, self.h)
def main():
    app = qw.QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()