import sys, cv2, time

from beauty_score import Ui_dialog

from PyQt5.QtWidgets import QApplication,QMainWindow




class MyWindow(QMainWindow,Ui_dialog):
    def __init__(self,parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui= Ui_dialog()    
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
