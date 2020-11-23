
import sys
import time
import random
import eyed3
from PyQt5 import sip
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QTableWidgetItem, QTableView
from qtpy import QtMultimedia
from musicWindow import Ui_MusicWindow
from MusicPlayerMainWindow import Ui_MusicPlayerMainWindow
import os
class MusicWindow(QWidget, Ui_MusicWindow):
    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.attrInit()
    def attrInit(self):
        self.fileDialog=QFileDialog(self,'选择你的音乐..','.',"music (*.mp3 *.wav *.flav)")
        self.fileDialog.finished.connect(self.musicReloaded)
        self.fileDialog.setModal(1)
        self.fileDialog.setViewMode(QFileDialog.Detail)
        self.pushButton_2.clicked.connect(self.fileDialog.show)
        self.tableWidget.setColumnCount(6)
        self.musicLoaded()

        pass
    def musicReloaded(self):

        musicCache = []
        self.tableWidget.setRowCount(len(self.fileDialog.selectedFiles()))
        with open('musicContent.cache', 'w+') as f:
            for i, file in enumerate(self.fileDialog.selectedFiles()):
                musicCache.append(file)
                mp3 = eyed3.load(file)

                self.tableWidget.setItem(i, 0, QTableWidgetItem(mp3.tag.title))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(mp3.tag.artist))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(mp3.tag.album))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(str(mp3.info.time_secs / 60)[:4] + 'min'))
                self.tableWidget.setItem(i, 4, QTableWidgetItem(str(mp3.info.size_bytes / 1024 / 1024)[:5] + 'M'))
            f.write(str(musicCache))
    def musicLoaded(self):
        if not os.path.exists('musicContent.cache'):
            with open('musicContent.cache','w+') as cache:
                cache.write('first init..')

        with open('musicContent.cache') as cache:
            musicContent=cache.read()
            if musicContent !="[]":
                self.tableWidget.setRowCount(len(eval(musicContent)))
                for i, file in enumerate(eval(musicContent)):
                    mp3 = eyed3.load(file)
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(mp3.tag.title))
                    self.tableWidget.setItem(i,1, QTableWidgetItem(mp3.tag.artist))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(mp3.tag.album))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(mp3.info.time_secs / 60)[:4] + 'min'))
                    self.tableWidget.setItem(i, 4,QTableWidgetItem(str(mp3.info.size_bytes / 1024 / 1024)[:5] + 'M'))






class MainWindow(QMainWindow, Ui_MusicPlayerMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.musicWindowInit()
        self.qSliderInit()
        self.qMediaPlayerInit()
        self.attrInit()
        self.toolButtonInit()
    def musicWindowInit(self):
        self.musicWindow=MusicWindow()

        self.mainBodyLayout.addWidget(self.musicWindow)

    def switchFace(self,index):
        if index == 0:
            self.musicMediaPlayer.pause()
        elif index == 1:
            self.musicMediaPlayer.play()
        for face in list(self.face.keys()):
            if face!=index:
                self.face[face].setVisible(0)
            else:
                self.face[face].setVisible(1)
    def toolButtonInit(self):
        self.actionPlayList.triggered.connect(lambda :self.switchFace(0))
        self.actionBtnMV.triggered.connect(lambda :self.switchFace(1))
    def attrInit(self):
        self.face={0:self.musicWindow,1:self.videoWidget}
    def qMediaPlayerInit(self):
        self.musicMediaPlayer=QtMultimedia.QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.musicMediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(r'mv/mv.mp4')))
        self.videoWidget = QVideoWidget()
        self.mainBodyLayout.addWidget(self.videoWidget)
        self.videoWidget.setVisible(0)
        self.musicMediaPlayer.setVideoOutput(self.videoWidget)
    def qSliderInit(self):
        self.styleTimer=QTimer()
        self.temp = 0
        self.tempOpac=0
        self.end=0
        self.tempColor = random.randint(0,255)
        self.toolBarWidth=self.toolBar.size().width()
        self.styleTimer.timeout.connect(self.styleChange)
        self.styleTimer.start()
        self.styleTimer.setInterval(10)
        self.horizontalSlider.setStyleSheet("""
        QSlider#horizontalSlider::handle {    
width:0px;
padding:0px 0px;
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.01 rgba(255,255, 255, 100), stop:1 rgba(255, 255, 0, 255));
    border:120px solid red;
     border-radius: 10px;
    border-image: url(:/buttonicon/MusicButtonIcon/robot.svg) 370 0 0 330 round;
}; background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.01 rgba(255, 255, 0, 100), stop:1 rgba(255, 0, 0, 225));
height:40px;
 border-radius: 20px;
        """)
    def styleChange(self):
        #设置中间值,作为一个移动的东东,这里是temp
        #计算比例

        #接着我们从0开始

        if self.end == 0 :
            if int(self.temp)<self.toolBarWidth:
                self.temp+=self.toolBarWidth/100
            else:
                self.end=1
                self.tempColor= random.randint(0,255)
        else:
            if int(self.temp)>0:
                self.temp -= self.toolBarWidth/100
            else:
                self.end=0
                self.tempColor = random.randint(0, 255)
        indexProportion=self.temp/self.toolBarWidth

        self.toolBar.setStyleSheet("""
        background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, {}), stop:{} rgba(255, 0, 0,{}),stop:1 rgba(255, 0, 0,{}));
        """.format(indexProportion,indexProportion,indexProportion,indexProportion))
        self.widget_3.setStyleSheet("""
        background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, {}), stop:{} rgba(255, 0, 0, {}),stop:1 rgba(255, 0, 0, {}));
        """.format(indexProportion,indexProportion,indexProportion,indexProportion))






    def closeEvent(self, a0) -> None:
        for i in range(100,0,-1):
            self.setWindowOpacity(i/100)
            time.sleep(0.002)

if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
