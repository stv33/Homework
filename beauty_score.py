# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beauty_score.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(486, 398)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 310, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 90, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(30, 70, 281, 201))
        self.label.setText("")
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(330, 150, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 200, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(dialog)
       # self.buttonBox.accepted.connect(dialog.accept)
      #  self.buttonBox.rejected.connect(dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.pushButton.setText(_translate("dialog", "Beauty Score"))
        self.pushButton_2.setText(_translate("dialog", "reset"))


