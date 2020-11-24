# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MusicTable.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MusicTable(object):
    def setupUi(self, MusicTable):
        MusicTable.setObjectName("MusicTable")
        MusicTable.resize(651, 463)
        MusicTable.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.verticalLayout = QtWidgets.QVBoxLayout(MusicTable)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = MyMusicTable(MusicTable)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.DashDotDotLine)
        self.tableWidget.setProperty("setMouseTracking", True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(MusicTable)
        QtCore.QMetaObject.connectSlotsByName(MusicTable)

    def retranslateUi(self, MusicTable):
        _translate = QtCore.QCoreApplication.translate
        MusicTable.setWindowTitle(_translate("MusicTable", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MusicTable", "歌名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MusicTable", "歌手"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MusicTable", "专辑"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MusicTable", "时长"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MusicTable", "大小"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MusicTable", "路径"))

from MyMusicTable import MyMusicTable
