# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FirstWindow(object):
    def setupUi(self, FirstWindow):
        FirstWindow.setObjectName("FirstWindow")
        FirstWindow.setEnabled(True)
        FirstWindow.setFixedSize(430, 350)
        self.centralwidget = QtWidgets.QWidget(FirstWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 80, 351, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 40, 171, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 120, 191, 31))
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 160, 150, 150))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(238, 161, 150, 150))
        self.label_2.setObjectName("label_2")
        FirstWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FirstWindow)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)

    def retranslateUi(self, FirstWindow):
        _translate = QtCore.QCoreApplication.translate
        FirstWindow.setWindowTitle(_translate("FirstWindow", "TicTacToe"))
        self.label_3.setText(_translate("FirstWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Enter username</span></p></body></html>"))
        self.label_4.setText(_translate("FirstWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Choose sign</span></p></body></html>"))
        self.label.setText(_translate("FirstWindow", "<html><head/><body><p><img src=\":/x/x_img.png\"/></p></body></html>"))
        self.label_2.setText(_translate("FirstWindow", "<html><head/><body><p><img src=\":/o/o_img.png\"/></p></body></html>"))

import o_rc
