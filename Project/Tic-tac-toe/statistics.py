# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TableList(object):
    def setupUi(self, TableList):
        TableList.setObjectName("TableList")
        TableList.setFixedSize(500, 500)
        self.centralwidget = QtWidgets.QWidget(TableList)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.ResetButton = QtWidgets.QPushButton(self.centralwidget)
        self.ResetButton.setObjectName("ResetButton")
        self.verticalLayout.addWidget(self.ResetButton)
        TableList.setCentralWidget(self.centralwidget)

        self.retranslateUi(TableList)
        QtCore.QMetaObject.connectSlotsByName(TableList)

    def retranslateUi(self, TableList):
        _translate = QtCore.QCoreApplication.translate
        TableList.setWindowTitle(_translate("TableList", "Statistics"))
        self.ResetButton.setText(_translate("TableList", "Reset"))

