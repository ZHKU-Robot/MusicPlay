#ifndef MUSICTABLE_H
#define MUSICTABLE_H

#include <QWidget>

namespace Ui {
class MusicTable;
}

class MusicTable : public QWidget
{
    Q_OBJECT

public:
    explicit MusicTable(QWidget *parent = nullptr);
    ~MusicTable();

private:
    Ui::MusicTable *ui;
};

#endif // MUSICTABLE_H
