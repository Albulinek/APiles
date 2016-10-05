import sys
from PySide import QtGui, QtCore
import ui.main as mainWindow


class AGeo(QtGui.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)


def main():
    application = QtGui.QApplication(sys.argv)
    mainWnd = AGeo()
    mainWnd.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()