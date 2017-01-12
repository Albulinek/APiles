# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/start.ui'
#
# Created: Tue Jan 10 14:28:12 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_StartDialog(object):
    def setupUi(self, StartDialog):
        StartDialog.setObjectName("StartDialog")
        StartDialog.resize(382, 101)
        StartDialog.setMinimumSize(QtCore.QSize(382, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ui/icons/Rock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StartDialog.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(StartDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtGui.QPushButton(StartDialog)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.MasopustPileButton = QtGui.QPushButton(StartDialog)
        self.MasopustPileButton.setObjectName("MasopustPileButton")
        self.verticalLayout.addWidget(self.MasopustPileButton)
        self.HorizontalPileButton = QtGui.QPushButton(StartDialog)
        self.HorizontalPileButton.setObjectName("HorizontalPileButton")
        self.verticalLayout.addWidget(self.HorizontalPileButton)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(StartDialog)
        QtCore.QObject.connect(self.HorizontalPileButton, QtCore.SIGNAL("clicked()"), StartDialog.openHorizontalPiles)
        QtCore.QObject.connect(self.MasopustPileButton, QtCore.SIGNAL("clicked()"), StartDialog.openMasopustPiles)
        QtCore.QMetaObject.connectSlotsByName(StartDialog)

    def retranslateUi(self, StartDialog):
        StartDialog.setWindowTitle(QtGui.QApplication.translate("StartDialog", "Zvolte typ výpočtu...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("StartDialog", "Dle EN (připraveno pro implementaci)", None, QtGui.QApplication.UnicodeUTF8))
        self.MasopustPileButton.setText(QtGui.QApplication.translate("StartDialog", "Pilota dle Masopusta", None, QtGui.QApplication.UnicodeUTF8))
        self.HorizontalPileButton.setText(QtGui.QApplication.translate("StartDialog", "Horizontálně zatížená pilota", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
