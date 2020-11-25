# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'songwordsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_songwordsWindow(object):
    def setupUi(self, songwordsWindow):
        songwordsWindow.setObjectName("songwordsWindow")
        songwordsWindow.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(songwordsWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListView(songwordsWindow)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(songwordsWindow)
        QtCore.QMetaObject.connectSlotsByName(songwordsWindow)

    def retranslateUi(self, songwordsWindow):
        _translate = QtCore.QCoreApplication.translate
        songwordsWindow.setWindowTitle(_translate("songwordsWindow", "Form"))

