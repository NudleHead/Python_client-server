# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoLogin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(638, 501)
        self.labelLogin = QtWidgets.QLabel(Dialog)
        self.labelLogin.setEnabled(True)
        self.labelLogin.setGeometry(QtCore.QRect(100, 170, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelLogin.setFont(font)
        self.labelLogin.setObjectName("labelLogin")
        self.labelPassword = QtWidgets.QLabel(Dialog)
        self.labelPassword.setEnabled(True)
        self.labelPassword.setGeometry(QtCore.QRect(100, 240, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPassword.setFont(font)
        self.labelPassword.setObjectName("labelPassword")
        self.lineEditLogin = QtWidgets.QLineEdit(Dialog)
        self.lineEditLogin.setGeometry(QtCore.QRect(210, 180, 151, 31))
        self.lineEditLogin.setObjectName("lineEditLogin")
        self.lineEditPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditPassword.setGeometry(QtCore.QRect(210, 250, 151, 31))
        self.lineEditPassword.setFrame(True)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(390, 220, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 330, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelLogin.setText(_translate("Dialog", "Login:"))
        self.labelPassword.setText(_translate("Dialog", "Password:"))
        self.pushButton.setText(_translate("Dialog", "Sign in"))
