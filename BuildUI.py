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

        # 系统托盘区设置
        self.TraySettings()
        FunctionsUI.setupUIFunctions(self)

    def TraySettings(self):
        self.tray = QSystemTrayIcon(self)
        self.tray.setIcon(QIcon('./Resources/online-conference.png'))

        minimizeAction = QAction("Mi&nimize", self, triggered = self.hide)
        restoreAction = QAction("&Restore", self, triggered = self.showNormal)
        quitAction = QAction("&Quit", self, triggered = QApplication.instance().quit)
        self.trayMenu = QMenu(self)
        self.trayMenu.addAction(minimizeAction)
        self.trayMenu.addAction(restoreAction)
        self.trayMenu.addSeparator()
        self.trayMenu.addAction(quitAction)
        self.tray.setContextMenu(self.trayMenu)
        self.tray.show()
        self.tray.activated.connect(self.IconClicked)

    def IconClicked(self, reason):
        """
            鼠标点击icon传递的信号会带有一个整形的值
            1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
        """
        if reason == 2 or reason == 3:
            if self.isVisible():
                self.hide()
            else:
                self.show()

    def closeEvent(self, event):
        event.ignore()  # 忽略关闭事件
        self.hide()     # 隐藏窗体

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

    