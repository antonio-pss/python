# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'total_role.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(222, 277)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget_total_role = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_total_role.setObjectName("tableWidget_total_role")
        self.tableWidget_total_role.setColumnCount(2)
        self.tableWidget_total_role.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_total_role.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_total_role.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tableWidget_total_role)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "total_role"))
        item = self.tableWidget_total_role.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Cargo"))
        item = self.tableWidget_total_role.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Total Salário"))