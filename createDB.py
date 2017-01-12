from PySide import QtSql, QtGui
import site


def createDB():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('database.dbx')

    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                                   QtGui.qApp.tr("Unable to establish a database connection.\n"
                                                 "This example needs SQLite support. Please read "
                                                 "the Qt SQL driver documentation for information "
                                                 "how to build it.\n\n" "Click Cancel to exit."),
                                   QtGui.QMessageBox.Cancel)

        return False

    else:
        query1 = QtSql.QSqlQuery(db)
        print('Execute query 1..')
        query1.exec_(
            "CREATE TABLE layers(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, Name CHAR(20), Thickness FLOAT, Edef FLOAT, c FLOAT, phi FLOAT, ky FLOAT, beta FLOAT)")
        print(query1.lastError())

        query = QtSql.QSqlQuery(db)
        print('Execute query 2..')
        query.exec_("CREATE TABLE piles(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, Thickness FLOAT, Edef FLOAT, diameter FLOAT)")
        print(query.lastError())

        query3 = QtSql.QSqlQuery(db)
        print('Execute query 3..')
        query3.exec_(
            "CREATE TABLE layersMasopust(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, Name CHAR(20), Thickness FLOAT, radius FLOAT, m2 FLOAT, ep FLOAT)")
        print(query3.lastError())

        return db
