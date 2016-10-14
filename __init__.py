import sys
from PySide import QtGui, QtCore
import mainWindow as m


def main():
    application = QtGui.QApplication(sys.argv)
    mainWnd = m.MainWindow()
    mainWnd.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
