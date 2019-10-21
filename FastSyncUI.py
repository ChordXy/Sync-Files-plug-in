# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Chordxy\自写代码\快捷同步\FastSyncUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_Display = QtWidgets.QFrame(self.centralwidget)
        self.frame_Display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_Display.setObjectName("frame_Display")
        self.verticalLayout_4.addWidget(self.frame_Display)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_SourceDropbox = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_SourceDropbox.setFont(font)
        self.label_SourceDropbox.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SourceDropbox.setObjectName("label_SourceDropbox")
        self.horizontalLayout_2.addWidget(self.label_SourceDropbox)
        self.pushButton_OpenSrouce = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_OpenSrouce.sizePolicy().hasHeightForWidth())
        self.pushButton_OpenSrouce.setSizePolicy(sizePolicy)
        self.pushButton_OpenSrouce.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_OpenSrouce.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_OpenSrouce.setStyleSheet("border-image: url(:/Icons/Resources/File.png);")
        self.pushButton_OpenSrouce.setText("")
        self.pushButton_OpenSrouce.setObjectName("pushButton_OpenSrouce")
        self.horizontalLayout_2.addWidget(self.pushButton_OpenSrouce)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.textEdit_Display_Source = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Display_Source.setObjectName("textEdit_Display_Source")
        self.horizontalLayout_6.addWidget(self.textEdit_Display_Source)
        self.label_Display_Source = QtWidgets.QLabel(self.centralwidget)
        self.label_Display_Source.setStyleSheet("border-image: url(:/Icons/Resources/EmptyFile.png);")
        self.label_Display_Source.setText("")
        self.label_Display_Source.setObjectName("label_Display_Source")
        self.horizontalLayout_6.addWidget(self.label_Display_Source)
        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_DestinyDropbox = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_DestinyDropbox.setFont(font)
        self.label_DestinyDropbox.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DestinyDropbox.setObjectName("label_DestinyDropbox")
        self.horizontalLayout_3.addWidget(self.label_DestinyDropbox)
        self.pushButton_OpenDestiny = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_OpenDestiny.sizePolicy().hasHeightForWidth())
        self.pushButton_OpenDestiny.setSizePolicy(sizePolicy)
        self.pushButton_OpenDestiny.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_OpenDestiny.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_OpenDestiny.setStyleSheet("border-image: url(:/Icons/Resources/File.png);")
        self.pushButton_OpenDestiny.setText("")
        self.pushButton_OpenDestiny.setObjectName("pushButton_OpenDestiny")
        self.horizontalLayout_3.addWidget(self.pushButton_OpenDestiny)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.textEdit_Display_Destiny = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Display_Destiny.setObjectName("textEdit_Display_Destiny")
        self.horizontalLayout_7.addWidget(self.textEdit_Display_Destiny)
        self.label_Display_Destiny = QtWidgets.QLabel(self.centralwidget)
        self.label_Display_Destiny.setStyleSheet("border-image: url(:/Icons/Resources/EmptyFile.png);")
        self.label_Display_Destiny.setText("")
        self.label_Display_Destiny.setObjectName("label_Display_Destiny")
        self.horizontalLayout_7.addWidget(self.label_Display_Destiny)
        self.horizontalLayout_7.setStretch(0, 3)
        self.horizontalLayout_7.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_8.addWidget(self.line)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_add.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_add.setStyleSheet("border-image: url(:/Icons/Resources/Add-5.png);")
        self.pushButton_add.setText("")
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_4.addWidget(self.pushButton_add)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.pushButton_Delete = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Delete.sizePolicy().hasHeightForWidth())
        self.pushButton_Delete.setSizePolicy(sizePolicy)
        self.pushButton_Delete.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_Delete.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_Delete.setStyleSheet("border-image: url(:/Icons/Resources/Trashbin-2.png);")
        self.pushButton_Delete.setText("")
        self.pushButton_Delete.setObjectName("pushButton_Delete")
        self.horizontalLayout_4.addWidget(self.pushButton_Delete)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pushButton_PageUp = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_PageUp.sizePolicy().hasHeightForWidth())
        self.pushButton_PageUp.setSizePolicy(sizePolicy)
        self.pushButton_PageUp.setMinimumSize(QtCore.QSize(30, 15))
        self.pushButton_PageUp.setMaximumSize(QtCore.QSize(301, 15))
        self.pushButton_PageUp.setStyleSheet("border-image: url(:/Icons/Resources/ArrowLeft.png);")
        self.pushButton_PageUp.setText("")
        self.pushButton_PageUp.setObjectName("pushButton_PageUp")
        self.horizontalLayout.addWidget(self.pushButton_PageUp)
        self.label_Pages = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_Pages.setFont(font)
        self.label_Pages.setStyleSheet("color: rgb(0, 114, 240);")
        self.label_Pages.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Pages.setObjectName("label_Pages")
        self.horizontalLayout.addWidget(self.label_Pages)
        self.pushButton_PageDown = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_PageDown.sizePolicy().hasHeightForWidth())
        self.pushButton_PageDown.setSizePolicy(sizePolicy)
        self.pushButton_PageDown.setMinimumSize(QtCore.QSize(30, 15))
        self.pushButton_PageDown.setMaximumSize(QtCore.QSize(30, 15))
        self.pushButton_PageDown.setStyleSheet("border-image: url(:/Icons/Resources/ArrowRight.png);")
        self.pushButton_PageDown.setText("")
        self.pushButton_PageDown.setObjectName("pushButton_PageDown")
        self.horizontalLayout.addWidget(self.pushButton_PageDown)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.label_SyncProcess = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(10)
        self.label_SyncProcess.setFont(font)
        self.label_SyncProcess.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SyncProcess.setObjectName("label_SyncProcess")
        self.verticalLayout_3.addWidget(self.label_SyncProcess)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_Uploads = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(10)
        self.pushButton_Uploads.setFont(font)
        self.pushButton_Uploads.setObjectName("pushButton_Uploads")
        self.horizontalLayout_5.addWidget(self.pushButton_Uploads)
        self.pushButton_Downloads = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(10)
        self.pushButton_Downloads.setFont(font)
        self.pushButton_Downloads.setObjectName("pushButton_Downloads")
        self.horizontalLayout_5.addWidget(self.pushButton_Downloads)
        self.pushButton_Quit = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(10)
        self.pushButton_Quit.setFont(font)
        self.pushButton_Quit.setObjectName("pushButton_Quit")
        self.horizontalLayout_5.addWidget(self.pushButton_Quit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_SourceDropbox.setText(_translate("MainWindow", "Source Dropbox"))
        self.label_DestinyDropbox.setText(_translate("MainWindow", "Destiny Dropbox"))
        self.label_Pages.setText(_translate("MainWindow", "1 / 1"))
        self.label_SyncProcess.setText(_translate("MainWindow", "同步进度："))
        self.pushButton_Uploads.setText(_translate("MainWindow", "本地上传"))
        self.pushButton_Downloads.setText(_translate("MainWindow", "云端下载"))
        self.pushButton_Quit.setText(_translate("MainWindow", "退出"))
import MyRes_rc
