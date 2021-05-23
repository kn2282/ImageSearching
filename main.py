from GUI import Ui_MainWindow
from ModelDetector import ModelDetector
import os
from ImageSearcher import ImageSearcher, SearchAlgorithm, AlgorithmType
import SetSearcher

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from SetSearcher import SearchSet
import sys
from PyQt5 import QtWidgets

if __name__ == "__main__":

    photos = []
    for (dir_path, dir_names, filenames) in os.walk("photos"):
        for file in filenames:
            photos.append(os.path.join(dir_path, file))

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi(MainWindow)

    ui.update_confident_photos(photos)

    MainWindow.show()

    sys.exit(app.exec_())
