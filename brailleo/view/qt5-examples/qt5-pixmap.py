import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                    QLabel, QApplication)
from PyQt5.QtGui import QPixmap


class Pixmap(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("redrock.png")

        lb1 = QLabel(self)
        lb1.setPixmap(pixmap)

        hbox.addWidget(lb1)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    px = Pixmap()
    sys.exit(app.exec_())
