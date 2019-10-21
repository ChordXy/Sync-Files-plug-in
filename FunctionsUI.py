import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json
import os


class setupUIFunctions():
    def __init__(self, Window):
        self.Window = Window
        # 建立UI功能
        self.setupUIFunctions()

    def setupUIFunctions(self):
        self.InitEnvironment()
        self.InitStyle()
        self.connectSignals2Slots()

    def InitEnvironment(self):
        pass

    def InitStyle(self):
        # 按钮样式
        self.Window.pushButton_add.setStyleSheet("QPushButton{border-image: url(:/Icons/Resources/Add-5.png);}"
            "QPushButton:hover{border-image: url(:/Icons/Resources/Add-5-hover.png);}"
            "QPushButton:pressed{border-image: url(:/Icons/Resources/Add-5-press.png);}")

        self.Window.pushButton_Delete.setStyleSheet("QPushButton{border-image: url(:/Icons/Resources/Trashbin-2.png);}"
            "QPushButton:hover{border-image: url(:/Icons/Resources/Trashbin-2-hover.png);}"
            "QPushButton:pressed{border-image: url(:/Icons/Resources/Trashbin-2-press.png);}")

        self.Window.pushButton_PageUp.setStyleSheet("QPushButton{border-image: url(:/Icons/Resources/ArrowLeft.png);}"
            "QPushButton:hover{border-image: url(:/Icons/Resources/ArrowLeft-hover.png);}"
            "QPushButton:pressed{border-image: url(:/Icons/Resources/ArrowLeft-press.png);}")

        self.Window.pushButton_PageDown.setStyleSheet("QPushButton{border-image: url(:/Icons/Resources/ArrowRight.png);}"
            "QPushButton:hover{border-image: url(:/Icons/Resources/ArrowRight-hover.png);}"
            "QPushButton:pressed{border-image: url(:/Icons/Resources/ArrowRight-press.png);}")

        self.Window.pushButton_OpenSrouce.setStyleSheet("QPushButton{border-image: url(:/Icons/Resources/File.png);}"
            "QPushButton:hover{border-image: url(:/Icons/Resources/File-hover.png);}"
            "QPushButton:pressed{border-image: url(:/Icons/Resources/File-press.png);}")

        self.Window.pushButton_OpenDestiny.setStyleSheet("QPushButton{border-image: url(:/Icons/Resources/File.png);}"
            "QPushButton:hover{border-image: url(:/Icons/Resources/File-hover.png);}"
            "QPushButton:pressed{border-image: url(:/Icons/Resources/File-press.png);}")

    def connectSignals2Slots(self):
        # 添加
        self.Window.pushButton_add.clicked.connect(self.AddNewSyncPair)
        # 删除
        self.Window.pushButton_Delete.clicked.connect(self.DeleteSyncPair)
        # 上一页
        self.Window.pushButton_PageUp.clicked.connect(self.DoPageUp)
        # 下一页
        self.Window.pushButton_PageDown.clicked.connect(self.DoPageDown)
        # 上传
        self.Window.pushButton_Uploads.clicked.connect(self.SyncUpload)
        # 下载
        self.Window.pushButton_Downloads.clicked.connect(self.SyncDownload)
        # 打开源文件夹
        self.Window.pushButton_OpenSrouce.clicked.connect(self.getSrcDirectory)
        # 打开目标文件夹
        self.Window.pushButton_OpenDestiny.clicked.connect(self.getDstDirectory)
        
        # 退出
        self.Window.pushButton_Quit.clicked.connect(lambda:self.QuitThisApp())

        
    def QuitThisApp(self):
        self.Window.close()
    
    def AddNewSyncPair(self):
        print("Yes")

    def DeleteSyncPair(self):
        print("Yes")

    def DoPageUp(self):
        print("Yes")

    def DoPageDown(self):
        print("Yes")

    def SyncUpload(self):
        print("Yes")

    def SyncDownload(self):
        print("Yes")

    def getSrcDirectory(self):
        print("Yes")

    def getDstDirectory(self):
        print("Yes")



 