import sys
from PyQt5.QtWidgets import QApplication, QWidget


app = QApplication(sys.argv)

window = QWidget()
window.resize(250, 150)
window.move(300, 300)
window.setWindowTitle('brailleo')
window.show()


sys.exit(app.exec_())
