from PyQt5 import QtWidgets as qw

class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello world")
        # self.setGeometry(500,500,500,300)
        self.showMaximized()

app = qw.QApplication([])
window = Window()
window.show()
app.exec_()

