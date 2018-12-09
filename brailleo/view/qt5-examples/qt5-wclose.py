import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class CWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        qbutton = QPushButton('Quit', self)
        qbutton.clicked.connect(QApplication.instance().quit)
        qbutton.resize(qbutton.sizeHint())
        qbutton.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    cw = CWindow()
    sys.exit(app.exec_())
