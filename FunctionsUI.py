import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json
import os


class MyButton(QPushButton, QWidget):
    def __init__(self, parent, border):
        super(MyButton, self).__init__(parent)
        self.mouse_isMoved = False
        self.PresentPosition = None
        self.tlx = border.topLeft().x()
        self.tly = border.topLeft().y()
        self.brx = border.bottomRight().x() - 110
        self.bry = border.bottomRight().y() - 110
        self.justClicked = False
        self.Selected = False
        self.setStyleSheet("QPushButton{border-image: url(:/Icons/Resources/File.png)}")
        self.setText("")
    
    def mousePressEvent(self, event):
        self.Origin_Point = event.globalPos()
        self.mouse_isMoved = True
        self.PresentPosition = self.frameGeometry().topLeft()
        self.justClicked = True
    
    def mouseReleaseEvent(self, event):
        self.mouse_isMoved = False
        sP_x = self.frameGeometry().topLeft().x() - self.tlx
        sP_y = self.frameGeometry().topLeft().y() - self.tly
        x_Position = ((sP_x - 1) // 130) * 130 + 11 + self.tlx
        y_Position = (sP_y // 118) * 120 + 3 + self.tly
        self.move(QPoint(x_Position, y_Position))
        if self.justClicked == True:
            if self.Selected == False:
                self.setStyleSheet("QPushButton{border-image: url(:/Icons/Resources/File-press.png)}")
                self.Selected = True
            else:
                self.setStyleSheet("QPushButton{border-image: url(:/Icons/Resources/File.png)}")
                self.Selected = False
    
    def mouseMoveEvent(self, event):
        if self.mouse_isMoved:
            # print("Origin Position : ", self.Origin_Point)
            # print("Present Position : ", event.globalPos())
            # print("Difference : ", event.globalPos() - self.Origin_Point)
            toMove = event.globalPos() - self.Origin_Point + self.PresentPosition
            toMove_x = toMove.x()
            toMove_y = toMove.y()
            self.justClicked = False
            if toMove_x <= self.tlx or toMove_x >= self.brx or toMove_y <= self.tly or toMove_y >= self.bry:
                return
            else:
                self.move(toMove)


class setupUIFunctions():
    def __init__(self, Window):
        self.Window = Window
        self.SrcDirectory = None
        self.DstDirectory = None
        self.setupUIFunctions()

    def setupUIFunctions(self):
        self.InitEnvironment()
        self.InitStyle()
        self.connectSignals2Slots()

    def InitEnvironment(self):
        pass

    def InitStyle(self):
        # 设置按钮样式
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

        self.Window.pushButton_SrcClear.setStyleSheet("QPushButton{border-image: url(:/Icons/Resources/EmptyFile.png);}"
            "QPushButton:hover{border-image: url(:/Icons/Resources/EmptyFile-hover.png);}"
            "QPushButton:pressed{border-image: url(:/Icons/Resources/EmptyFile-Clear.png);}")

        self.Window.pushButton_DstClear.setStyleSheet("QPushButton{border-image: url(:/Icons/Resources/EmptyFile.png);}"
            "QPushButton:hover{border-image: url(:/Icons/Resources/EmptyFile-hover.png);}"
            "QPushButton:pressed{border-image: url(:/Icons/Resources/EmptyFile-Clear.png);}")

    def connectSignals2Slots(self):
        # 增加
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
        # 打开源文件
        self.Window.pushButton_OpenSrouce.clicked.connect(self.getSrcDirectory)
        # 打开目标文件
        self.Window.pushButton_OpenDestiny.clicked.connect(self.getDstDirectory)
        # 清除源文件文本
        self.Window.pushButton_SrcClear.clicked.connect(self.ClearSrcText)
        # 清除目标文件文本
        self.Window.pushButton_DstClear.clicked.connect(self.ClearDstText)

        # 源文件文本变动
        self.Window.textEdit_Display_Source.textChanged.connect(self.SrcFileCheck)
        # 目标文件文本变动
        self.Window.textEdit_Display_Destiny.textChanged.connect(self.DstFileCheck)

        # 退出
        self.Window.pushButton_Quit.clicked.connect(lambda:self.QuitThisApp())

        
    def QuitThisApp(self):
        # 防止退出后系统托盘区图标依然存在问题
        self.Window.tray.setVisible(False)
        QApplication.instance().quit()
    
    def AddNewSyncPair(self):
        self.Window.btn = MyButton(self.Window.centralwidget, self.Window.frame_Display.frameGeometry())
        self.Window.btn.resize(110, 110)

        position = self.Window.frame_Display.frameGeometry().topLeft() + QPoint(1, 3) + QPoint(10, 0)
        self.Window.btn.move(position)
        self.Window.btn.show()


    def DeleteSyncPair(self):
        print(self.Window.frame_Display.frameGeometry())

    def DoPageUp(self):
        print("Yes")

    def DoPageDown(self):
        print("Yes")

    def SyncUpload(self):
        print("Yes")

    def SyncDownload(self):
        print("Yes")

    def getSrcDirectory(self):
        fname = QFileDialog.getExistingDirectory(self.Window, '选择路径', './')
        if os.path.exists(fname):
            self.SrcDirectory = fname
            self.Window.textEdit_Display_Source.setText(fname)
        else:
            self.Window.textEdit_Display_Source.setText("路径选择错误")

    def getDstDirectory(self):
        fname = QFileDialog.getExistingDirectory(self.Window, '选择路径', './')
        if os.path.exists(fname):
            self.SrcDirectory = fname
            self.Window.textEdit_Display_Destiny.setText(fname)
        else:
            self.Window.textEdit_Display_Destiny.setText("路径选择错误")

    def SrcFileCheck(self):
        text = self.Window.textEdit_Display_Source.toPlainText()
        text = text.replace("file:///", '')
        if os.path.exists(text):
            self.Window.pushButton_SrcClear.setStyleSheet("QPushButton{border-image: url(:/Icons/Resources/EmptyFile-OK.png);}"
                "QPushButton:hover{border-image: url(:/Icons/Resources/EmptyFile-hover.png);}"
                "QPushButton:pressed{border-image: url(:/Icons/Resources/EmptyFile-Clear.png);}")
            self.SrcDirectory = text

    def ClearSrcText(self):
        self.Window.textEdit_Display_Source.clear()
        self.Window.pushButton_SrcClear.setStyleSheet("QPushButton{border-image: url(:/Icons/Resources/EmptyFile.png);}"
            "QPushButton:hover{border-image: url(:/Icons/Resources/EmptyFile-hover.png);}"
            "QPushButton:pressed{border-image: url(:/Icons/Resources/EmptyFile-Clear.png);}")
        self.SrcDirectory = None

    def DstFileCheck(self):
        text = self.Window.textEdit_Display_Destiny.toPlainText()
        text = text.replace("file:///", '')
        if os.path.exists(text):
            self.Window.pushButton_DstClear.setStyleSheet("QPushButton{border-image: url(:/Icons/Resources/EmptyFile-OK.png);}"
                "QPushButton:hover{border-image: url(:/Icons/Resources/EmptyFile-hover.png);}"
                "QPushButton:pressed{border-image: url(:/Icons/Resources/EmptyFile-Clear.png);}")
            self.DstDirectory = text
    
    def ClearDstText(self):
        self.Window.textEdit_Display_Destiny.clear()
        self.Window.pushButton_DstClear.setStyleSheet("QPushButton{border-image: url(:/Icons/Resources/EmptyFile.png);}"
            "QPushButton:hover{border-image: url(:/Icons/Resources/EmptyFile-hover.png);}"
            "QPushButton:pressed{border-image: url(:/Icons/Resources/EmptyFile-Clear.png);}")
        self.DstDirectory = None

    def AddNewMenu(self):
        mAction = QAction("Mini&mize1", self.Window, triggered = self.Window.hide)
        self.Window.trayMenu.addAction(mAction)
        self.Window.tray.setContextMenu(self.Window.trayMenu)
        self.Window.tray.show()

 