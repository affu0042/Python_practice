from PyQt5 import QtWidgets as qw 

class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.setGeometry(750,400,400,300)
        text1 = qw.QLabel('Hello world',self)

app = qw.QApplication([])
window = Window()
window.show()
app.exec_()

        