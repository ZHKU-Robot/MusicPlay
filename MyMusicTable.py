from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class MyMusicTable(QTableWidget):
    def __init__(self, *args, **kwargs):
        super(QTableWidget, self).__init__(*args, **kwargs)
        self.setMouseTracking(True)
        self.setColumnCount(6)
        self.setRowCount(0)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(5, item)
        item = self.horizontalHeaderItem(0)
        item.setText("歌名")
        item = self.horizontalHeaderItem(1)
        item.setText("歌手")
        item = self.horizontalHeaderItem(2)
        item.setText("专辑")
        item = self.horizontalHeaderItem(3)
        item.setText("时长")
        item = self.horizontalHeaderItem(4)
        item.setText("大小")
        item = self.horizontalHeaderItem(5)
        item.setText("路径")
        self.curRow=-1

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


