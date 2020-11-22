#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QMediaPlayer>
#include <QMediaPlaylist>
#include <QStringList>
#include <QPushButton>
#include <QDir>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    void init(); //初始化播放列表和播放器
    QStringList getFileNames(const QString &path);  // 启动播放器和暂停播放器

private:
    Ui::MainWindow *ui;
    bool isPlay=false;
    QString MusicPath = "/home/chen/Music";
    QMediaPlaylist * playlist; //播放列表
    QMediaPlayer * play; //播放器


private slots:
    void ButtonConvert(); //播放键与暂停键的切换
    void MusicNext(); //切换下一首
};

#endif // MAINWINDOW_H
