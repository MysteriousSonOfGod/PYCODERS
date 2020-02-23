from PyQt5 import QtSql, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication

def createDB():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('rcb.db')

    if not db.open():
        QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Cannot open database"),
                                   QtWidgets.qApp.tr("Unable to establish a database connection.\n"
                                                 "This example needs SQLite support. Please read "
                                                 "the Qt SQL driver documentation for information "
                                                 "how to build it.\n\n" "Click Cancel to exit."),
                                   QtWidgets.QMessageBox.Cancel)

        return False

    query = QtSql.QSqlQuery()

    query.exec_("create table rcbplayers(ID INT, palyername varchar(20), price INT, city VARCHAR(20))")

    query.exec_("insert into rcbplayers values(18, 'Virat Kohili', 150000000, 'Delhi')")
    query.exec_("insert into rcbplayers values(29,'Gurkeerat Singh', 5000000, 'Punjab')")
    # query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
    # query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
    # query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
    # query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
    return True


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    createDB()