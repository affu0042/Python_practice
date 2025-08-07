from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui
import sys

class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello world ")
        self.setGeometry(0,0,500,500)
        self.image = QtGui.QPixmap(r'C:\Users\OMOLP76\Desktop\python\pygame_practice\car-racing-4394450_1280.jpg')

        self.text1 = qw.QLabel("",self)
        self.text1.resize(200,200)
        self.text1.setScaledContents(True)
        self.text1.setPixmap(self.image)

def main():
    app = qw.QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()