import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                        QComboBox, QApplication)


class ComboBox(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.lb1 = QLabel("Ubuntu", self)

        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.lb1.move(50, 150)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):

        self.lb1.setText(text)
        self.lb1.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    cb = ComboBox()
    sys.exit(app.exec_())
