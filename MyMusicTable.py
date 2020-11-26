import eyed3
from PyQt5.QtCore import QPoint, QUrl
from PyQt5.QtGui import QBrush, QColor, QPixmap, QIcon
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QWidget


class MyMusicTable(QTableWidget):
    def __init__(self,*args, **kwargs):
        #记得要添加父类
        super(MyMusicTable, self).__init__(*args, **kwargs)
        self.setMouseTracking(True)
        self.curRow=-1
        self.play=0
        self.songPath= ''
        self.mainWindow = self.parent().parent()
        if type(self.mainWindow)==QWidget:
            self.mainWindow=self.parent().parent().parent()


    def mouseMoveEvent(self, e) -> None:
        self.globalPos=e.pos()
        self.lastRow=self.rowAt(self.globalPos.y())

        if self.lastRow!=self.curRow:
            items = []
            for i in range(self.columnCount()):
                item=self.item(self.lastRow,i)
                if item!=None:
                    items.append(item)
            for row in items:
                row.setForeground(QBrush(QColor(255, 0, 0, 255)))
            items = []
            for i in range(self.columnCount()):
                item=self.item(self.curRow,i)
                if item!=None:
                    items.append(item)
            for row in items:
                row.setForeground(QBrush(QColor(0, 0, 0, 255)))
            self.curRow=self.lastRow
    def getCurMusicSize(self,path):
        for row in range(self.rowCount()):
            print(path,self.item(row,5).text())
            if self.item(row,5).text()==path:
                return self.item(row,3).text()
        return 0
        pass
    def mouseDoubleClickEvent(self, e) -> None:
        if self.lastRow!=-1:
            self.songPath = self.item(self.lastRow, self.columnCount() - 1).text()
            #将当前曲目加入历史列表中

            self.mainWindow.musicMediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.songPath)))
            self.mainWindow.curMusic=self.songPath

            #如果是播放历史table
            if isinstance(self.mainWindow,QWidget):
                if self.songPath not in self.mainWindow.historyTable:

                    #如果放的歌没在历史记录里,加入并且放在最前面
                    mp3 = eyed3.load(self.songPath)
                    self.mainWindow.musiclistTable.setRowCount(self.mainWindow.musiclistTable.rowCount()+1)
                    i =self.mainWindow.musiclistTable.rowCount()-1
                    file=self.songPath
                    self.mainWindow.musiclistTable.setItem(i, 0, QTableWidgetItem(
                        mp3.tag.title if mp3.tag.title != None else file.split('/')[-1]))
                    self.mainWindow.musiclistTable.setItem(i, 1,
                                            QTableWidgetItem(mp3.tag.artist if mp3.tag.artist != None else "未知艺术家"))
                    self.mainWindow.musiclistTable.setItem(i, 2,
                                            QTableWidgetItem(mp3.tag.album if mp3.tag.album != None else "未知专辑"))
                    self.mainWindow.musiclistTable.setItem(i, 3, QTableWidgetItem(str(mp3.info.time_secs / 60)[:4] + 'min'))
                    self.mainWindow.musiclistTable.setItem(i, 4,
                                            QTableWidgetItem(str(mp3.info.size_bytes / 1024 / 1024)[:5] + 'M'))
                    self.mainWindow.musiclistTable.setItem(i, 5, QTableWidgetItem(file))
                    self.mainWindow.historyTable.insert(0,self.songPath)
                else:
                    #如果在的话，置顶
                    self.mainWindow.musiclistTable
                self.mainWindow.label.setText("共{}首".format(len(self.mainWindow.historyTable)))

            self.mainWindow.musicMediaPlayer.play()

            #加载歌词
            self.mainWindow.musicWindow.lyricsWindowInit(self.songPath)
            if self.mainWindow.musicMediaPlayer.state()==1:
                self.mainWindow.btnstar.setIcon(QIcon(":/buttonicon/MusicButtonIcon/pause.svg"))
            else:
                pass



