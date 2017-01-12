import ui.mainMasopust as mainWindowMasopust
from PySide import QtGui, QtSql, QtCore, QtWebKit, QtNetwork
import createDB
import masopust
import io
import sys
import numpy as np

layer = []


class MainWindow(QtGui.QMainWindow, mainWindowMasopust.Ui_MainWindow):
    def __init__(self, db, query):
        super(self.__class__, self).__init__()

        self.setupUi(self)

        self.db = db
        self.query = query

        self.model = QtSql.QSqlTableModel()
        self.delrow = -1

        self.webView = PDFViewer(self)
        self.webLayout.addWidget(self.webView, 0)

        self.initializeModel()

        self.V = 0
        self.a = []
        self.a_value = []
        self.b = []
        self.b_value = []
        self.e = []
        self.e_value = []
        self.f = []
        self.f_value = []
        self.Es = []
        self.Es_value = []
        self.txt = []

        # self.setHorizontalStiffness()

    def sendAllStats(self):
        return

    def tabChanged(self):
        return

    def removeLayer(self):
        self.model.removeRow(self.delrow)
        return

    def findRow(self, i):
        self.delrow = i.row()

    def addLayer(self):
        self.query.exec_(
            "INSERT INTO layersMasopust(Name, Thickness, radius, m2, ep) VALUES ('Default', '1.', '1.', '1.', '1.')")
        print(self.query.lastError())
        self.initializeModel()

    def runAction(self):
        return

    def initializeModel(self):
        self.model.setTable('layersMasopust')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()

        self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, 'Název vrstvy')
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, 'Mocnost vrstvy [m]')
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, 'Průměr piloty [m]')
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, 'Ochrana dříku m2 [-]')
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, 'E piloty [MPa]')
        self.layersView.setModel(self.model)
        validator = ValidatedItemDelegate()
        validator.createEditor(self, '', self.layersView.currentIndex())
        self.layersView.setItemDelegate(validator)
        self.layersView.setWindowTitle("Table Model (View 1)")
        self.layersView.hideColumn(0)  # Hide ID's
        for c in range(0, self.layersView.horizontalHeader().count()):
            self.layersView.horizontalHeader().setResizeMode(c, QtGui.QHeaderView.Stretch)

    def setHorizontalStiffness(self):
        i = self.model.rowCount()
        self.stiffnessDynamicGridLayout.setSpacing(10)


        self.removeWidgets(self.stiffnessDynamicGridLayout)
        self.stiffnessDynamicGridLayout.addWidget(QtGui.QLabel('Název vrstvy', self), 0, 0)
        self.stiffnessDynamicGridLayout.addWidget(QtGui.QLabel('Regresní součinitel a', self), 0, 1)
        self.stiffnessDynamicGridLayout.addWidget(QtGui.QLabel('Regresní součinitel b', self), 0, 2)
        self.stiffnessDynamicGridLayout.addWidget(QtGui.QLabel('Regresní součinitel e', self), 0, 3)
        self.stiffnessDynamicGridLayout.addWidget(QtGui.QLabel('Regresní součinitel f', self), 0, 4)
        self.stiffnessDynamicGridLayout.addWidget(QtGui.QLabel('Sečný modul zeminy Es', self), 0, 5)

        for j in range(0, i):
            txt = QtGui.QLabel(self.model.record(j).value('Name'), self)
            if txt not in self.txt:
                self.txt.append(txt)
            self.txt[j] = QtGui.QLabel(self.model.record(j).value('Name'), self)
            self.stiffnessDynamicGridLayout.addWidget(self.txt[j], j + 1, 0)

            a = QtGui.QLineEdit(str(j), self)
            a.setText('1')
            a.setValidator(
                QtGui.QDoubleValidator(a))
            if len(self.a) - 1 < j:
                self.a.append(a)
                self.a[j].editingFinished.connect(self.sendAllStats)
            self.stiffnessDynamicGridLayout.addWidget(self.a[j], j + 1, 1)

            b = QtGui.QLineEdit(str(j), self)
            b.setText('1')
            b.setValidator(
                QtGui.QDoubleValidator(b))
            if len(self.b) - 1 < j:
                self.b.append(b)
                self.b[j].editingFinished.connect(self.sendAllStats)
            self.stiffnessDynamicGridLayout.addWidget(self.b[j], j + 1, 2)

            e = QtGui.QLineEdit(str(j), self)
            e.setText('1')
            e.setValidator(
                QtGui.QDoubleValidator(e))

            if len(self.e) - 1 < j:
                self.e.append(e)
                self.e[j].editingFinished.connect(self.sendAllStats)
            self.stiffnessDynamicGridLayout.addWidget(self.e[j], j + 1, 3)

            f = QtGui.QLineEdit(str(j), self)
            f.setText('1')
            f.setValidator(
                QtGui.QDoubleValidator(a))
            if len(self.f) - 1 < j:
                self.f.append(f)
                self.f[j].editingFinished.connect(self.sendAllStats)
            self.stiffnessDynamicGridLayout.addWidget(self.f[j], j + 1, 4)

            Es = QtGui.QLineEdit(str(j), self)
            Es.setText('1')
            Es.setValidator(
                QtGui.QDoubleValidator(Es))
            if len(self.Es) - 1 < j:
                self.Es.append(Es)
                self.Es[j].editingFinished.connect(self.sendAllStats)

            self.stiffnessDynamicGridLayout.addWidget(self.Es[j], j + 1, 5)

    def tabChanged(self):
        print('Tab changed')
        self.setHorizontalStiffness()
        # maybe() is better solution, but this will prevent some weird behaviour if user do something unexpected
        self.sendAllStats()

    def removeWidgets(self, layout):
        for i in reversed(range(layout.count())):
            widgetToRemove = layout.itemAt(i).widget()
            # remove it from the layout list
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)

    def sendAllStats(self):
        self.V = self.lmbdFloat(self.verticalForceLineEdit.text())
        for i in range(0, len(self.a)):
            if i < len(self.a_value):
                self.a_value[i] = self.lmbdFloat(self.a[i].text())
                self.b_value[i] = self.lmbdFloat(self.b[i].text())
                self.e_value[i] = self.lmbdFloat(self.e[i].text())
                self.f_value[i] = self.lmbdFloat(self.f[i].text())
                self.Es_value[i] = self.lmbdFloat(self.Es[i].text())
            else:
                self.a_value.append(self.lmbdFloat(self.a[i].text()))
                self.b_value.append(self.lmbdFloat(self.b[i].text()))
                self.e_value.append(self.lmbdFloat(self.e[i].text()))
                self.f_value.append(self.lmbdFloat(self.f[i].text()))
                self.Es_value.append(self.lmbdFloat(self.Es[i].text()))

    @staticmethod
    def lmbdFloat(text):
        if text == '':
            return float(0)
        else:
            return float(str(text).replace(',', '.'))

    def createScene(self, view, url):
        scene = QtGui.QGraphicsScene()
        img = QtGui.QPixmap(url)
        scaledPix = img.scaled(view.size(), QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        scene.addPixmap(scaledPix)
        view.setScene(scene)
        view.fitInView(scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)

    def runAction(self):
        self.setHorizontalStiffness()
        # TODO: Write check procedure
        self.sendAllStats()
        if self.radioButton.isChecked():
            m1 = 0.7
        else:
            m1 = 1

        L = np.array([])
        radius = np.array([])
        m2 = np.array([])
        edp = np.array([])
        i = self.model.rowCount()
        for k in range(0, i):
            L = np.append(L, self.lmbdFloat(self.model.record(k).value('Thickness')))
            radius = np.append(radius, self.lmbdFloat(self.model.record(k).value('radius')))
            m2 = np.append(m2, self.lmbdFloat(self.model.record(k).value('m2')))
            edp = np.append(edp, self.lmbdFloat(self.model.record(k).value('m2')))

        masopust.masopust(self.consoleBrowser, L, h_head_pile=0, L_pile=L, D_pile=radius, reg_a=self.a_value, reg_b=self.b_value, reg_e=self.e_value, reg_f=self.f_value, soil_Es=self.Es_value, pile_E=edp, m2=m2, V=self.V, m1=m1)
        # SHOW RESULTANT GRAPHS
        self.createScene(self.pilesGraphicsView_2, 'výsledky/masopust.png')
        self.pilesGraphicsView_2.fitInView(0, 0, self.pilesGraphicsView_2.width(), self.pilesGraphicsView_2.height(),
                                         QtCore.Qt.KeepAspectRatio)

    def dbgPrint(self, *objects, sep=' ', end='\n', file=sys.stdout, flush=False):
        # ignore file, uses StringIO API
        sIO = io.StringIO()
        print(*objects, sep=sep, end=end, file=sIO, flush=flush)
        self.consoleBrowser.insertPlainText(sIO.getvalue())
        sIO.close()


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
        return super(ValidatedItemDelegate, self).createEditor(widget, option, index)


class PDFViewer(QtWebKit.QWebView):
    pdf_viewer_page = 'res/masopust.html'

    def __init__(self, parent=None):
        super().__init__(parent)
        self.settings = QtWebKit.QWebSettings.globalSettings()
        self.settings.setAttribute(QtWebKit.QWebSettings.LocalContentCanAccessFileUrls, True)
        self.settings.setAttribute(QtWebKit.QWebSettings.LocalContentCanAccessRemoteUrls, True)
        # self.settings.setAttribute(QtWebKit.QWebSettings.DeveloperExtrasEnabled, True )
        # nam = QtNetwork.QNetworkAccessManager()
        # page = QtWebKit.QWebPage(self)
        # page.setNetworkAccessManager(nam)
        # self.setPage(page)
        # self.loadFinished.connect(self.onLoadFinish)
        self.setUrl(QtCore.QUrl(self.pdf_viewer_page))

    def onLoadFinish(self, success):
        if success:
            self.page().mainFrame().evaluateJavaScript("init();")
