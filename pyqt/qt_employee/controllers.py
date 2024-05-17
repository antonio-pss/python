import sys
from PyQt5 import QtWidgets

import list
import main_window
import total_role
import total_sex


class MainController(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.pushButton_salvar.clicked.connect(self.on_click_save)
        self.pushButton_listar.clicked.connect(self.on_click_list)
        self.pushButton_total_sexo.clicked.connect(self.on_click_total_sex)
        self.pushButton_cargo.clicked.connect(self.on_click_total_role)

    def on_click_save(self):
        file = open('employees.txt', 'a')
        line = self.lineEdit_name.text() + ";" + self.comboBox_sex.currentText() + ";"
        line += self.lineEdit_salario.text() + ";" + self.comboBox_cargo.currentText() + "\n"

        self.lineEdit_name.clear()
        self.lineEdit_salario.clear()
        self.comboBox_cargo.clear()
        self.comboBox_sex.clear()

        file.write(line)
        file.close()

    @staticmethod
    def on_click_list():
        dialog = ListController()
        dialog.exec_()

    @staticmethod
    def on_click_total_sex():
        dialog = TotalSexController()
        dialog.exec_()

    @staticmethod
    def on_click_total_role():
        dialog = TotalRoleController()
        dialog.exec_()


class ListController(QtWidgets.QDialog, list.Ui_Dialog):
    width_column = {
        0: 300,
        1: 100,
        2: 100,
        3: 200
    }

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.populate_table()
        self.resize_columns()

    def resize_columns(self):
        for k, v in self.width_column.items():
            self.tableWidget_list.setColumnWidth(k, v)

    def populate_table(self):
        file = open('employees.txt', 'r')
        lines = file.readlines()
        columns = []
        for line in lines:
            columns.append(line.split(';'))

        self.tableWidget_list.setRowCount(len(columns))
        for index, column in enumerate(columns):
            name = QtWidgets.QTableWidgetItem()
            name.setText(column[0])
            self.tableWidget_list.setItem(index, 0, name)

            sex = QtWidgets.QTableWidgetItem()
            sex.setText(column[1])
            self.tableWidget_list.setItem(index, 1, sex)

            sal = QtWidgets.QTableWidgetItem()
            sal.setText(column[2])
            self.tableWidget_list.setItem(index, 2, sal)

            role = QtWidgets.QTableWidgetItem()
            role.setText(column[3])
            self.tableWidget_list.setItem(index, 3, role)

        file.close()


class TotalSexController(QtWidgets.QDialog, total_sex.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.populate_list()

    def populate_list(self):
        file = open('employees.txt', 'r')
        lines = file.readlines()
        columns = []

        total_male = 0.0
        total_female = 0.0

        for line in lines:
            columns.append(line.split(';'))

        for column in columns:
            if column[1] == 'Masculino':
                total_male += float(column[2])
            elif column[1] == 'Feminino':
                total_female += float(column[2])

        self.label_homens_sal.setText(str(total_male))
        self.label_mulheres_sal.setText(str(total_female))

        file.close()


class TotalRoleController(QtWidgets.QDialog, total_role.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.populate_table()

    def populate_table(self):
        file = open('employees.txt', 'r')
        lines = file.readlines()
        columns = []
        for line in lines:
            columns.append(line.split(';'))

        total_role_desenvolvedor = 0.0
        total_role_designer = 0.0
        total_role_analista = 0.0

        self.tableWidget_total_role.setRowCount(3)
        self.tableWidget_total_role.setItem(0, 0, QtWidgets.QTableWidgetItem('Desenvolvedor'))
        self.tableWidget_total_role.setItem(1, 0, QtWidgets.QTableWidgetItem('Designer'))
        self.tableWidget_total_role.setItem(2, 0, QtWidgets.QTableWidgetItem('Analista de Testes'))

        for index, column in enumerate(columns):
            if column[3] == 'Desenvolvedor\n':
                total_role_desenvolvedor += float(column[2])
            elif column[3] == 'Designer\n':
                total_role_designer += float(column[2])
            elif column[3] == 'Analista de Testes\n':
                total_role_analista += float(column[2])

        self.tableWidget_total_role.setItem(0, 1, QtWidgets.QTableWidgetItem(str(total_role_desenvolvedor)))
        self.tableWidget_total_role.setItem(1, 1, QtWidgets.QTableWidgetItem(str(total_role_designer)))
        self.tableWidget_total_role.setItem(2, 1, QtWidgets.QTableWidgetItem(str(total_role_analista)))

        file.close()


app = QtWidgets.QApplication(sys.argv)
main = MainController()
main.show()
sys.exit(app.exec_())
