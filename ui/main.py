# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Tue Jan 10 16:48:45 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1709, 838)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ui/icons/Rock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.consoleBrowser = QtGui.QTextBrowser(self.tab_3)
        self.consoleBrowser.setMinimumSize(QtCore.QSize(500, 350))
        self.consoleBrowser.setMaximumSize(QtCore.QSize(500, 350))
        self.consoleBrowser.setObjectName("consoleBrowser")
        self.gridLayout_3.addWidget(self.consoleBrowser, 2, 3, 1, 1)
        self.pilesGraphicsView_3 = QtGui.QGraphicsView(self.tab_3)
        self.pilesGraphicsView_3.setMinimumSize(QtCore.QSize(500, 350))
        self.pilesGraphicsView_3.setMaximumSize(QtCore.QSize(500, 350))
        self.pilesGraphicsView_3.setObjectName("pilesGraphicsView_3")
        self.gridLayout_3.addWidget(self.pilesGraphicsView_3, 2, 1, 1, 1)
        self.pilesGraphicsView = QtGui.QGraphicsView(self.tab_3)
        self.pilesGraphicsView.setMinimumSize(QtCore.QSize(500, 350))
        self.pilesGraphicsView.setMaximumSize(QtCore.QSize(500, 350))
        self.pilesGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pilesGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pilesGraphicsView.setObjectName("pilesGraphicsView")
        self.gridLayout_3.addWidget(self.pilesGraphicsView, 1, 1, 1, 1)
        self.pilesGraphicsView_2 = QtGui.QGraphicsView(self.tab_3)
        self.pilesGraphicsView_2.setMinimumSize(QtCore.QSize(500, 350))
        self.pilesGraphicsView_2.setMaximumSize(QtCore.QSize(500, 350))
        self.pilesGraphicsView_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pilesGraphicsView_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pilesGraphicsView_2.setObjectName("pilesGraphicsView_2")
        self.gridLayout_3.addWidget(self.pilesGraphicsView_2, 1, 3, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uxGraphicView = QtGui.QGraphicsView(self.tab_4)
        self.uxGraphicView.setObjectName("uxGraphicView")
        self.verticalLayout.addWidget(self.uxGraphicView)
        self.uyGraphicView = QtGui.QGraphicsView(self.tab_4)
        self.uyGraphicView.setObjectName("uyGraphicView")
        self.verticalLayout.addWidget(self.uyGraphicView)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.horizontalLayout_7.addWidget(self.tabWidget_2)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.layersTab = QtGui.QWidget()
        self.layersTab.setObjectName("layersTab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layersTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.removeLayerButton = QtGui.QPushButton(self.layersTab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ui/icons/Minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeLayerButton.setIcon(icon1)
        self.removeLayerButton.setObjectName("removeLayerButton")
        self.gridLayout.addWidget(self.removeLayerButton, 1, 2, 1, 1)
        self.layersView = QtGui.QTableView(self.layersTab)
        self.layersView.setObjectName("layersView")
        self.gridLayout.addWidget(self.layersView, 2, 0, 1, 3)
        self.addLayerButton = QtGui.QPushButton(self.layersTab)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ui/icons/Plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addLayerButton.setIcon(icon2)
        self.addLayerButton.setObjectName("addLayerButton")
        self.gridLayout.addWidget(self.addLayerButton, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.layersTab)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 3)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.layersTab, "")
        self.pilesTab = QtGui.QWidget()
        self.pilesTab.setObjectName("pilesTab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.pilesTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stiffnessLayout_2 = QtGui.QGridLayout()
        self.stiffnessLayout_2.setObjectName("stiffnessLayout_2")
        self.groupBox_2 = QtGui.QGroupBox(self.pilesTab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.floatPileBottomRadioButton = QtGui.QRadioButton(self.groupBox_2)
        self.floatPileBottomRadioButton.setChecked(True)
        self.floatPileBottomRadioButton.setObjectName("floatPileBottomRadioButton")
        self.verticalLayout_3.addWidget(self.floatPileBottomRadioButton)
        self.leanedPileBottomRadioButton = QtGui.QRadioButton(self.groupBox_2)
        self.leanedPileBottomRadioButton.setObjectName("leanedPileBottomRadioButton")
        self.verticalLayout_3.addWidget(self.leanedPileBottomRadioButton)
        self.cantileveredPileBottomRadioButton_2 = QtGui.QRadioButton(self.groupBox_2)
        self.cantileveredPileBottomRadioButton_2.setObjectName("cantileveredPileBottomRadioButton_2")
        self.verticalLayout_3.addWidget(self.cantileveredPileBottomRadioButton_2)
        self.gridLayout_6.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.stiffnessLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.stiffnessLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.removePileLayerButton = QtGui.QPushButton(self.pilesTab)
        self.removePileLayerButton.setIcon(icon1)
        self.removePileLayerButton.setObjectName("removePileLayerButton")
        self.gridLayout_7.addWidget(self.removePileLayerButton, 1, 2, 1, 1)
        self.pileLayersView = QtGui.QTableView(self.pilesTab)
        self.pileLayersView.setObjectName("pileLayersView")
        self.gridLayout_7.addWidget(self.pileLayersView, 2, 0, 1, 3)
        self.addLayerPileButton = QtGui.QPushButton(self.pilesTab)
        self.addLayerPileButton.setIcon(icon2)
        self.addLayerPileButton.setObjectName("addLayerPileButton")
        self.gridLayout_7.addWidget(self.addLayerPileButton, 1, 0, 1, 1)
        self.stiffnessLayout_2.addLayout(self.gridLayout_7, 1, 0, 1, 2)
        self.horizontalLayout_2.addLayout(self.stiffnessLayout_2)
        self.tabWidget.addTab(self.pilesTab, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stiffnessLayout = QtGui.QGridLayout()
        self.stiffnessLayout.setObjectName("stiffnessLayout")
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.constRadioButton = QtGui.QRadioButton(self.groupBox)
        self.constRadioButton.setChecked(True)
        self.constRadioButton.setObjectName("constRadioButton")
        self.verticalLayout_2.addWidget(self.constRadioButton)
        self.linRadioButton = QtGui.QRadioButton(self.groupBox)
        self.linRadioButton.setEnabled(False)
        self.linRadioButton.setObjectName("linRadioButton")
        self.verticalLayout_2.addWidget(self.linRadioButton)
        self.otherRadioButton = QtGui.QRadioButton(self.groupBox)
        self.otherRadioButton.setObjectName("otherRadioButton")
        self.verticalLayout_2.addWidget(self.otherRadioButton)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.stiffnessLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.stiffnessLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.stiffnessLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.stiffnessDynamicGridLayout = QtGui.QGridLayout()
        self.stiffnessDynamicGridLayout.setObjectName("stiffnessDynamicGridLayout")
        self.stiffnessLayout.addLayout(self.stiffnessDynamicGridLayout, 1, 0, 1, 2)
        self.horizontalLayout_3.addLayout(self.stiffnessLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalForceLineEdit = QtGui.QLineEdit(self.tab_2)
        self.horizontalForceLineEdit.setObjectName("horizontalForceLineEdit")
        self.gridLayout_2.addWidget(self.horizontalForceLineEdit, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.bendForceLineEdit = QtGui.QLineEdit(self.tab_2)
        self.bendForceLineEdit.setObjectName("bendForceLineEdit")
        self.gridLayout_2.addWidget(self.bendForceLineEdit, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.verticalForceLineEdit = QtGui.QLineEdit(self.tab_2)
        self.verticalForceLineEdit.setObjectName("verticalForceLineEdit")
        self.gridLayout_2.addWidget(self.verticalForceLineEdit, 2, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 3, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 2, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 2, 2, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.calculateTab = QtGui.QWidget()
        self.calculateTab.setObjectName("calculateTab")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.calculateTab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label = QtGui.QLabel(self.calculateTab)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem7, 0, 2, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem8, 3, 1, 1, 1)
        self.femLengthEdit = QtGui.QLineEdit(self.calculateTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.femLengthEdit.sizePolicy().hasHeightForWidth())
        self.femLengthEdit.setSizePolicy(sizePolicy)
        self.femLengthEdit.setMaxLength(20)
        self.femLengthEdit.setObjectName("femLengthEdit")
        self.gridLayout_8.addWidget(self.femLengthEdit, 0, 1, 1, 1)
        self.kyfootLineEdit = QtGui.QLineEdit(self.calculateTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kyfootLineEdit.sizePolicy().hasHeightForWidth())
        self.kyfootLineEdit.setSizePolicy(sizePolicy)
        self.kyfootLineEdit.setObjectName("kyfootLineEdit")
        self.gridLayout_8.addWidget(self.kyfootLineEdit, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.calculateTab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 1, 0, 1, 3)
        self.label_6 = QtGui.QLabel(self.calculateTab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.calculateTab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 2, 2, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_8)
        self.tabWidget.addTab(self.calculateTab, "")
        self.horizontalLayout_7.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAddLayer = QtGui.QAction(MainWindow)
        self.actionAddLayer.setIcon(icon2)
        self.actionAddLayer.setObjectName("actionAddLayer")
        self.actionRemove = QtGui.QAction(MainWindow)
        self.actionRemove.setIcon(icon1)
        self.actionRemove.setObjectName("actionRemove")
        self.actionSettings = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ui/icons/Settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon3)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ui/icons/Cancel 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName("actionExit")
        self.actionRun = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ui/icons/Calculator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon5)
        self.actionRun.setObjectName("actionRun")
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.addLayerButton, QtCore.SIGNAL("clicked()"), MainWindow.addLayer)
        QtCore.QObject.connect(self.removeLayerButton, QtCore.SIGNAL("clicked()"), MainWindow.removeLayer)
        QtCore.QObject.connect(self.layersView, QtCore.SIGNAL("clicked(QModelIndex)"), MainWindow.findRow)
        QtCore.QObject.connect(self.actionRun, QtCore.SIGNAL("triggered()"), MainWindow.runAction)
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), MainWindow.tabChanged)
        QtCore.QObject.connect(self.floatPileBottomRadioButton, QtCore.SIGNAL("clicked()"), MainWindow.setBC)
        QtCore.QObject.connect(self.leanedPileBottomRadioButton, QtCore.SIGNAL("clicked()"), MainWindow.setBC)
        QtCore.QObject.connect(self.cantileveredPileBottomRadioButton_2, QtCore.SIGNAL("clicked()"), MainWindow.setBC)
        QtCore.QObject.connect(self.pileLayersView, QtCore.SIGNAL("clicked(QModelIndex)"), MainWindow.findPileRow)
        QtCore.QObject.connect(self.addLayerPileButton, QtCore.SIGNAL("clicked()"), MainWindow.addPileRow)
        QtCore.QObject.connect(self.removePileLayerButton, QtCore.SIGNAL("clicked()"), MainWindow.removePileRow)
        QtCore.QObject.connect(self.bendForceLineEdit, QtCore.SIGNAL("editingFinished()"), MainWindow.sendAllStats)
        QtCore.QObject.connect(self.horizontalForceLineEdit, QtCore.SIGNAL("editingFinished()"), MainWindow.sendAllStats)
        QtCore.QObject.connect(self.verticalForceLineEdit, QtCore.SIGNAL("editingFinished()"), MainWindow.sendAllStats)
        QtCore.QObject.connect(self.femLengthEdit, QtCore.SIGNAL("editingFinished()"), MainWindow.sendAllStats)
        QtCore.QObject.connect(self.kyfootLineEdit, QtCore.SIGNAL("editingFinished()"), MainWindow.sendAllStats)
        QtCore.QObject.connect(self.otherRadioButton, QtCore.SIGNAL("clicked()"), MainWindow.tabChanged)
        QtCore.QObject.connect(self.constRadioButton, QtCore.SIGNAL("clicked()"), MainWindow.tabChanged)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "AGeo", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Výstupy N, V, M a konzole", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Deformace Ux, Uy", None, QtGui.QApplication.UnicodeUTF8))
        self.removeLayerButton.setText(QtGui.QApplication.translate("MainWindow", "Odebrat vrstvu", None, QtGui.QApplication.UnicodeUTF8))
        self.addLayerButton.setText(QtGui.QApplication.translate("MainWindow", "Přidat vrstvu", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Pokud není v parametrech piloty vybrána možnost plovoucí pilota, lze nechat hodnoty svislý pružin Ky nulové", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.layersTab), QtGui.QApplication.translate("MainWindow", "Parametry zeminy", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Model uložení paty piloty:", None, QtGui.QApplication.UnicodeUTF8))
        self.floatPileBottomRadioButton.setText(QtGui.QApplication.translate("MainWindow", "Plovoucí pata piloty", None, QtGui.QApplication.UnicodeUTF8))
        self.leanedPileBottomRadioButton.setText(QtGui.QApplication.translate("MainWindow", "Pilota opřená o skalní podloží", None, QtGui.QApplication.UnicodeUTF8))
        self.cantileveredPileBottomRadioButton_2.setText(QtGui.QApplication.translate("MainWindow", "Vetknutá pilota", None, QtGui.QApplication.UnicodeUTF8))
        self.removePileLayerButton.setText(QtGui.QApplication.translate("MainWindow", "Odebrat vrstvu", None, QtGui.QApplication.UnicodeUTF8))
        self.addLayerPileButton.setText(QtGui.QApplication.translate("MainWindow", "Přidat vrstvu", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pilesTab), QtGui.QApplication.translate("MainWindow", "Parametry piloty", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Výpočet tuhosti pružin dle:", None, QtGui.QApplication.UnicodeUTF8))
        self.constRadioButton.setText(QtGui.QApplication.translate("MainWindow", "Konstantní průběh modulu reakce", None, QtGui.QApplication.UnicodeUTF8))
        self.linRadioButton.setText(QtGui.QApplication.translate("MainWindow", "Lineární průběh (Bowles) - připraveno pro implementaci", None, QtGui.QApplication.UnicodeUTF8))
        self.otherRadioButton.setText(QtGui.QApplication.translate("MainWindow", "Vlastní hodnoty vodorovných tuhostí", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Tuhost", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalForceLineEdit.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Moment v hlavě piloty M =", None, QtGui.QApplication.UnicodeUTF8))
        self.bendForceLineEdit.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Horizontální síla v hlavě piloty H =", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Vertikální síla v hlavě piloty V=", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalForceLineEdit.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Zatížení", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Přibližná délka MKP elementů", None, QtGui.QApplication.UnicodeUTF8))
        self.femLengthEdit.setText(QtGui.QApplication.translate("MainWindow", "0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.kyfootLineEdit.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "V případě výpočtu svislých deformací plovoucí piloty je třeba zadat pružinu v patě", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Ky,paty =", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "N/m^2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.calculateTab), QtGui.QApplication.translate("MainWindow", "Parametry výpočtu", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddLayer.setText(QtGui.QApplication.translate("MainWindow", "Add Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddLayer.setToolTip(QtGui.QApplication.translate("MainWindow", "Add new layer of soil", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove.setText(QtGui.QApplication.translate("MainWindow", "Remove Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove.setToolTip(QtGui.QApplication.translate("MainWindow", "Remove layer of soil", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setToolTip(QtGui.QApplication.translate("MainWindow", "Setting up UI", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setToolTip(QtGui.QApplication.translate("MainWindow", "Exit program", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("MainWindow", "Spustit výpočet", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
