import sys, cv2, time

from beauty_score import Ui_dialog

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFileDialog,QTabWidget 

from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt

from PyQt5.QtGui import QPixmap, QImage

from PyQt5.QtWidgets import QLabel,QWidget


class MyWindow(Qbeauty_score, Ui_beauty_score):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Mywindow()
    window.show()
    sys.exit(app.exec_())
