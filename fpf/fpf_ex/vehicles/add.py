# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(633, 105)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)
        self.lineEdit_plate = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_plate.setObjectName("lineEdit_plate")
        self.gridLayout.addWidget(self.lineEdit_plate, 1, 4, 1, 1)
        self.lineEdit_model = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_model.setObjectName("lineEdit_model")
        self.gridLayout.addWidget(self.lineEdit_model, 1, 3, 1, 1)
        self.lineEdit_color = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_color.setObjectName("lineEdit_color")
        self.gridLayout.addWidget(self.lineEdit_color, 1, 1, 1, 1)
        self.lineEdit_brand = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_brand.setObjectName("lineEdit_brand")
        self.gridLayout.addWidget(self.lineEdit_brand, 1, 0, 1, 1)
        self.lineEdit_price = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.gridLayout.addWidget(self.lineEdit_price, 1, 5, 1, 1)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Brand"))
        self.label_5.setText(_translate("Dialog", "Price"))
        self.label_2.setText(_translate("Dialog", "Color"))
        self.label_3.setText(_translate("Dialog", "Model"))
        self.label_4.setText(_translate("Dialog", "Plate"))