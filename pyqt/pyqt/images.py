# corrected code there is a error in PPT

from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui
import sys

class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.setGeometry(0, 0, 600, 600)  # Adjusted size for image display
        self.ui()

    def ui(self):
        pixmap = QtGui.QPixmap(r"C:\Users\OMOLP76\Desktop\python\pygame_practice\car-racing-4394450_1280.jpg")
        label = qw.QLabel(self)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())  # Optional: Resize label to fit the image

def main():
    app = qw.QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
