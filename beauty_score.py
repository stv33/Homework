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
        dialog.resize(1012, 644)
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(60, 70, 651, 481))
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(dialog)
        self.widget.setGeometry(QtCore.QRect(760, 180, 191, 271))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton.raise_()
        self.lcdNumber.raise_()
        self.pushButton_2.raise_()
        self.label.raise_()
        # self.pushButton.clicked.connect()

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.pushButton.setText(_translate("dialog", "Beauty Score"))
        self.pushButton_2.setText(_translate("dialog", "reset"))

    def show_img_in_lable_center( label, fname):
    #label表示要用来显示图片的那个标签~
    #fname表示事先获取到的要打开的图片文件名（含路径）
    pix_map = QPixmap(fname)
    img_w = pix_map.width()
    img_h = pix_map.height()
    lab_w = label.width()
    lab_h = label.height()
    if (img_w > lab_w) | (img_h > lab_h):
        #若图片宽高大于label宽高，则在label居中显示按图片原始比例缩放后的图片
        w_rate = float(img_w) / float(lab_w)
        h_rate = float(img_h) / float(lab_h)
        if w_rate >= h_rate:
            w = lab_w
            h = int(img_h / w_rate)
        else:
            w = int(img_w / h_rate)
            h = lab_h
    else:
        #若图片宽高都小于label宽高，则按图片原始大小显示
        w = img_w
        h = img_h
    label.setPixmap(pix_map.scaled(w, h))


