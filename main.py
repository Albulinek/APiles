import sys
from PySide import QtGui, QtCore, QtSql
import mainDialog as d

def main():
    application = QtGui.QApplication(sys.argv)

    mainWnd = d.MainDialog()
    mainWnd.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
