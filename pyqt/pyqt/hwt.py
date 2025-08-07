from PyQt5 import QtWidgets as qw
import sys

class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.setGeometry(300, 300, 300, 200)  # Made window larger so labels fit
        self.ui()

    def ui(self):
        # Create QLabel and assign the parent as 'self' so it shows on the window
        t1 = qw.QLabel("Hello World", self)
        t1.move(20, 20)  # Position of the first label

        t2 = qw.QLabel("How are you", self)
        t2.move(20, 60)  # Position of the second label

def main():
    app = qw.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    