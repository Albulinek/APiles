import ui.start as mainDialog
import mainWindow as m
import mainWindowMasopust as mas
from PySide import QtGui, QtSql, QtCore
import createDB

class MainDialog(QtGui.QDialog, mainDialog.Ui_StartDialog):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.db = createDB.createDB()
        self.db.setDatabaseName('database.dbx')
        try:
            self.db.open()
        except:
            print('Chyba db')
        self.query = QtSql.QSqlQuery(self.db)

        self.mainWnd = m.MainWindow(self.db, self.query)
        self.masopMainWnd = mas.MainWindow(self.db, self.query)
        self.setupUi(self)

    def openHorizontalPiles(self):
        self.mainWnd.show()

    def openMasopustPiles(self):
        self.masopMainWnd.show()