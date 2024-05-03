# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: gray\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setMaximumSize(QtCore.QSize(16777215, 150))
        self.widget_8.setObjectName("widget_8")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget_8)
        self.widget_5.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_cargo = QtWidgets.QLabel(self.widget_5)
        self.label_cargo.setMaximumSize(QtCore.QSize(16777215, 1000000))
        self.label_cargo.setStyleSheet("color: white;\n"
"font: bold 11pt \"Arial\";")
        self.label_cargo.setObjectName("label_cargo")
        self.verticalLayout_3.addWidget(self.label_cargo)
        self.comboBox_cargo = QtWidgets.QComboBox(self.widget_5)
        self.comboBox_cargo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Arial\";")
        self.comboBox_cargo.setObjectName("comboBox_cargo")
        self.comboBox_cargo.addItem("")
        self.comboBox_cargo.setItemText(0, "")
        self.comboBox_cargo.addItem("")
        self.comboBox_cargo.addItem("")
        self.comboBox_cargo.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_cargo)
        self.gridLayout.addWidget(self.widget_5, 2, 1, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.widget_8)
        self.widget_4.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_salario = QtWidgets.QLabel(self.widget_4)
        self.label_salario.setStyleSheet("color: white;\n"
"font: bold 11pt \"Arial\";")
        self.label_salario.setObjectName("label_salario")
        self.verticalLayout_7.addWidget(self.label_salario)
        self.lineEdit_salario = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_salario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Arial\";")
        self.lineEdit_salario.setObjectName("lineEdit_salario")
        self.verticalLayout_7.addWidget(self.lineEdit_salario)
        self.gridLayout.addWidget(self.widget_4, 2, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.widget_8)
        self.widget_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_name = QtWidgets.QLabel(self.widget_2)
        self.label_name.setStyleSheet("color: white;\n"
"font: bold 11pt \"Arial\";")
        self.label_name.setObjectName("label_name")
        self.verticalLayout_6.addWidget(self.label_name)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_name.setMaximumSize(QtCore.QSize(300, 20))
        self.lineEdit_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Arial\";")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout_6.addWidget(self.lineEdit_name)
        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.widget_8)
        self.widget_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_sexo = QtWidgets.QLabel(self.widget_3)
        self.label_sexo.setStyleSheet("color: white;\n"
"font: bold 11pt \"Arial\";")
        self.label_sexo.setObjectName("label_sexo")
        self.verticalLayout_4.addWidget(self.label_sexo)
        self.comboBox_sex = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_sex.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Arial\";")
        self.comboBox_sex.setObjectName("comboBox_sex")
        self.comboBox_sex.addItem("")
        self.comboBox_sex.setItemText(0, "")
        self.comboBox_sex.addItem("")
        self.comboBox_sex.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_sex)
        self.gridLayout.addWidget(self.widget_3, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setMaximumSize(QtCore.QSize(10000000, 50))
        self.widget_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_salvar = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_salvar.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_salvar.setStyleSheet("background-color: white;\n"
"font: 11pt \"Arial\";")
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        self.horizontalLayout_2.addWidget(self.pushButton_salvar)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setMaximumSize(QtCore.QSize(100000, 50))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_listar = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_listar.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_listar.setStyleSheet("background-color: white;\n"
"font: 11pt \"Arial\";")
        self.pushButton_listar.setObjectName("pushButton_listar")
        self.horizontalLayout.addWidget(self.pushButton_listar)
        self.pushButton_total_sexo = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_total_sexo.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_total_sexo.setStyleSheet("background-color: white;\n"
"font: 11pt \"Arial\";")
        self.pushButton_total_sexo.setObjectName("pushButton_total_sexo")
        self.horizontalLayout.addWidget(self.pushButton_total_sexo)
        self.pushButton_cargo = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_cargo.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_cargo.setStyleSheet("background-color: white;\n"
"font: 11pt \"Arial\";")
        self.pushButton_cargo.setObjectName("pushButton_cargo")
        self.horizontalLayout.addWidget(self.pushButton_cargo)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main"))
        self.label_cargo.setText(_translate("MainWindow", "Cargo:"))
        self.comboBox_cargo.setItemText(1, _translate("MainWindow", "Desenvolvedor"))
        self.comboBox_cargo.setItemText(2, _translate("MainWindow", "Designer"))
        self.comboBox_cargo.setItemText(3, _translate("MainWindow", "Analista de Testes"))
        self.label_salario.setText(_translate("MainWindow", "Salário:"))
        self.label_name.setText(_translate("MainWindow", "Nome:"))
        self.label_sexo.setText(_translate("MainWindow", "Sexo:"))
        self.comboBox_sex.setItemText(1, _translate("MainWindow", "Masculino"))
        self.comboBox_sex.setItemText(2, _translate("MainWindow", "Feminino"))
        self.pushButton_salvar.setText(_translate("MainWindow", "Salvar"))
        self.pushButton_listar.setText(_translate("MainWindow", "Listar"))
        self.pushButton_total_sexo.setText(_translate("MainWindow", "Total Salário Sexo"))
        self.pushButton_cargo.setText(_translate("MainWindow", "Total Salário Cargo"))
