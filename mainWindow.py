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
        query = QtSql.QSqlQuery(self.db)
        query.exec_("INSERT INTO layers (Name, Soil, Type) VALUES ('Default', '<Choose!>', '<Choose!>')")
        self.model.setTable('layers')
        self.model.select()

    def removeLayer(self):
        self.model.removeRow(self.delrow)
        return

    def findRow(self, i):
        self.delrow = i.row()

    def initializeModel(self):
        self.model.setTable('layers')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()

        self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, 'Name')
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, 'Soil')
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, 'Type')
        self.layersView.setModel(self.model)
        validator = ValidatedItemDelegate()
        validator.createEditor(self, '', self.layersView.currentIndex())
        self.layersView.setItemDelegate(validator)
        self.layersView.setWindowTitle("Table Model (View 1)")
        self.layersView.hideColumn(0)  # Hide ID's

    def returnActuallRow(self):
        return self.delrow


class ValidatedItemDelegate(QtGui.QStyledItemDelegate):
    def createEditor(self, widget, option, index):
        if not index.isValid():
            return 0
        if index.column() == 0:
            editor = QtGui.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp("\d{11}"), editor)
            editor.setValidator(validator)
            return editor
        if index.column() == 2:
            editor = QtGui.QComboBox(widget)
            list = ['Weak rock', 'Coherent', 'Incoherent']
            for i in range(0, len(list)):
                editor.addItem(str(list[i]))
            return editor
        if index.column() == 3:
            model = index.model()
            if model:
                value = model.data(model.index(int(index.row()), int(index.column()) - 1))
            if value == 'Weak rock':
                editor = QtGui.QComboBox(widget)
                list = ['R3', 'R4', 'R5']
                for i in range(0, len(list)):
                    editor.addItem(str(list[i]))
            elif value == 'Coherent':
                editor = QtGui.QComboBox(widget)
                list = ['Id = 0.5', 'Id = 0.7', 'Id = 1.0']
                for i in range(0, len(list)):
                    editor.addItem(str(list[i]))
            elif value == 'Incoherent':
                editor = QtGui.QComboBox(widget)
                list = ['Ic = 0.5', 'Ic >= 1; R6']
                for i in range(0, len(list)):
                    editor.addItem(str(list[i]))
            else:
                editor = QtGui.QComboBox(widget)
                list = ['Choose soil type!']
                editor.addItem(str(list[0]))

            return editor
        return super(ValidatedItemDelegate, self).createEditor(widget, option, index)