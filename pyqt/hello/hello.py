# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(676, 491)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labeNamel = QtWidgets.QLabel(self.widget)
        self.labeNamel.setStyleSheet("")
        self.labeNamel.setObjectName("labeNamel")
        self.verticalLayout.addWidget(self.labeNamel)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButtonSave = QtWidgets.QPushButton(self.widget)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.verticalLayout.addWidget(self.pushButtonSave)
        self.labelMessage = QtWidgets.QLabel(self.widget)
        self.labelMessage.setEnabled(True)
        self.labelMessage.setObjectName("labelMessage")
        self.verticalLayout.addWidget(self.labelMessage)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget)
        Main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)
        self.actionName = QtWidgets.QAction(Main)
        self.actionName.setObjectName("actionName")

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Hello"))
        self.labeNamel.setText(_translate("Main", "Name:"))
        self.pushButtonSave.setText(_translate("Main", "Save"))
        self.labelMessage.setText(_translate("Main", "TextLabel"))
        self.actionName.setText(_translate("Main", "Name"))