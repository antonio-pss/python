# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(805, 401)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget_list = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_list.setMaximumSize(QtCore.QSize(100000, 16777215))
        self.tableWidget_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_list.setAlternatingRowColors(True)
        self.tableWidget_list.setObjectName("tableWidget_list")
        self.tableWidget_list.setColumnCount(4)
        self.tableWidget_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_list.setHorizontalHeaderItem(3, item)
        self.tableWidget_list.horizontalHeader().setVisible(True)
        self.tableWidget_list.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_list.horizontalHeader().setHighlightSections(True)
        self.tableWidget_list.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_list.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_list.verticalHeader().setVisible(True)
        self.tableWidget_list.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_list.verticalHeader().setHighlightSections(True)
        self.tableWidget_list.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_list.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget_list)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "list"))
        item = self.tableWidget_list.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Nome:"))
        item = self.tableWidget_list.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Sexo:"))
        item = self.tableWidget_list.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Salario:"))
        item = self.tableWidget_list.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Cargo:"))
