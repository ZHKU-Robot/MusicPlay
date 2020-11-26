from PyQt5.QtCore import QPoint, QUrl
from PyQt5.QtGui import QBrush, QColor, QPixmap, QIcon
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class MyMusicTable(QTableWidget):
    def __init__(self,*args, **kwargs):
        #记得要添加父类
        super(MyMusicTable, self).__init__(*args, **kwargs)
        self.setMouseTracking(True)
        self.curRow=-1
        self.play=0
        self.songPath= ''
        self.mainWindow=self.parent().parent()
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
    def mouseDoubleClickEvent(self, e) -> None:
        if self.lastRow!=-1:
            self.songPath = self.item(self.lastRow, self.columnCount() - 1).text()
            #将当前曲目加入历史列表中

            self.mainWindow.musicMediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.songPath)))

            self.mainWindow.musicMediaPlayer.play()

            #加载歌词
            self.mainWindow.musicWindow.lyricsWindowInit(self.songPath)
            if self.mainWindow.musicMediaPlayer.state()==1:
                self.mainWindow.btnstar.setIcon(QIcon(":/buttonicon/MusicButtonIcon/pause.svg"))
            else:
                pass



