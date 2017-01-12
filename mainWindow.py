import ui.main as mainWindow
from PySide import QtGui, QtSql, QtCore
import createDB
import numpy as np
import fem
import io
import sys

layer = []


class MainWindow(QtGui.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self, db, query):
        super(self.__class__, self).__init__()

        self.db = db
        self.query = query

        self.model = QtSql.QSqlTableModel()
        self.delrow = -1

        self.pileModel = QtSql.QSqlTableModel()
        self.pileDelrow = -1

        # STATS
        self.BC = 1
        self.len_FEM = 0.1
        self.V = 0.
        self.H = 0.
        self.M = 0.
        # list with dynamic widgets
        self.txt = []
        self.ky_foot = 0
        self.kx = []
        self.kx_value = []
        self.isselectedconst = False

        self.setupUi(self)
        self.pilesGraphicsView.setSceneRect(0, 0, self.pilesGraphicsView.width(), self.pilesGraphicsView.height())
        self.pilesGraphicsView_2.setSceneRect(0, 0, self.pilesGraphicsView_2.width(), self.pilesGraphicsView_2.height())
        self.pilesGraphicsView_3.setSceneRect(0, 0, self.pilesGraphicsView_3.width(), self.pilesGraphicsView_3.height())

        # validators
        self.bendForceLineEdit.setValidator(
            QtGui.QDoubleValidator(self.bendForceLineEdit))
        self.horizontalForceLineEdit.setValidator(
            QtGui.QDoubleValidator(self.horizontalForceLineEdit))
        self.verticalForceLineEdit.setValidator(
            QtGui.QDoubleValidator(self.verticalForceLineEdit))
        self.femLengthEdit.setValidator(
            QtGui.QDoubleValidator(self.femLengthEdit))
        self.kyfootLineEdit.setValidator(
            QtGui.QDoubleValidator(self.kyfootLineEdit))

        self.stiffnessDynamicGridLayout.setColumnStretch(2, 1)

        self.initializeModel()
        self.initializePileModel()

    def addLayer(self):
        self.query.exec_(
            "INSERT INTO layers (Name, Thickness, Edef, c, phi, ky, beta) VALUES ('Default', '1.', '0.', '0.', '0.', '1.', '0.')")
        print(self.query.lastError())
        self.initializeModel()

    def addPileRow(self):
        self.query.exec_(
            "INSERT INTO piles (Thickness, Edef, diameter) VALUES ('1.', '0.', '0.')")
        print(self.query.lastError())
        self.initializePileModel()

    def removeLayer(self):
        self.model.removeRow(self.delrow)
        return

    def removePileRow(self):
        self.pileModel.removeRow(self.pileDelrow)
        return

    def findRow(self, i):
        self.delrow = i.row()

    def findPileRow(self, i):
        self.pileDelrow = i.row()

    def initializeModel(self):
        self.model.setTable('layers')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()

        self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, 'Název vrtvy')
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, 'Mocnost vrstvy [m]')
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, 'E,def vrstvy [Pa]')
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, 'c [Pa]')
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, 'phi [°]')
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, 'Ky [N/m^2]')
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, 'beta [°]')
        self.layersView.setModel(self.model)
        validator = ValidatedItemDelegate()
        validator.createEditor(self, '', self.layersView.currentIndex())
        self.layersView.setItemDelegate(validator)
        self.layersView.setWindowTitle("Table Model (View 1)")
        self.layersView.hideColumn(0)  # Hide ID's
        for c in range(0, self.layersView.horizontalHeader().count()):
            self.layersView.horizontalHeader().setResizeMode(c, QtGui.QHeaderView.Stretch)

    def initializePileModel(self):
        self.pileModel.setTable('piles')
        self.pileModel.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.pileModel.select()

        self.pileModel.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
        self.pileModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Výška úseku piloty')
        self.pileModel.setHeaderData(2, QtCore.Qt.Horizontal, 'E,def piloty')
        self.pileModel.setHeaderData(3, QtCore.Qt.Horizontal, 'Průměr piloty')
        self.pileLayersView.setModel(self.pileModel)
        validator = ValidatedItemDelegate()
        validator.createEditor(self, '', self.layersView.currentIndex())
        self.pileLayersView.setItemDelegate(validator)
        self.pileLayersView.setWindowTitle("Table Model (View 1)")
        self.pileLayersView.hideColumn(0)  # Hide ID's
        for c in range(0, self.pileLayersView.horizontalHeader().count()):
            self.pileLayersView.horizontalHeader().setResizeMode(c, QtGui.QHeaderView.Stretch)

        # def returnActuallRow(self):
        # return self.delrow

    def createScene(self, view, url):
        scene = QtGui.QGraphicsScene()
        img = QtGui.QPixmap(url)
        scaledPix = img.scaled(view.size(), QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        scene.addPixmap(scaledPix)
        view.setScene(scene)
        view.fitInView(scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)

    def setBC(self):
        if self.floatPileBottomRadioButton.isChecked():
            self.BC = 1
        if self.leanedPileBottomRadioButton.isChecked():
            self.BC = 2
        if self.cantileveredPileBottomRadioButton_2.isChecked():
            self.BC = 3
        print(self.BC)

    def setHorizontalStiffness(self):
        i = self.model.rowCount()
        if self.otherRadioButton.isChecked():
            self.isselectedconst = False
            self.removeWidgets(self.stiffnessDynamicGridLayout)
            self.stiffnessDynamicGridLayout.addWidget(QtGui.QLabel('Název vrstvy', self), 0, 0)
            self.stiffnessDynamicGridLayout.addWidget(QtGui.QLabel('Tuhost pružiny Kx[N/m^2]', self), 0, 1)
            for j in range(0, i):
                txt = QtGui.QLabel(self.model.record(j).value('Name'), self)
                if txt not in self.txt:
                    self.txt.append(txt)
                self.txt[j] = QtGui.QLabel(self.model.record(j).value('Name'), self)
                self.stiffnessDynamicGridLayout.addWidget(self.txt[j], j + 1, 0)

                kx = QtGui.QLineEdit(str(j), self)
                kx.setText('0')
                kx.setValidator(
                    QtGui.QDoubleValidator(kx))
                if len(self.kx) - 1 < j:
                    self.kx.append(kx)
                    self.kx[j].editingFinished.connect(self.sendAllStats)
                self.stiffnessDynamicGridLayout.addWidget(self.kx[j], j + 1, 1)

        else:
            self.isselectedconst = True
            self.removeWidgets(self.stiffnessDynamicGridLayout)





    def runAction(self):
        # TODO: Write check procedure
        self.setHorizontalStiffness()
        self.sendAllStats()

        i = self.model.rowCount()
        L_soil = np.array([])
        Edef_soil = np.array([])
        ky = np.array([])
        beta = np.array([])
        for j in range(0, i):
            L_soil = np.append(L_soil, self.lmbdFloat(self.model.record(j).value('Thickness')))
            Edef_soil = np.append(Edef_soil, self.lmbdFloat(self.model.record(j).value('Edef')))
            ky = np.append(ky, self.lmbdFloat(self.model.record(j).value('ky')))
            beta = np.append(beta, self.lmbdFloat(self.model.record(j).value('beta')))

        L_pile = np.array([])
        Edef_pile = np.array([])
        diameter = np.array([])
        j = self.pileModel.rowCount()
        for k in range(0, j):
            L_pile = np.append(L_pile, self.lmbdFloat(self.pileModel.record(k).value('Thickness')))
            Edef_pile = np.append(Edef_pile, self.lmbdFloat(self.pileModel.record(k).value('Edef')))
            diameter = np.append(diameter, self.lmbdFloat(self.pileModel.record(k).value('diameter')))

        # SHOW RESULTANT GRAPHS
        fem.MKP(L_pile, self.consoleBrowser,
                self.BC, self.len_FEM, self.M,
                self.V, self.H, Edef_pile, diameter, L_soil, Edef_soil, ky, self.kx_value, beta, self.isselectedconst, self.ky_foot)
        self.createScene(self.pilesGraphicsView, 'výsledky/M.png')
        self.pilesGraphicsView.fitInView(0, 0, self.pilesGraphicsView.width(), self.pilesGraphicsView.height(),
                                         QtCore.Qt.KeepAspectRatio)

        self.createScene(self.pilesGraphicsView_2, 'výsledky/V.png')
        self.pilesGraphicsView_2.fitInView(0, 0, self.pilesGraphicsView_2.width(), self.pilesGraphicsView_2.height(),
                                           QtCore.Qt.KeepAspectRatio)

        self.createScene(self.pilesGraphicsView_3, 'výsledky/N.png')
        self.pilesGraphicsView_3.fitInView(0, 0, self.pilesGraphicsView_3.width(), self.pilesGraphicsView_3.height(),
                                           QtCore.Qt.KeepAspectRatio)

        self.createScene(self.uxGraphicView, 'výsledky/Ux.png')
        self.uxGraphicView.fitInView(0, 0, self.uxGraphicView.width(), self.uxGraphicView.height(),
                                           QtCore.Qt.KeepAspectRatio)

        self.createScene(self.uyGraphicView, 'výsledky/Uy.png')
        self.uyGraphicView.fitInView(0, 0, self.uyGraphicView.width(), self.uyGraphicView.height(),
                                           QtCore.Qt.KeepAspectRatio)

    def tabChanged(self):
        print('Tab changed')
        self.setHorizontalStiffness()

    def removeWidgets(self, layout):
        for i in reversed(range(layout.count())):
            widgetToRemove = layout.itemAt(i).widget()
            # remove it from the layout list
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)

    def dbgPrint(self, *objects, sep=' ', end='\n', file=sys.stdout, flush=False):
        # ignore file, uses StringIO API
        sIO = io.StringIO()
        print(*objects, sep=sep, end=end, file=sIO, flush=flush)
        self.consoleBrowser.insertPlainText(sIO.getvalue())
        sIO.close()

    def sendAllStats(self):
        print('Sending stats!')
        self.len_FEM = self.lmbdFloat(self.femLengthEdit.text())
        self.M = self.lmbdFloat(self.bendForceLineEdit.text())
        self.V = self.lmbdFloat(self.verticalForceLineEdit.text())
        self.H = self.lmbdFloat(self.horizontalForceLineEdit.text())
        self.ky_foot = self.lmbdFloat(self.kyfootLineEdit.text())

        for i in range(0, len(self.kx)):
            if i < len(self.kx_value):
                self.kx_value[i] = self.lmbdFloat(self.kx[i].text())
            else:
                self.kx_value.append(self.lmbdFloat(self.kx[i].text()))
        return

        print('Kx values are')
        print(self.kx_value)

    @staticmethod
    def lmbdFloat(text):
        if text == '':
            return float(0)
        else:
            return float(str(text).replace(',', '.'))



class ValidatedItemDelegate(QtGui.QStyledItemDelegate):
    def createEditor(self, widget, option, index):
        if not index.isValid():
            return 0
        if index.column() == 0:
            editor = QtGui.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp("\d{11}"), editor)
            editor.setValidator(validator)
            return editor
        # floating numbers validator
        if index.column() == 1:
            editor = QtGui.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp("^\w{0,15}$"), editor)
            editor.setValidator(validator)
            return editor
        if index.column() > 1:
            editor = QtGui.QLineEdit(widget)
            validator = QtGui.QDoubleValidator(editor)
            editor.setValidator(validator)
            return editor
        """
        Pro masopustovu metodičku??
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
        """
        return super(ValidatedItemDelegate, self).createEditor(widget, option, index)
