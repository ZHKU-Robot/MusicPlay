# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MusicPlayerMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MusicPlayerMainWindow(object):
    def setupUi(self, MusicPlayerMainWindow):
        MusicPlayerMainWindow.setObjectName("MusicPlayerMainWindow")
        MusicPlayerMainWindow.setWindowModality(QtCore.Qt.NonModal)
        MusicPlayerMainWindow.resize(810, 553)
        MusicPlayerMainWindow.setWindowOpacity(1.0)
        MusicPlayerMainWindow.setDocumentMode(False)
        MusicPlayerMainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MusicPlayerMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mainBodyLayout = QtWidgets.QHBoxLayout()
        self.mainBodyLayout.setObjectName("mainBodyLayout")
        self.horizontalLayout_2.addLayout(self.mainBodyLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.01, QtGui.QColor(0, 0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.01, QtGui.QColor(0, 0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.01, QtGui.QColor(0, 0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.01, QtGui.QColor(0, 0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.01, QtGui.QColor(0, 0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.01, QtGui.QColor(0, 0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.01, QtGui.QColor(0, 0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.01, QtGui.QColor(0, 0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.01, QtGui.QColor(0, 0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.widget_3.setPalette(palette)
        self.widget_3.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.01 rgba(0, 0, 0, 0), stop:1 rgba(255, 0, 0, 255))")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnlast = QtWidgets.QPushButton(self.widget_3)
        self.btnlast.setMinimumSize(QtCore.QSize(45, 45))
        self.btnlast.setMaximumSize(QtCore.QSize(45, 45))
        self.btnlast.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/buttonicon/MusicButtonIcon/last.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnlast.setIcon(icon)
        self.btnlast.setIconSize(QtCore.QSize(32, 32))
        self.btnlast.setFlat(True)
        self.btnlast.setObjectName("btnlast")
        self.horizontalLayout.addWidget(self.btnlast)
        self.btnstar = QtWidgets.QPushButton(self.widget_3)
        self.btnstar.setMinimumSize(QtCore.QSize(45, 45))
        self.btnstar.setMaximumSize(QtCore.QSize(45, 45))
        self.btnstar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/buttonicon/MusicButtonIcon/_pause .svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnstar.setIcon(icon1)
        self.btnstar.setIconSize(QtCore.QSize(35, 35))
        self.btnstar.setFlat(True)
        self.btnstar.setObjectName("btnstar")
        self.horizontalLayout.addWidget(self.btnstar)
        self.btnnext = QtWidgets.QPushButton(self.widget_3)
        self.btnnext.setMinimumSize(QtCore.QSize(45, 45))
        self.btnnext.setMaximumSize(QtCore.QSize(45, 45))
        self.btnnext.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/buttonicon/MusicButtonIcon/next.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnnext.setIcon(icon2)
        self.btnnext.setIconSize(QtCore.QSize(32, 32))
        self.btnnext.setFlat(True)
        self.btnnext.setObjectName("btnnext")
        self.horizontalLayout.addWidget(self.btnnext)
        self.horizontalSlider = QtWidgets.QSlider(self.widget_3)
        self.horizontalSlider.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.01 rgba(255, 0, 0, 100), stop:1 rgba(255, 0, 0, 225));\n"
"border-radius: 10px;\n"
"height:30px;\n"
"\n"
"")
        self.horizontalSlider.setMaximum(120)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(True)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.btnvolum = QtWidgets.QPushButton(self.widget_3)
        self.btnvolum.setMinimumSize(QtCore.QSize(30, 30))
        self.btnvolum.setMaximumSize(QtCore.QSize(30, 30))
        self.btnvolum.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/buttonicon/MusicButtonIcon/volume-off.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnvolum.setIcon(icon3)
        self.btnvolum.setIconSize(QtCore.QSize(30, 30))
        self.btnvolum.setFlat(True)
        self.btnvolum.setObjectName("btnvolum")
        self.horizontalLayout.addWidget(self.btnvolum)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.widget_3)
        self.horizontalSlider_2.setMinimumSize(QtCore.QSize(80, 20))
        self.horizontalSlider_2.setMaximumSize(QtCore.QSize(80, 20))
        self.horizontalSlider_2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.01 rgba(255, 0, 0, 100), stop:1 rgba(255, 0, 0, 225));\n"
"\n"
"border-radius: 10px;\n"
"margin: 0px;")
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayout.addWidget(self.horizontalSlider_2)
        self.btnclock = QtWidgets.QPushButton(self.widget_3)
        self.btnclock.setMinimumSize(QtCore.QSize(30, 30))
        self.btnclock.setMaximumSize(QtCore.QSize(30, 30))
        self.btnclock.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/buttonicon/MusicButtonIcon/history.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnclock.setIcon(icon4)
        self.btnclock.setIconSize(QtCore.QSize(30, 30))
        self.btnclock.setFlat(True)
        self.btnclock.setObjectName("btnclock")
        self.horizontalLayout.addWidget(self.btnclock)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout_2.setStretch(0, 9)
        self.verticalLayout_2.setStretch(1, 1)
        MusicPlayerMainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MusicPlayerMainWindow)
        self.toolBar.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.01 rgba(255, 0, 0, 0), stop:1 rgba(255, 0, 0, 100))")
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName("toolBar")
        MusicPlayerMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionPlayList = QtWidgets.QAction(MusicPlayerMainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/buttonicon/MusicButtonIcon/Music.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlayList.setIcon(icon5)
        self.actionPlayList.setObjectName("actionPlayList")
        self.actionBtnMV = QtWidgets.QAction(MusicPlayerMainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/buttonicon/MusicButtonIcon/media.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBtnMV.setIcon(icon6)
        self.actionBtnMV.setObjectName("actionBtnMV")
        self.toolBar.addAction(self.actionPlayList)
        self.toolBar.addAction(self.actionBtnMV)

        self.retranslateUi(MusicPlayerMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MusicPlayerMainWindow)

    def retranslateUi(self, MusicPlayerMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MusicPlayerMainWindow.setWindowTitle(_translate("MusicPlayerMainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MusicPlayerMainWindow", "toolBar"))
        self.actionPlayList.setText(_translate("MusicPlayerMainWindow", "PlayList"))
        self.actionPlayList.setToolTip(_translate("MusicPlayerMainWindow", "打开播放列表"))
        self.actionBtnMV.setText(_translate("MusicPlayerMainWindow", "BtnMV"))
        self.actionBtnMV.setToolTip(_translate("MusicPlayerMainWindow", "打开MV列表"))

import res_rc
