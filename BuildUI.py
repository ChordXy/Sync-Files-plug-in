import sys
import ctypes
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from FastSyncUI import Ui_MainWindow
import FunctionsUI


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("快捷同步")
        self.setWindowIcon(QIcon('./Resources/online-conference.png'))


        FunctionsUI.setupUIFunctions(self)
 

if __name__ == "__main__":
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)
        ctypes.windll.kernel32.CloseHandle(whnd)
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

    