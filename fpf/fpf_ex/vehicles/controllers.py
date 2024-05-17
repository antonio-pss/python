from PyQt5 import QtWidgets
import sys

import add
import average_price
import list_all
import list_brand
import list_model
import main


class MainController(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.pushButton_add.clicked.connect(self.on_click_add)
        self.pushButton_list.clicked.connect(self.on_click_list_all)
        self.pushButton_list_brand.clicked.connect(self.on_click_list_brand)
        self.pushButton_list_model.clicked.connect(self.on_click_list_model)
        self.pushButton_average.clicked.connect(self.on_click_average )

    @staticmethod
    def on_click_add():
        dialog = AddController()
        dialog.exec_()

    @staticmethod
    def on_click_list_all():
        dialog = ListController()
        dialog.exec_()

    @staticmethod
    def on_click_list_brand():
        dialog = ListBrand()
        dialog.exec_()

    @staticmethod
    def on_click_list_model():
        dialog = ListModel()
        dialog.exec_()

    @staticmethod
    def on_click_average():
        dialog = Average()
        dialog.exec_()


class AddController(QtWidgets.QDialog, add.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


class ListController(QtWidgets.QDialog, list_all.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


class ListModel(QtWidgets.QDialog, list_model.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


class ListBrand(QtWidgets.QDialog, list_brand.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


class Average(QtWidgets.QDialog, average_price.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
main = MainController()
main.show()
sys.exit(app.exec_())

