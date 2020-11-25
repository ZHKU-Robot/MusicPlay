# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MusicWindow(object):
    def setupUi(self, MusicWindow):
        MusicWindow.setObjectName("MusicWindow")
        MusicWindow.resize(982, 668)
        self.verticalLayout = QtWidgets.QVBoxLayout(MusicWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(MusicWindow)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(188, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(MusicWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(225, 0, 21);\n"
"color: rgb(244, 246, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);};")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/buttonicon/MusicButtonIcon/playall.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(MusicWindow)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"\n"
"    color: rgb(17, 108, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);};")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/buttonicon/MusicButtonIcon/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.musicTable = MyMusicTable(MusicWindow)
        self.musicTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.musicTable.setAlternatingRowColors(True)
        self.musicTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.musicTable.setGridStyle(QtCore.Qt.DashDotDotLine)
        self.musicTable.setObjectName("musicTable")
        self.musicTable.setColumnCount(6)
        self.musicTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.musicTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.musicTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.musicTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.musicTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.musicTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.musicTable.setHorizontalHeaderItem(5, item)
        self.musicTable.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_2.addWidget(self.musicTable)
        self.listView = QtWidgets.QListView(MusicWindow)
        self.listView.setObjectName("listView")
        self.horizontalLayout_2.addWidget(self.listView)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(MusicWindow)
        QtCore.QMetaObject.connectSlotsByName(MusicWindow)

    def retranslateUi(self, MusicWindow):
        _translate = QtCore.QCoreApplication.translate
        MusicWindow.setWindowTitle(_translate("MusicWindow", "Music"))
        self.label.setText(_translate("MusicWindow", "本地音乐"))
        self.label_2.setText(_translate("MusicWindow", "共1首"))
        self.pushButton.setText(_translate("MusicWindow", "播放全部"))
        self.pushButton_2.setText(_translate("MusicWindow", "添加音乐"))
        item = self.musicTable.horizontalHeaderItem(0)
        item.setText(_translate("MusicWindow", "歌名"))
        item = self.musicTable.horizontalHeaderItem(1)
        item.setText(_translate("MusicWindow", "歌手"))
        item = self.musicTable.horizontalHeaderItem(2)
        item.setText(_translate("MusicWindow", "专辑"))
        item = self.musicTable.horizontalHeaderItem(3)
        item.setText(_translate("MusicWindow", "时长"))
        item = self.musicTable.horizontalHeaderItem(4)
        item.setText(_translate("MusicWindow", "大小"))
        item = self.musicTable.horizontalHeaderItem(5)
        item.setText(_translate("MusicWindow", "路径"))

from MyMusicTable import MyMusicTable
import res_rc
