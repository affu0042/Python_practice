from PyQt5 import QtWidgets as qw
import sys

class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Push Button practice...")
        self.setGeometry(0,0,500,500)
        self.ui()
    def ui(self):
        self.text1 = qw.QLabel("Hello worlf", self)
        self.button = qw.QPushButton("enter",self)
        # self.button.move(200,200)
        # self.button.setGeometry(250,250,100,100)
        self.button.setStyleSheet("background-color: blue; color:white; width:150px;height:80px;border-radius:5px; margin:100px 100px;")
        self.button.clicked.connect(self.func)
    def func(self):
        self.text1.setText("button is Clickcd")
        self.text1.resize(200,50)
        self.button.setText("button is Clickcd")
        self.setDisabled(True)
        
def main():
    app = qw.QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()