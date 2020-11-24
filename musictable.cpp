#include "musictable.h"
#include "ui_musictable.h"

MusicTable::MusicTable(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::MusicTable)
{
    ui->setupUi(this);
}

MusicTable::~MusicTable()
{
    delete ui;
}
