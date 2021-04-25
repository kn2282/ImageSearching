import os
import shutil
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton('self.centralwidget')
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)

        """ Non GUI-specific variables"""
        self.gallery_array = []
        self.curr_photo = 0
        self.gallery_path = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 710)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 261, 31))
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton.setGeometry(QtCore.QRect(810, 420, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2.setGeometry(QtCore.QRect(360, 50, 181, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3.setGeometry(QtCore.QRect(750, 530, 91, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox.setGeometry(QtCore.QRect(20, 400, 251, 251))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 60, 113, 20))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 90, 113, 20))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_16.setGeometry(QtCore.QRect(130, 90, 113, 20))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.comboBox.setGeometry(QtCore.QRect(20, 110, 261, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_2.setGeometry(QtCore.QRect(850, 540, 241, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_6.setGeometry(QtCore.QRect(760, 20, 81, 20))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton1.setGeometry(QtCore.QRect(810, 360, 151, 41))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton_21.setGeometry(QtCore.QRect(640, 360, 151, 41))
        self.pushButton_21.setObjectName("pushButton_21")
        self.label.setGeometry(QtCore.QRect(610, 50, 381, 301))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_4.setGeometry(QtCore.QRect(640, 420, 151, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_7.setGeometry(QtCore.QRect(70, 20, 161, 20))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8.setGeometry(QtCore.QRect(870, 510, 201, 20))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9.setGeometry(QtCore.QRect(120, 160, 161, 31))
        self.lineEdit_9.setReadOnly(False)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10.setGeometry(QtCore.QRect(120, 210, 161, 31))
        self.lineEdit_10.setReadOnly(False)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11.setGeometry(QtCore.QRect(20, 160, 91, 31))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12.setGeometry(QtCore.QRect(20, 210, 91, 31))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1116, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ML photo search algorithm GUI"))
        self.lineEdit.setText(_translate("MainWindow", "C:\\Users\\Ja\\Desktop\\MyGallery"))
        self.pushButton.setText(_translate("MainWindow", "Oznacz jako z elementem"))
        self.pushButton_2.setText(_translate("MainWindow", "..."))
        self.pushButton_3.setText(_translate("MainWindow", "Zapisz"))
        self.groupBox.setTitle(_translate("MainWindow", "Statystyki zdjęć"))
        self.lineEdit_3.setText(_translate("MainWindow", "Liczba znalezionych:"))
        self.lineEdit_4.setText(_translate("MainWindow", "Liczba wątpliwych:"))
        self.lineEdit_5.setText(_translate("MainWindow", "Liczba wszystkich:"))
        self.lineEdit_16.setText(_translate("MainWindow", "-"))
        self.lineEdit_17.setText(_translate("MainWindow", "-"))
        self.lineEdit_18.setText(_translate("MainWindow", "-"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Wybierz model"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Twarze"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Samochody"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Rowery"))
        self.lineEdit_6.setText(_translate("MainWindow", "Podgląd zdjęcia"))
        self.pushButton1.setText(_translate("MainWindow", "Następne"))
        self.pushButton_21.setText(_translate("MainWindow", "Poprzednie"))
        self.lineEdit_2.setText(_translate("MainWindow", "ResultDataSet"))
        self.pushButton_4.setText(_translate("MainWindow", "..."))
        self.lineEdit_7.setText(_translate("MainWindow", "Ścieżka do folderu ze zdjęciami:"))
        self.lineEdit_8.setText(_translate("MainWindow", "Ścieżka do zapisania znalezionych zdjęć:"))
        self.lineEdit_9.setText(_translate("MainWindow", "80"))
        self.lineEdit_10.setText(_translate("MainWindow", "20"))
        self.lineEdit_11.setText(_translate("MainWindow", "Parametr 1 (%):"))
        self.lineEdit_12.setText(_translate("MainWindow", "Parametr 2:"))

        self.pushButton1.clicked.connect(self._next_photo)
        self.pushButton_21.clicked.connect(self._prev_photo)
        self.pushButton_3.clicked.connect(self.save_photos_to_dir)
        self.pushButton_4.clicked.connect(self._set_save_path)
        self.pushButton_2.clicked.connect(self._set_read_path)

    def save_photos_to_dir(self):
        """
        Handler method for "Save" button.
        Saves to currently written path in "Save Path" lineEdit field.
        :return:
        """
        save_path = self.lineEdit_2.text()
        if not os.path.exists(save_path): # TODO: Photos copy only after closing GUI not right after pressing the button
            os.makedirs(save_path)
        for photo in self.gallery_array:
            folder_path = os.path.join(save_path, os.path.basename(photo))
            shutil.copyfile(photo, folder_path)

    def _next_photo(self):
        """
        Handler method for "next" button
        :return:
        """
        if len(self.gallery_array) == 0:
            return

        self.curr_photo = (self.curr_photo + 1) % len(self.gallery_array)
        photo = self.gallery_array[self.curr_photo]
        self.label.setPixmap(QtGui.QPixmap(photo))

    def _prev_photo(self):
        """
        Handler method for "previous" button
        :return:
        """
        if len(self.gallery_array) == 0:
            return

        self.curr_photo = (self.curr_photo - 1) % len(self.gallery_array)
        photo = self.gallery_array[self.curr_photo]
        self.label.setPixmap(QtGui.QPixmap(photo))

    def update_photos_array(self, photos):
        """
        Update photos array that gallery uses.
        :param photos: array of photo paths or directory path to folder with photos
        :return:
        """
        if isinstance(photos, list):
            self.gallery_array = photos
        elif os.path.isdir(photos):
            photos_path = photos
            self.gallery_array = []
            for (dir_path, dir_names, filenames) in os.walk(photos_path):
                for file in filenames:
                    self.gallery_array.append(os.path.join(dir_path, file))
        else:
            raise ValueError("To update photos array pass either array of photo paths or directory path")

    def get_parameter_1(self):
        """
        Getter for parameter 1
        :return: Parameter 1 value as int
        """
        return self.lineEdit_9.text()

    def get_parameter_2(self):
        """
        Getter for parameter 2
        :return: Parameter 2 value as int
        """
        return self.lineEdit_10.text()

    def get_model_type(self):
        """
        Getter for model type
        :return: Model type as string
        """
        return self.comboBox.currentText()

    def _set_read_path(self):
        """
        Method to choose starting dataset using FileDialog. Updates "read_path" lineEdit
        :return:
        """
        path = str(QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, 'Select Folder'))
        self.lineEdit.setText(path)

    def _set_save_path(self):
        """
        Method to choose writing location for selected photos using FileDialog. Updates "save_path" lineEdit
        :return:
        """
        path = str(QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, 'Select Folder'))
        self.lineEdit_2.setText(path)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.update_photos_array("photos")
    MainWindow.show()
    sys.exit(app.exec_())
