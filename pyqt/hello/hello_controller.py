import sys
from PyQt5 import QtWidgets

import hello


class HelloController(QtWidgets.QMainWindow, hello.Ui_Main):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.labelMessage.setVisible(False)

        self.pushButtonSave.clicked.connect(self.on_click_save)

    def on_click_save(self):
        self.labelMessage.setVisible(True)
        self.labelMessage.setText(f'Hello {self.lineEdit.text()}')
        self.lineEdit.clear()


app = QtWidgets.QApplication(sys.argv)
window = HelloController()
window.show()
sys.exit(app.exec_())
