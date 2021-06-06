from GUI import Ui_MainWindow
import os
import sys
from PyQt5 import QtWidgets

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())
