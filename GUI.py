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
        self.swap_button = QtWidgets.QPushButton(self.centralwidget)
        self.photo_display_info_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.save_path_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.model_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.stats_detected_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.stats_questionable_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.stats_total_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.stats_total_info_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.stats_questionable_info_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.stats_detected_info_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.mark_with_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_path_lineEdit = QtWidgets.QLineEdit(self.centralwidget)

        # self.centralwidget.setStyleSheet("background-color: lightblue;")
        """ Non GUI-specific variables"""
        self.confident_photos = []
        self.questionable_photos = []
        self.curr_photo = 0
        self.current_photos = None
        self.marked_with_array = []
        self.marked_without_array = []



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
        self.stats_detected_info_lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.stats_detected_info_lineEdit.setReadOnly(True)
        self.stats_detected_info_lineEdit.setObjectName("n_detected_info_lineEdit")
        self.stats_questionable_info_lineEdit.setGeometry(QtCore.QRect(10, 60, 113, 20))
        self.stats_questionable_info_lineEdit.setReadOnly(True)
        self.stats_questionable_info_lineEdit.setObjectName("n_questionable_info_lineEdit")
        self.stats_total_info_lineEdit.setGeometry(QtCore.QRect(10, 90, 113, 20))
        self.stats_total_info_lineEdit.setReadOnly(True)
        self.stats_total_info_lineEdit.setObjectName("n_all_info_lineEdit")
        self.stats_total_lineEdit.setGeometry(QtCore.QRect(130, 90, 113, 20))
        self.stats_total_lineEdit.setReadOnly(True)
        self.stats_total_lineEdit.setObjectName("n_info_lineEdit")
        self.stats_questionable_lineEdit.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.stats_questionable_lineEdit.setReadOnly(True)
        self.stats_questionable_lineEdit.setObjectName("n_questionable_lineEdit")
        self.stats_detected_lineEdit.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.stats_detected_lineEdit.setReadOnly(True)
        self.stats_detected_lineEdit.setObjectName("n_detected_lineEdit")
        self.model_comboBox.setGeometry(QtCore.QRect(20, 110, 261, 21))
        self.model_comboBox.setObjectName("model_comboBox")
        for _ in os.listdir("models"):
            self.model_comboBox.addItem("")
        self.save_path_lineEdit.setGeometry(QtCore.QRect(780, 610, 241, 41))
        self.save_path_lineEdit.setObjectName("save_path_lineEdit")
        self.photo_display_info_lineEdit.setGeometry(QtCore.QRect(790, 20, 101, 20))
        self.photo_display_info_lineEdit.setReadOnly(True)
        self.photo_display_info_lineEdit.setObjectName("photo_display_info_lineEdit")
        self.next_button.setGeometry(QtCore.QRect(850, 440, 151, 41))
        self.next_button.setObjectName("next_button")
        self.prev_button.setGeometry(QtCore.QRect(690, 440, 151, 41))
        self.prev_button.setObjectName("prev_button")
        self.swap_button.setGeometry(QtCore.QRect(600, 440, 81, 41))
        self.swap_button.setObjectName("swap_button")
        self.photo_display.setGeometry(QtCore.QRect(590, 50, 491, 381))
        self.photo_display.setText("")
        self.photo_display.setPixmap(QtGui.QPixmap())
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
        self.stats_detected_info_lineEdit.setText(_translate("MainWindow", "Liczba znalezionych:"))
        self.stats_questionable_info_lineEdit.setText(_translate("MainWindow", "Liczba wątpliwych:"))
        self.stats_total_info_lineEdit.setText(_translate("MainWindow", "Liczba wszystkich:"))
        self.stats_total_lineEdit.setText(_translate("MainWindow", "-"))
        self.stats_questionable_lineEdit.setText(_translate("MainWindow", "-"))
        self.stats_detected_lineEdit.setText(_translate("MainWindow", "-"))
        for i, file in enumerate(os.listdir("models")):
            self.model_comboBox.setItemText(i, _translate("MainWindow", file))
        self.save_path_lineEdit.setText(_translate("MainWindow", "C:\\Users\\Ja\\Desktop\\SelectedFacesGallery"))
        self.photo_display_info_lineEdit.setText(_translate("MainWindow", "Podgląd zdjęcia"))
        self.next_button.setText(_translate("MainWindow", "Następne"))
        self.swap_button.setText(_translate("MainWindow", "Zmień galerię"))
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

        # self.save_path_button.setStyleSheet("background-color : lightblue")

        filenames = os.listdir("models")
        for i, file in enumerate(filenames):
            self.model_comboBox.setItemText(i, _translate("MainWindow", file))

        # self.save_path_button.setStyleSheet("background-color : lightgreen")
        self.next_button.clicked.connect(self._next_photo)
        self.prev_button.clicked.connect(self._prev_photo)
        self.save_button.clicked.connect(self._save_photos_to_dir)
        self.save_path_button.clicked.connect(self._set_save_path)
        self.load_path_button.clicked.connect(self._set_load_path)
        self.mark_with_button.clicked.connect(self._marked_with)
        self.mark_without_button.clicked.connect(self._marked_without)
        self.swap_button.clicked.connect(self._swap_gallery)
        self.update_gallery_text()
        self.update_stats()

    def _save_photos_to_dir(self):
        """
        Handler method for save_button.
        Saves to currently written path in "Save Path" lineEdit field.
        """
        save_path = self.save_path_lineEdit.text()
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        for photo in self.confident_photos:
            folder_path = os.path.join(save_path, os.path.basename(photo))
            shutil.copyfile(photo, folder_path)

    def _set_load_path(self):
        """
        Method to choose starting dataset using FileDialog. Updates load_path_info_lineEdit
        """
        path = str(QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, 'Select Folder'))
        self.load_path_lineEdit.setText(path)

    def _set_save_path(self):
        """
        Method to choose writing location for selected photos using FileDialog. Updates "save_path" lineEdit
        """
        path = str(QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, 'Select Folder'))
        self.save_path_lineEdit.setText(path)

    def _next_photo(self):
        """
        Handler method for next_button
        """
        if len(self.current_photos) == 0:
            return

        self.curr_photo = (self.curr_photo + 1) % len(self.current_photos)
        photo = self.current_photos[self.curr_photo]
        self.photo_display.setPixmap(QtGui.QPixmap(photo))

    def _prev_photo(self):
        """
        Handler method for prev_button
        """
        if len(self.current_photos) == 0:
            return

        self.curr_photo = (self.curr_photo - 1) % len(self.current_photos)
        photo = self.current_photos[self.curr_photo]
        self.photo_display.setPixmap(QtGui.QPixmap(photo))

    def update_gallery_text(self):
        if self.current_photos == self.confident_photos:
            self.photo_display_info_lineEdit.setText("Pewne zdjęcia")
        elif self.current_photos == self.questionable_photos:
            self.photo_display_info_lineEdit.setText("Niepewne zdjęcia")
        else:
            self.photo_display_info_lineEdit.setText("Brak zdjęć")  # Do przetestowania

    def _swap_gallery(self):
        """
        Handler method for swap_button
        """
        if self.current_photos == self.confident_photos:
            self.current_photos = self.questionable_photos
        else:
            self.current_photos = self.confident_photos

        if len(self.current_photos) == 0:
            self.photo_display.setPixmap(QtGui.QPixmap())

        self.update_gallery_text()

    def update_confident_photos(self, photos):
        """
        Update photos array that gallery uses.
        :param photos: array of photo paths
        """
        if isinstance(photos, list):
            self.confident_photos = photos
            self.current_photos = self.confident_photos
        else:
            raise TypeError("To update photos array pass array of photo paths")

    def update_questionable_photos(self, photos):
        """
        Update photos array that gallery uses.
        :param photos: array of photo paths
        """
        if isinstance(photos, list):
            self.questionable_photos = photos
            self.current_photos = self.questionable_photos
        else:
            raise TypeError("To update photos array pass array of photo paths")

    def get_parameter_1(self):
        """
        Getter for parameter 1
        """
        return self.param_1_lineEdit.text()

    def get_parameter_2(self):
        """
        Getter for parameter 2
        """
        return self.param_2_info_lineEdit.text()

    def get_model_type(self):
        """
        Getter for model type
        """
        return self.model_comboBox.currentText()

    def get_load_path(self):
        """
        Getter for directory path with photos to use in algorithm
        """
        return self.save_path_lineEdit.text()

    def update_stats(self):
        """
        Updating statistics lineEdits
        """
        self.stats_detected_lineEdit.setText(str(len(self.confident_photos)))
        self.stats_questionable_lineEdit.setText(str(len(self.questionable_photos)))
        self.stats_total_lineEdit.setText(str(len(self.questionable_photos) + len(self.confident_photos)))

    def _marked_with(self):
        """
        Handler for mark_with_button
        """
        photo = self.confident_photos[self.curr_photo]
        if photo not in self.marked_with_array:
            self.marked_with_array.append(photo)

    def _marked_without(self):
        """
        Handler for mark_without_button
        """
        photo = self.confident_photos[self.curr_photo]
        if photo not in self.marked_without_array:
            self.marked_without_array.append(photo)


if __name__ == "__main__":
    import sys

    photos = []
    for (dir_path, dir_names, filenames) in os.walk("photos"):
        for file in filenames:
            photos.append(os.path.join(dir_path, file))

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.update_confident_photos(photos)
    MainWindow.show()
    sys.exit(app.exec_())
