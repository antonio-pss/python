# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'total_sex.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(398, 186)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("background-color: gray;")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_homens = QtWidgets.QLabel(self.widget)
        self.label_homens.setMaximumSize(QtCore.QSize(100, 25))
        self.label_homens.setStyleSheet("color: white;\n"
"font: bold 11pt \"Arial\";")
        self.label_homens.setObjectName("label_homens")
        self.gridLayout.addWidget(self.label_homens, 0, 0, 1, 1)
        self.label_homens_sal = QtWidgets.QLabel(self.widget)
        self.label_homens_sal.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_homens_sal.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: bold 11pt \"Arial\";")
        self.label_homens_sal.setText("")
        self.label_homens_sal.setObjectName("label_homens_sal")
        self.gridLayout.addWidget(self.label_homens_sal, 0, 1, 1, 1)
        self.label_mulheres = QtWidgets.QLabel(self.widget)
        self.label_mulheres.setMaximumSize(QtCore.QSize(100, 25))
        self.label_mulheres.setStyleSheet("color: white;\n"
"font: bold 11pt \"Arial\";")
        self.label_mulheres.setObjectName("label_mulheres")
        self.gridLayout.addWidget(self.label_mulheres, 1, 0, 1, 1)
        self.label_mulheres_sal = QtWidgets.QLabel(self.widget)
        self.label_mulheres_sal.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_mulheres_sal.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: bold 11pt \"Arial\";")
        self.label_mulheres_sal.setText("")
        self.label_mulheres_sal.setObjectName("label_mulheres_sal")
        self.gridLayout.addWidget(self.label_mulheres_sal, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "total_sex"))
        self.label_homens.setText(_translate("Dialog", "Homens:"))
        self.label_mulheres.setText(_translate("Dialog", "Mulheres:"))
