from PyQt5 import QtCore, QtGui, QtWidgets
import os
import shutil

class Ui_MainWindow(object):
    def __init__(self):
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.stats_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.save_path_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_path_button = QtWidgets.QPushButton(self.centralwidget)
        self.param_2_info_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.param_1_info_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.param_2_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.param_1_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.save_info_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.load_path_info_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.mark_without_button = QtWidgets.QPushButton(self.centralwidget)
        self.photo_display = QtWidgets.QLabel(self.centralwidget)
        self.prev_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.photo_display_info_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.save_path_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.model_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.n_found_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.n_questionable_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.n_info_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.n_all_info_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.n_questionable_info_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.n_found_info_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.mark_with_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_path_lineEdit = QtWidgets.QLineEdit(self.centralwidget)


        """ Non GUI-specific variables"""
        self.gallery_array = []
        self.curr_photo = 0
        self.gallery_path = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 710)
        self.centralwidget.setObjectName("centralwidget")
        self.load_path_lineEdit.setGeometry(QtCore.QRect(20, 50, 261, 41))
        self.load_path_lineEdit.setReadOnly(False)
        self.load_path_lineEdit.setObjectName("read_path_lineEdit")
        self.mark_with_button.setGeometry(QtCore.QRect(850, 490, 151, 41))
        self.mark_with_button.setObjectName("mark_with_button")
        self.start_button.setGeometry(QtCore.QRect(370, 50, 111, 41))
        self.start_button.setObjectName("start_button")
        self.save_button.setGeometry(QtCore.QRect(690, 610, 71, 41))
        self.save_button.setObjectName("save_button")
        self.stats_groupBox.setGeometry(QtCore.QRect(20, 400, 251, 251))
        self.stats_groupBox.setObjectName("stats_groupBox")
        self.n_found_info_lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.n_found_info_lineEdit.setReadOnly(True)
        self.n_found_info_lineEdit.setObjectName("n_found_info_lineEdit")
        self.n_questionable_info_lineEdit.setGeometry(QtCore.QRect(10, 60, 113, 20))
        self.n_questionable_info_lineEdit.setReadOnly(True)
        self.n_questionable_info_lineEdit.setObjectName("n_questionable_info_lineEdit")
        self.n_all_info_lineEdit.setGeometry(QtCore.QRect(10, 90, 113, 20))
        self.n_all_info_lineEdit.setReadOnly(True)
        self.n_all_info_lineEdit.setObjectName("n_all_info_lineEdit")
        self.n_info_lineEdit.setGeometry(QtCore.QRect(130, 90, 113, 20))
        self.n_info_lineEdit.setReadOnly(True)
        self.n_info_lineEdit.setObjectName("n_info_lineEdit")
        self.n_questionable_lineEdit.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.n_questionable_lineEdit.setReadOnly(True)
        self.n_questionable_lineEdit.setObjectName("n_questionable_lineEdit")
        self.n_found_lineEdit.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.n_found_lineEdit.setReadOnly(True)
        self.n_found_lineEdit.setObjectName("n_found_lineEdit")
        self.model_comboBox.setGeometry(QtCore.QRect(20, 110, 261, 21))
        self.model_comboBox.setObjectName("model_comboBox")
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.save_path_lineEdit.setGeometry(QtCore.QRect(780, 610, 241, 41))
        self.save_path_lineEdit.setObjectName("save_path_lineEdit")
        self.photo_display_info_lineEdit.setGeometry(QtCore.QRect(790, 20, 81, 20))
        self.photo_display_info_lineEdit.setReadOnly(True)
        self.photo_display_info_lineEdit.setObjectName("photo_display_info_lineEdit")
        self.next_button.setGeometry(QtCore.QRect(850, 440, 151, 41))
        self.next_button.setObjectName("next_button")
        self.prev_button.setGeometry(QtCore.QRect(690, 440, 151, 41))
        self.prev_button.setObjectName("prev_button")
        self.photo_display.setGeometry(QtCore.QRect(590, 50, 491, 381))
        self.photo_display.setText("")
        self.photo_display.setPixmap(QtGui.QPixmap("other/indeks.png"))  # white photo just to show something at start
        self.photo_display.setScaledContents(True)
        self.photo_display.setObjectName("photo_display")
        self.mark_without_button.setGeometry(QtCore.QRect(690, 490, 151, 41))
        self.mark_without_button.setObjectName("mark_without_button")
        self.load_path_info_lineEdit.setGeometry(QtCore.QRect(70, 20, 161, 20))
        self.load_path_info_lineEdit.setReadOnly(True)
        self.load_path_info_lineEdit.setObjectName("load_path_info_lineEdit")
        self.save_info_lineEdit.setGeometry(QtCore.QRect(800, 580, 201, 20))
        self.save_info_lineEdit.setReadOnly(True)
        self.save_info_lineEdit.setObjectName("save_info_lineEdit")
        self.param_1_lineEdit.setGeometry(QtCore.QRect(120, 160, 161, 31))
        self.param_1_lineEdit.setReadOnly(False)
        self.param_1_lineEdit.setObjectName("param_1_lineEdit")
        self.param_2_lineEdit.setGeometry(QtCore.QRect(120, 210, 161, 31))
        self.param_2_lineEdit.setReadOnly(False)
        self.param_2_lineEdit.setObjectName("param_2_lineEdit_2")
        self.param_1_info_lineEdit.setGeometry(QtCore.QRect(20, 160, 91, 31))
        self.param_1_info_lineEdit.setReadOnly(True)
        self.param_1_info_lineEdit.setObjectName("param_1_info_lineEdit")
        self.param_2_info_lineEdit.setGeometry(QtCore.QRect(20, 210, 91, 31))
        self.param_2_info_lineEdit.setReadOnly(True)
        self.param_2_info_lineEdit.setObjectName("param_2_lineEdit")
        self.load_path_button.setGeometry(QtCore.QRect(290, 50, 51, 41))
        self.load_path_button.setObjectName("load_path_button")
        self.save_path_button.setGeometry(QtCore.QRect(1030, 610, 51, 41))
        self.save_path_button.setObjectName("save_path_button")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.load_path_lineEdit.setText(_translate("MainWindow", "C:\\Users\\Ja\\Desktop\\MyGallery"))
        self.mark_with_button.setText(_translate("MainWindow", "Oznacz jako z elementem"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.save_button.setText(_translate("MainWindow", "Zapisz"))
        self.stats_groupBox.setTitle(_translate("MainWindow", "Statystyki zdjęć"))
        self.n_found_info_lineEdit.setText(_translate("MainWindow", "Liczba znalezionych:"))
        self.n_questionable_info_lineEdit.setText(_translate("MainWindow", "Liczba wątpliwych:"))
        self.n_all_info_lineEdit.setText(_translate("MainWindow", "Liczba wszystkich:"))
        self.n_info_lineEdit.setText(_translate("MainWindow", "-"))
        self.n_questionable_lineEdit.setText(_translate("MainWindow", "-"))
        self.n_found_lineEdit.setText(_translate("MainWindow", "-"))
        self.model_comboBox.setItemText(0, _translate("MainWindow", "Wybierz model"))
        self.model_comboBox.setItemText(1, _translate("MainWindow", "Twarze"))
        self.model_comboBox.setItemText(2, _translate("MainWindow", "Samochody"))
        self.model_comboBox.setItemText(3, _translate("MainWindow", "Rowery"))
        self.save_path_lineEdit.setText(_translate("MainWindow", "C:\\Users\\Ja\\Desktop\\SelectedFacesGallery"))
        self.photo_display_info_lineEdit.setText(_translate("MainWindow", "Podgląd zdjęcia"))
        self.next_button.setText(_translate("MainWindow", "Następne"))
        self.prev_button.setText(_translate("MainWindow", "Poprzednie"))
        self.mark_without_button.setText(_translate("MainWindow", "Oznacz jako bez elementu"))
        self.load_path_info_lineEdit.setText(_translate("MainWindow", "Ścieżka do folderu ze zdjęciami:"))
        self.save_info_lineEdit.setText(_translate("MainWindow", "Ścieżka do zapisania znalezionych zdjęć:"))
        self.param_1_lineEdit.setText(_translate("MainWindow", "80"))
        self.param_2_lineEdit.setText(_translate("MainWindow", "20"))
        self.param_1_info_lineEdit.setText(_translate("MainWindow", "Parametr 1 (%):"))
        self.param_2_info_lineEdit.setText(_translate("MainWindow", "Parametr 2:"))
        self.load_path_button.setText(_translate("MainWindow", "..."))
        self.save_path_button.setText(_translate("MainWindow", "..."))

        self.next_button.clicked.connect(self._next_photo)
        self.prev_button.clicked.connect(self._prev_photo)
        self.save_button.clicked.connect(self.save_photos_to_dir)
        self.save_path_button.clicked.connect(self._set_save_path)
        self.load_path_button.clicked.connect(self._set_load_path)

    def save_photos_to_dir(self):
        """
        Handler method for save_button.
        Saves to currently written path in "Save Path" lineEdit field.
        :return:
        """
        save_path = self.save_path_lineEdit.text()
        if not os.path.exists(save_path): # TODO: Photos copy only after closing GUI not right after pressing the button
            os.makedirs(save_path)
        for photo in self.gallery_array:
            folder_path = os.path.join(save_path, os.path.basename(photo))
            shutil.copyfile(photo, folder_path)

    def _next_photo(self):
        """
        Handler method for next_button
        :return:
        """
        if len(self.gallery_array) == 0:
            return

        self.curr_photo = (self.curr_photo + 1) % len(self.gallery_array)
        photo = self.gallery_array[self.curr_photo]
        self.photo_display.setPixmap(QtGui.QPixmap(photo))

    def _prev_photo(self):
        """
        Handler method for prev_button
        :return:
        """
        if len(self.gallery_array) == 0:
            return

        self.curr_photo = (self.curr_photo - 1) % len(self.gallery_array)
        photo = self.gallery_array[self.curr_photo]
        self.photo_display.setPixmap(QtGui.QPixmap(photo))

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
            raise TypeError("To update photos array pass either array of photo paths or directory path")

    def get_parameter_1(self):
        """
        Getter for parameter 1
        :return: Parameter 1 value as int
        """
        return self.param_1_lineEdit.text()

    def get_parameter_2(self):
        """
        Getter for parameter 2
        :return: Parameter 2 value as int
        """
        return self.param_2_info_lineEdit.text()

    def get_model_type(self):
        """
        Getter for model type
        :return: Model type as string
        """
        return self.model_comboBox.currentText()

    def _set_load_path(self):
        """
        Method to choose starting dataset using FileDialog. Updates load_path_info_lineEdit
        :return:
        """
        path = str(QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, 'Select Folder'))
        self.load_path_lineEdit.setText(path)

    def _set_save_path(self):
        """
        Method to choose writing location for selected photos using FileDialog. Updates "save_path" lineEdit
        :return:
        """
        path = str(QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, 'Select Folder'))
        self.save_path_lineEdit.setText(path)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.update_photos_array("photos")
    MainWindow.show()
    sys.exit(app.exec_())
