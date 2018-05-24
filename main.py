import sys
from gsui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__ (self, parent = None):
        super (MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi (self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    m = MainWindow()
    m.show()
    sys.exit (app.exec_())


if __name__ == '__main__':
    main ()