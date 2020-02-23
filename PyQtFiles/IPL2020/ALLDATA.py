# from PyQt5 import QtSql, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMessageBox, QApplication
#
# def createDB():
#     db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
#     db.setDatabaseName('sports.db')
#
#     if not db.open():
#         QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Cannot open database"),
#                                    QtWidgets.qApp.tr("Unable to establish a database connection.\n"
#                                                  "This example needs SQLite support. Please read "
#                                                  "the Qt SQL driver documentation for information "
#                                                  "how to build it.\n\n" "Click Cancel to exit."),
#                                    QtWidgets.QMessageBox.Cancel)
#
#         return False
#
#     query = QtSql.QSqlQuery()
#
#     query.exec_("create table sportsmen(id int primary key, "
#                 "firstname varchar(20), lastname varchar(20))")
#
#     query.exec_("insert into sportsmen values(101, 'Roger', 'Federer')")
#     query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
#     query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
#     query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
#     query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
#     return True
#
#
# if __name__ == '__main__':
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     createDB()


import sys
from PyQt5 import QtCore, QtGui, QtSql, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
# import sportsconnection


def initializeModel(model):
    model.setTable('sportsmen')
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")


def createView(title, model):
    view = QtWidgets.QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view


def addrow():
    print(model.rowCount())
    ret = model.insertRows(model.rowCount(), 1)
    print(ret)


def findrow(i):
    delrow = i.row()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('sports.db')
    model = QtSql.QSqlTableModel()
    delrow = -1
    initializeModel(model)

    view1 = createView("Table Model (View 1)", model)
    view1.clicked.connect(findrow)

    dlg = QtWidgets.QDialog()
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(view1)

    button = QtWidgets.QPushButton("Add a row")
    button.clicked.connect(addrow)
    layout.addWidget(button)

    btn1 = QtWidgets.QPushButton("del a row")
    btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
    layout.addWidget(btn1)

    dlg.setLayout(layout)
    dlg.setWindowTitle("Database Demo")
    dlg.show()
    sys.exit(app.exec_())