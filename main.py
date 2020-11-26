
import sys
import time
import random
import eyed3
from PyQt5.QtCore import QTimer, QUrl, Qt, QPoint, QAbstractItemModel
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QTableWidgetItem, QTableView, QTableWidget, \
    QAbstractItemView, QSplitter, QComboBox, QDialog, QMessageBox
from qtpy import QtMultimedia, QtCore, QtWidgets
from musicWindow import Ui_MusicWindow
from MusicPlayerMainWindow import Ui_MusicPlayerMainWindow
import os




class MusicWindow(QWidget, Ui_MusicWindow):
    def __init__(self, *args, **kwargs):
        super(MusicWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.attrInit()
    def attrInit(self,):
        self.musicWinSplitter=QSplitter(self)
        self.horizontalLayout_2.setStretch(4,2)
        # self.musicWinSplitter.setOrientation(Qt.Vertical)
        # self.lyricsWindow.setParent(self.musicWinSplitter)
        # self.musicTable.setParent(self.musicWinSplitter)
        self.musicWinSplitter.addWidget(self.lyricsWindow)
        self.musicWinSplitter.addWidget(self.musicTable)
        self.horizontalLayout_2.addWidget(self.musicWinSplitter)
        self.fileDialog=QFileDialog(self,'选择你的音乐..','.',"music (*.mp3 *.wav *.flac)")

        self.fileDialog.finished.connect(self.musicReloaded)
        self.fileDialog.setModal(1)
        self.fileDialog.setViewMode(QFileDialog.Detail)
        #是因为此Widget的父控件上又添加了其他Widget，覆盖在了按钮上，因此无法点击。
        # self.pushButton.raise_()
        # self.pushButton_2.raise_()
        self.pushButton_2.clicked.connect(self.getMusicPaths)
        self.musicLoaded()
    def getMusicPaths(self):
        self.musicPaths=list(self.fileDialog.getOpenFileNames(self, '选择你的音乐..', '.', "music (*.mp3 *.wav *.flac)"))[:-1][0]
        self.musicReloaded()
    def lyricsWindowInit(self,songPath):
        pass
        # s=eyed3.load(songPath)
        # ly=s.tag.lyrics
        # print(dir(ly))
        # print(ly)
        # for l in dir(ly):
        #     try:
        #         eval('ly.'+l)()
        #     except Exception as e:
        #         print(e)
        #获取歌词

    def musicReloaded(self):
        with open('musicContent.cache',encoding='utf8') as cache:
            musicContent=cache.read()
        musicCache = []
        count=0
        curRow=self.musicTable.rowCount()
        print(self.musicPaths)
        for i, file in enumerate(self.musicPaths):
            if file not in eval(musicContent):
                count+=1
        self.musicTable.setRowCount(count + self.musicTable.rowCount())

        with open('musicContent.cache', 'w+',encoding='utf8') as f:
            for i, file in enumerate(self.musicPaths):
                if file not in eval(musicContent):
                    musicCache.append(file)
                    self.musicContentList.append(file)
                    #暂不支持flac网易云格式
                    mp3 = eyed3.load(file)
                    i+=curRow

                    self.musicTable.setItem(i, 0, QTableWidgetItem(mp3.tag.title if mp3.tag.title !=None else file.split('/')[-1]))
                    self.musicTable.setItem(i,1, QTableWidgetItem(mp3.tag.artist if mp3.tag.artist!=None else "未知艺术家"))
                    self.musicTable.setItem(i, 2, QTableWidgetItem(mp3.tag.album if mp3.tag.album!=None else "未知专辑"))
                    self.musicTable.setItem(i, 3, QTableWidgetItem(str(mp3.info.time_secs / 60)[:4] + 'min'))
                    self.musicTable.setItem(i, 4,QTableWidgetItem(str(mp3.info.size_bytes / 1024 / 1024)[:5] + 'M'))
                    self.musicTable.setItem(i, 5, QTableWidgetItem(file))

            f.write(str(musicCache+eval(musicContent)))
            if self.fileDialog.selectedFiles()!=[]:
                self.label_2.setText('共{}首'.format(len(musicCache+eval(musicContent))))
    def musicLoaded(self):
        if not os.path.exists('musicContent.cache'):
            with open('musicContent.cache','w+',encoding='utf8') as cache:
                cache.write('[]')
            return
        else:
            with open('musicContent.cache','r+',encoding='utf8') as cache:
                musicContent = cache.read()
                #将本地列表加入到历史列表中,因为只有一个播放列表,现在是默认的

                if musicContent !="[]" and musicContent!='':
                    self.musicContentList = eval(musicContent)
                    for i, file in enumerate(self.musicContentList.copy()):
                        if not os.path.exists(file):
                            self.musicContentList.remove(file)

                    self.parent().historyTable = self.musicContentList.copy()
                    self.musicTable.setRowCount(len(self.musicContentList))
                    self.parent().musiclistTable.setRowCount(len(self.musicContentList))
                    for i, file in enumerate(self.musicContentList):
                        mp3 = eyed3.load(file)
                        self.musicTable.setItem(i, 0, QTableWidgetItem(mp3.tag.title if mp3.tag.title !=None else file.split('/')[-1]))
                        self.musicTable.setItem(i,1, QTableWidgetItem(mp3.tag.artist if mp3.tag.artist!=None else "未知艺术家"))
                        self.musicTable.setItem(i, 2, QTableWidgetItem(mp3.tag.album if mp3.tag.album!=None else "未知专辑"))
                        self.musicTable.setItem(i, 3, QTableWidgetItem(str(mp3.info.time_secs / 60)[:4] + 'min'))
                        self.musicTable.setItem(i, 4,QTableWidgetItem(str(mp3.info.size_bytes / 1024 / 1024)[:5] + 'M'))
                        self.musicTable.setItem(i, 5, QTableWidgetItem(file))

                        self.parent().musiclistTable.setItem(i, 0, QTableWidgetItem(mp3.tag.title if mp3.tag.title !=None else file.split('/')[-1]))
                        self.parent().musiclistTable.setItem(i,1, QTableWidgetItem(mp3.tag.artist if mp3.tag.artist!=None else "未知艺术家"))
                        self.parent().musiclistTable.setItem(i, 2, QTableWidgetItem(mp3.tag.album if mp3.tag.album!=None else "未知专辑"))
                        self.parent().musiclistTable.setItem(i, 3, QTableWidgetItem(str(mp3.info.time_secs / 60)[:4] + 'min'))
                        self.parent().musiclistTable.setItem(i, 4,QTableWidgetItem(str(mp3.info.size_bytes / 1024 / 1024)[:5] + 'M'))
                        self.parent().musiclistTable.setItem(i, 5, QTableWidgetItem(file))

                    self.parent().label.setText('共{}首'.format(len(eval(musicContent))))
                    self.label_2.setText('共{}首'.format(len(eval(musicContent))))
                    return
                else:
                    self.musicContentList=[]
                    cache.write('[]')




class MainWindow(QMainWindow, Ui_MusicPlayerMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.qSliderSytleChange()
        self.musicWindowInit()
        self.qMediaPlayerInit()

        self.playModeInit()
        self.attrInit()
        self.toolButtonInit()

    def musicHistoryRemove(self):
        for i in range(self.musiclistTable.rowCount(),-1,-1):
            self.musiclistTable.removeRow(i)
        self.historyTable=[]
        self.label.setText("共0首")
    def musicWindowInit(self):
        self.historyTable=list()
        self.musicWindow=MusicWindow(parent=self)
        # self.verticalLayout_2.setStretch(1,3)
        self.mainBodyLayout.insertWidget(0,self.musicWindow)

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
    def playModeChoice(self):
        self.mode+=1
        self.pushButton_3.setIcon(self.modeIconDict[self.mode])
        self.pushButton_3.setToolTip({1:'列表循环',2:'单曲循环',3:"随机播放"}[self.mode])
        self.musicPlayList.setPlaybackMode(self.modePlay[self.mode])
        if self.mode%len(self.modeIconDict)==0:
            self.mode=0



    def playModeInit(self):
        self.mode=1
        self.modeIconDict={1:QIcon(":/buttonicon/MusicButtonIcon/listcircle.svg"), 2:QIcon(":/buttonicon/MusicButtonIcon/singlecircle.svg")
                            ,3:QIcon(":/buttonicon/MusicButtonIcon/randomplay.svg")}
        self.modePlay={1:QMediaPlaylist .Loop,2:QMediaPlaylist .CurrentItemInLoop,3:QMediaPlaylist .Random}

        self.pushButton_3.clicked.connect(self.playModeChoice)
    def attrInit(self):
        self.playListWindow.setVisible(0)
        #播放列表的索引
        self.playListIndex=0
        #现在播放的音乐
        self.curMusic=''
        self.face={0:self.musicWindow,1:self.videoWidget}
        #history..按键初始化
        self.pushButton_2.clicked.connect( self.musicHistoryRemove)
    def myPlayerChanged(self):
        #如果等于1 即正在播放
        if self.musicMediaPlayer.state()==1:
            self.musicMediaPlayer.pause()
            self.btnstar.setIcon(QIcon(":/buttonicon/MusicButtonIcon/_pause .svg"))
        else:
            #这里意味着 直接点击播放键,没有进行任何处理默认从历史记录开始
            if self.curMusic=='':
                self.musicPlayList.setCurrentIndex(1)
                self.musicMediaPlayer.setPlaylist(self.musicPlayList)
                self.curMusic=self.musicPlayList.currentMedia().canonicalUrl().path()[1:]
                #记录上一次听过的音乐并播放s

            self.musicMediaPlayer.play()

            self.btnstar.setIcon(QIcon(":/buttonicon/MusicButtonIcon/pause.svg"))
    def qSliderChange(self):
        self.horizontalSlider.setValue(self.musicMediaPlayer.position())
        self.label_2.setText("{}".format(round(self.musicMediaPlayer.position()/1000/60,2)))
    def qMediaPlayerInit(self):
        # 音频流播放器初始化
        self.musicMediaPlayer=QtMultimedia.QMediaPlayer(None)
        self.musicMediaPlayer.durationChanged.connect(self.qSilderInit)
        self.musicMediaPlayer.positionChanged.connect(self.qSliderChange)
        self.musicPlayList=QMediaPlaylist()

        for url in self.historyTable:
            self.musicPlayList.addMedia(QMediaContent(QUrl.fromLocalFile(url)))
        self.musicPlayList.setCurrentIndex(0)
        #最后一个项目播放完毕后，将从第一个项目重新开始播放。
        self.musicPlayList.setPlaybackMode(QMediaPlaylist.Loop)
        self.musicMediaPlayer.setPlaylist(self.musicPlayList)

        self.videoMediaPlayer = QtMultimedia.QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoMediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(r'mv/mv.mp4')))
        self.videoWidget = QVideoWidget()
        self.mainBodyLayout.insertWidget(0,self.videoWidget)
        self.videoWidget.setVisible(0)
        self.videoMediaPlayer.setVideoOutput(self.videoWidget)
        #音频按钮绑定
        self.btnstar.clicked.connect(self.myPlayerChanged)
        self.btnHistory.clicked.connect(lambda :self.playListWindow.setVisible(0 if self.playListWindow.isVisible() else 1))
    def qSilderInit(self):
        musicSize=self.musicMediaPlayer.duration()
        self.horizontalSlider.setMaximum(musicSize)
        self.label_3.setText("{}".format(round(musicSize/1000/60,2)))
        self.horizontalSlider.sliderMoved.connect(lambda :self.musicMediaPlayer.setPosition(self.horizontalSlider.value()))
    def qSliderSytleChange(self):
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
        background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(	255,105,180, {}), stop:{} rgba(	255,182,193,{}),stop:1 rgba(	255,182,193,{}));
        """.format(1-indexProportion,1-indexProportion,indexProportion,indexProportion))
        self.widget_3.setStyleSheet("""
        background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255,182,193, {}), stop:{} rgba(	255,182,193, {}),stop:1 rgba(	255,182,193, {}));
        """.format(1-indexProportion,1-indexProportion,indexProportion,indexProportion))
        # self.musicWindow.setStyleSheet("""
        # background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:{}, stop:0 rgba(255, 255, 255, 0), stop:{} rgba(255, 0, 0, 50),stop:1 rgba(255, 0, 0, 50));
        # """.format(indexProportion,indexProportion,indexProportion,indexProportion))


    def closeEvent(self, a0) -> None:
        with open('musicContent.cache','w+',encoding='utf8')as f:
            f.write(str(self.musicWindow.musicContentList))

        for i in range(100,0,-1):
            self.setWindowOpacity(i/100)
            time.sleep(0.002)

if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle('No Tension')

    win.setGeometry(333,333,1000,600)
    # win.setWindowFlags(Qt.CustomizeWindowHint)
    win.show()
    sys.exit(app.exec_())
