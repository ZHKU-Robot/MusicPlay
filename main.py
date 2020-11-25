
import sys
import time
import random
import eyed3
from PyQt5.QtCore import QTimer, QUrl, Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QTableWidgetItem, QTableView, QTableWidget, \
    QAbstractItemView
from qtpy import QtMultimedia, QtCore, QtWidgets

from MusicTable import Ui_MusicTable
from musicWindow import Ui_MusicWindow
from MusicPlayerMainWindow import Ui_MusicPlayerMainWindow


import os
class MusicTable(QWidget, Ui_MusicTable):
    def __init__(self, *args, **kwargs):
        super(MusicTable, self).__init__(*args, **kwargs)

class MusicWindow(QWidget, Ui_MusicWindow):
    def __init__(self, *args, **kwargs):
        super(MusicWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.attrInit()
    def attrInit(self,):
        self.musicTable=MusicTable(parent=self)
        self.musicTable.setupUi(self.musicTable)
        self.tableWidget=self.musicTable.tableWidget
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.fileDialog=QFileDialog(self,'选择你的音乐..','.',"music (*.mp3 *.wav *.flav)")
        self.fileDialog.finished.connect(self.musicReloaded)
        self.fileDialog.setModal(1)
        self.fileDialog.setViewMode(QFileDialog.Detail)
        #是因为此Widget的父控件上又添加了其他Widget，覆盖在了按钮上，因此无法点击。
        # self.pushButton.raise_()
        # self.pushButton_2.raise_()
        self.pushButton_2.clicked.connect(self.fileDialog.show)


        self.musicBindInit()
        self.musicLoaded()

    def musicBindInit(self):
        pass
    def musicReloaded(self):
        with open('musicContent.cache',encoding='utf8') as cache:
            musicContent=cache.read()
        musicCache = []
        count=0
        curRow=self.tableWidget.rowCount()
        for i, file in enumerate(self.fileDialog.selectedFiles()):
            if file not in eval(musicContent):
                count+=1
        self.tableWidget.setRowCount(count + self.tableWidget.rowCount())

        with open('musicContent.cache', 'w+',encoding='utf8') as f:
            for i, file in enumerate(self.fileDialog.selectedFiles()):
                if file not in eval(musicContent):
                    musicCache.append(file)
                    mp3 = eyed3.load(file)
                    i+=curRow
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(mp3.tag.title if mp3.tag.title !=None else file.split('/')[-1]))
                    self.tableWidget.setItem(i,1, QTableWidgetItem(mp3.tag.artist if mp3.tag.artist!=None else "未知艺术家"))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(mp3.tag.album if mp3.tag.album!=None else "未知专辑"))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(mp3.info.time_secs / 60)[:4] + 'min'))
                    self.tableWidget.setItem(i, 4,QTableWidgetItem(str(mp3.info.size_bytes / 1024 / 1024)[:5] + 'M'))
                    self.tableWidget.setItem(i, 5, QTableWidgetItem(file))

            f.write(str(musicCache+eval(musicContent)))
            if self.fileDialog.selectedFiles()!=[]:
                self.label_2.setText('共{}首'.format(len(musicCache+eval(musicContent))))
    def musicLoaded(self):
        if not os.path.exists('musicContent.cache'):
            with open('musicContent.cache','w+') as cache:
                cache.write('[]')

        with open('musicContent.cache',encoding='utf8') as cache:
            musicContent=cache.read()

            if musicContent !="[]" and musicContent!='':
                self.tableWidget.setRowCount(len(eval(musicContent)))
                for i, file in enumerate(eval(musicContent)):
                    mp3 = eyed3.load(file)
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(mp3.tag.title if mp3.tag.title !=None else file.split('/')[-1]))
                    self.tableWidget.setItem(i,1, QTableWidgetItem(mp3.tag.artist if mp3.tag.artist!=None else "未知艺术家"))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(mp3.tag.album if mp3.tag.album!=None else "未知专辑"))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(mp3.info.time_secs / 60)[:4] + 'min'))
                    self.tableWidget.setItem(i, 4,QTableWidgetItem(str(mp3.info.size_bytes / 1024 / 1024)[:5] + 'M'))
                    self.tableWidget.setItem(i, 5, QTableWidgetItem(file))
                self.label_2.setText('共{}首'.format(len(eval(musicContent))))
                return
            else:
                pass
        with open('musicContent.cache', 'w+') as cache:
            cache.write('[]')


class MainWindow(QMainWindow, Ui_MusicPlayerMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.qSliderInit()
        self.qMediaPlayerInit()
        self.musicWindowInit()
        self.attrInit()
        self.toolButtonInit()
    def musicWindowInit(self):
        self.musicWindow=MusicWindow(parent=self)

        self.mainBodyLayout.addWidget(self.musicWindow)

    def switchFace(self,index):
        if index == 0:
            self.videoMediaPlayer.pause()
        elif index == 1:
            self.videoMediaPlayer.play()
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

    def myPlayerChanged(self):
        #如果等于1 即正在播放
        if self.musicMediaPlayer.state()==1:
            self.musicMediaPlayer.pause()
            self.btnstar.setIcon(QIcon(":/buttonicon/MusicButtonIcon/_pause .svg"))

        else:
            #记录上一次听过的音乐并播放
            self.musicMediaPlayer.play()
            self.btnstar.setIcon(QIcon(":/buttonicon/MusicButtonIcon/pause.svg"))
    def qMediaPlayerInit(self):
        # 音频流播放器初始化
        self.musicMediaPlayer=QtMultimedia.QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoMediaPlayer = QtMultimedia.QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoMediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(r'mv/mv.mp4')))
        self.videoWidget = QVideoWidget()
        self.mainBodyLayout.addWidget(self.videoWidget)
        self.videoWidget.setVisible(0)
        self.videoMediaPlayer.setVideoOutput(self.videoWidget)
        #音频按钮绑定
        self.btnstar.clicked.connect(self.myPlayerChanged)
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
        self.musicWindow.setStyleSheet("""
        background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0), stop:{} rgba(255, 0, 0, 50),stop:1 rgba(255, 0, 0, 50));
        """.format(indexProportion,indexProportion,indexProportion,indexProportion))


    def closeEvent(self, a0) -> None:
        for i in range(100,0,-1):
            self.setWindowOpacity(i/100)
            time.sleep(0.002)

if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle('No Tension')

    win.setGeometry(111,222,1000,600)
    # win.setWindowFlags(Qt.CustomizeWindowHint)
    win.show()
    sys.exit(app.exec_())
