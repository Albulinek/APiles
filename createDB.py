from PySide import QtSql, QtGui


def createDB():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('layers.dbx')

    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                                   QtGui.qApp.tr("Unable to establish a database connection.\n"
                                                 "This example needs SQLite support. Please read "
                                                 "the Qt SQL driver documentation for information "
                                                 "how to build it.\n\n" "Click Cancel to exit."),
                                   QtGui.QMessageBox.Cancel)

        return False

    else:
        query = QtSql.QSqlQuery(db)
        print('Execute query..')

        query.exec_("CREATE TABLE layers(id int primary key, name varchar(20), bearing int, thickness int)")
        # query.exec_("insert into layers values('NULL', 'Default', 0, 0)")

        return True


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    createDB()