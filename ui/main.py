# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Wed Oct 19 12:05:36 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ui/icons/Rock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pilesGraphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.pilesGraphicsView.setObjectName("pilesGraphicsView")
        self.horizontalLayout.addWidget(self.pilesGraphicsView)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.layersTab = QtGui.QWidget()
        self.layersTab.setObjectName("layersTab")
        self.verticalLayout = QtGui.QVBoxLayout(self.layersTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.layersView = QtGui.QTableView(self.layersTab)
        self.layersView.setObjectName("layersView")
        self.gridLayout.addWidget(self.layersView, 2, 0, 1, 3)
        self.removeLayerButton = QtGui.QPushButton(self.layersTab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ui/icons/Minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeLayerButton.setIcon(icon1)
        self.removeLayerButton.setObjectName("removeLayerButton")
        self.gridLayout.addWidget(self.removeLayerButton, 1, 2, 1, 1)
        self.addLayerButton = QtGui.QPushButton(self.layersTab)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ui/icons/Plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addLayerButton.setIcon(icon2)
        self.addLayerButton.setObjectName("addLayerButton")
        self.gridLayout.addWidget(self.addLayerButton, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.layersTab, "")
        self.pilesTab = QtGui.QWidget()
        self.pilesTab.setObjectName("pilesTab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.pilesTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtGui.QLabel(self.pilesTab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 2, 1, 1)
        self.acceptPileButton = QtGui.QPushButton(self.pilesTab)
        self.acceptPileButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ui/icons/Checkmark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.acceptPileButton.setIcon(icon3)
        self.acceptPileButton.setObjectName("acceptPileButton")
        self.gridLayout_2.addWidget(self.acceptPileButton, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.pilesTab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.pileDiameter = QtGui.QLineEdit(self.pilesTab)
        self.pileDiameter.setObjectName("pileDiameter")
        self.gridLayout_2.addWidget(self.pileDiameter, 0, 1, 1, 1)
        self.pileHeight = QtGui.QLineEdit(self.pilesTab)
        self.pileHeight.setObjectName("pileHeight")
        self.gridLayout_2.addWidget(self.pileHeight, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.pilesTab, "")
        self.calculateTab = QtGui.QWidget()
        self.calculateTab.setObjectName("calculateTab")
        self.tabWidget.addTab(self.calculateTab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(True)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ui/icons/Settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon4)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ui/icons/Cancel 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon5)
        self.actionExit.setObjectName("actionExit")
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.addLayerButton, QtCore.SIGNAL("clicked()"), MainWindow.addLayer)
        QtCore.QObject.connect(self.removeLayerButton, QtCore.SIGNAL("clicked()"), MainWindow.removeLayer)
        QtCore.QObject.connect(self.layersView, QtCore.SIGNAL("clicked(QModelIndex)"), MainWindow.findRow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pilesGraphicsView, self.tabWidget)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "AGeo", None, QtGui.QApplication.UnicodeUTF8))
        self.removeLayerButton.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.addLayerButton.setText(QtGui.QApplication.translate("MainWindow", "Add layer", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.layersTab), QtGui.QApplication.translate("MainWindow", "Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Diameter", None, QtGui.QApplication.UnicodeUTF8))
        self.acceptPileButton.setText(QtGui.QApplication.translate("MainWindow", "Done", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pilesTab), QtGui.QApplication.translate("MainWindow", "Piles", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.calculateTab), QtGui.QApplication.translate("MainWindow", "Calculate", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddLayer.setText(QtGui.QApplication.translate("MainWindow", "Add Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddLayer.setToolTip(QtGui.QApplication.translate("MainWindow", "Add new layer of soil", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove.setText(QtGui.QApplication.translate("MainWindow", "Remove Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove.setToolTip(QtGui.QApplication.translate("MainWindow", "Remove layer of soil", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setToolTip(QtGui.QApplication.translate("MainWindow", "Setting up UI", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setToolTip(QtGui.QApplication.translate("MainWindow", "Exit program", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
