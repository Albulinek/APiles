import ui.main as mainWindow
from PySide import QtGui, QtSql, QtCore
import createDB

layer = []



class MainWindow(QtGui.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('layers.dbx')

        self.model = QtSql.QSqlTableModel()
        self.delrow = -1

        self.setupUi(self)
        self.initializeModel()

    def addLayer(self):
        QtSql.QSqlQuery(self.db).exec_("insert into layers values('NULL', 'Default', 0, 0)")
        self.initializeModel()

    def removeLayer(self):
        self.model.removeRow(self.layersView.currentIndex().row())
        return

    def findRow(self, i):
        self.delrow = i.row()

    def initializeModel(self):
        self.model.setTable('layers')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, 'Name')
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, 'Bearing')
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, 'Thickness')
        self.layersView.setModel(self.model)
        self.layersView.setWindowTitle("Table Model (View 1)")