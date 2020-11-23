
import sys
import time
import random

from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from qtpy import QtMultimedia

from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.qSliderInit()
        self.qMediaPlayerInit()
        self.timer=QTimer()
        self.temp = 0
        self.tempOpac=0
        self.end=0
        self.tempColor = 0
        self.toolBarWidth=self.toolBar.size().width()
        self.timer.timeout.connect(self.styleChange)
        self.timer.start(11000)
        self.timer.setInterval(30)
    def qMediaPlayerInit(self):
        self.myMediaPlayer=QtMultimedia.QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.myMediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(r'插画.mp4')))
        self.videoWidget = QVideoWidget(self)
        self.horizontalLayout_2.addWidget(self.videoWidget)
        self.myMediaPlayer.setVideoOutput(self.videoWidget)
        self.myMediaPlayer.play()
        self.videoWidget.show()
    def callback(self):
        self.player.setPosition(0) # to start at the beginning of the video every time
        self.video.show()
        self.player.play()
    def qSliderInit(self):
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
        else:
            if int(self.temp)>0:
                self.temp -= self.toolBarWidth/100
            else:
                self.end=0
        indexProportion=self.temp/self.toolBarWidth

        self.toolBar.setStyleSheet("""
        background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 100), stop:{} rgba(255, 0, 0, 100),stop:1 rgba(255, 0, 0, 100));
        """.format(indexProportion,indexProportion))
        self.widget_3.setStyleSheet("""
        background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:{} rgba(255, 0, 0, 255),stop:1 rgba(255, 0, 0, 255));
        """.format(indexProportion,indexProportion))






    def closeEvent(self, a0) -> None:
        for i in range(100,0,-1):
            self.setWindowOpacity(i/100)
            time.sleep(0.002)

if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
