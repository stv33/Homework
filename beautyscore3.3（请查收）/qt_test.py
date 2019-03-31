import sys, cv2, time
from beauty_score import Ui_dialog
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QHBoxLayout,QLabel
from PyQt5.QtGui import QPixmap
import requests
from bs4 import BeautifulSoup
import os
import json
import base64
from judge import Face,judging



#GUI
class MyWindow(QMainWindow,Ui_dialog):
    def __init__(self,parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui= Ui_dialog()    
    ui.setupUi(MainWindow)
    ui.Botton_use(MainWindow)
    MainWindow.show()
    ui.show_img_in_label_center("cover.jpg")
    sys.exit(app.exec_())
