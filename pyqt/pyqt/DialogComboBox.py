from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui
from PyQt5 import QtCore

font = QtGui.QFont("times", 15)

class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Check')
        self.setGeometry(350, 350, 500, 500)

        # Combo Box 1
        self.combo1 = qw.QComboBox(self)
        self.combo1.addItems(['mango', 'banana', 'apple', 'mosambi'])
        self.combo1.move(0, 100)

        # Combo Box 2
        self.combo2 = qw.QComboBox(self)
        self.combo2.addItems(['mango', 'banana', 'apple', 'mosambi'])
        self.combo2.move(0, 200)

        # Button
        self.btn1 = qw.QPushButton('Check', self)
        self.btn1.move(110, 220) 
        self.btn1.clicked.connect(self.clic)

        # Label
        self.text = qw.QLabel("", self)
        self.text.setFont(font)
        # self.text.setAlignment(QtCore.Qt.AlignLeft)
        self.text.resize(300, 50)
        self.text.move(100, 300)

    def clic(self):
        self.t1 = self.combo1.currentText()
        self.t2 = self.combo2.currentText()
        if self.t1 == self.t2:
            self.text.setText('Both selections are the same!')
        else:
            self.text.setText('Selections are different.')

# Run the application
app = qw.QApplication([])
w = Window()
w.show()
app.exec_()
