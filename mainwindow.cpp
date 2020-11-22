#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDebug>


MainWindow::MainWindow(QWidget *parent) :QMainWindow(parent),ui
(new Ui::MainWindow)
{
    ui->setupUi(this);
    init();
    connect(ui->btnstar,&QPushButton::clicked,this,&MainWindow::ButtonConvert);
    connect(ui->btnnext,&QPushButton::clicked,this,&MainWindow::MusicNext);
    connect(ui->btnlast,&QPushButton::clicked,playlist,&QMediaPlaylist::previous);
}


// 初始化播放列表和播放器
void MainWindow::init()
{
    playlist = new QMediaPlaylist(this);
    QStringList fileList = getFileNames(this->MusicPath); //获取文件夹下的所有音乐文件

    for(int i=0;i<fileList.size();i++)
    {
        QString fileName = fileList.at(i);
        playlist->addMedia(QUrl::fromLocalFile(MusicPath+"/"+fileName));
    }
    playlist->setCurrentIndex(1);
    play = new QMediaPlayer(this);
    play->setMedia(playlist);
}


// 启动播放器和暂停播放器
void MainWindow::ButtonConvert()
{
    if(!isPlay)
    {
        ui->btnstar->setIcon(QIcon(":/buttonicon/MusicButtonIcon/暂停.svg"));
        ui->btnstar->setIconSize(QSize(45,45));
        isPlay = true;
        play->play();
    }
    else
    {
        ui->btnstar->setIcon(QIcon(":/buttonicon/MusicButtonIcon/greenplay.svg"));
        isPlay = false;
        play->pause();
    }
}


//获取文件夹下所有文件名字
QStringList MainWindow::getFileNames(const QString &path)
{
    QDir dir(path);
    QStringList nameFilters;
    nameFilters << "*.mp3";
    QStringList files = dir.entryList(nameFilters,QDir::Files|QDir::Readable,QDir::Name);
    return files;
}

void MainWindow::MusicNext()  //切换下一首
{
//    int i = playlist->currentIndex();
//    int lenth = playlist->mediaCount();
//    if(i == lenth-1)
//    {
//        playlist->
//    }
    playlist->next();

}


MainWindow::~MainWindow()
{
    delete ui;
}
