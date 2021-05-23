from PyQt5 import QtCore, QtGui, QtWidgets
import os
import shutil

from SetSearcher import SearchSet


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.stats_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.save_path_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_path_button = QtWidgets.QPushButton(self.centralwidget)
        self.max_depth_info_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.confidence_info_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.max_depth_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.confidence_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
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
        self.alg_type_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.stats_detected_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.stats_undetected_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.stats_total_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.stats_total_info_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.stats_undetected_info_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.stats_detected_info_lineEdit = QtWidgets.QLineEdit(self.stats_groupBox)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.mark_with_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_path_lineEdit = QtWidgets.QLineEdit(self.centralwidget)

        # self.centralwidget.setStyleSheet("background-color: lightblue;")
        """ Non GUI-specific variables"""
        self.detected_photos = []  # array of absolute paths
        self.undetected_photos = []
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
        self.mark_without_button.setGeometry(QtCore.QRect(690, 490, 151, 41))
        self.mark_without_button.setObjectName("mark_without_button")
        self.start_button.setGeometry(QtCore.QRect(370, 50, 111, 41))
        self.start_button.setObjectName("start_button")
        self.save_button.setGeometry(QtCore.QRect(600, 610, 81, 41))
        self.save_button.setObjectName("save_button")
        self.stats_groupBox.setGeometry(QtCore.QRect(20, 400, 261, 251))
        self.stats_groupBox.setObjectName("stats_groupBox")
        self.stats_detected_info_lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.stats_detected_info_lineEdit.setReadOnly(True)
        self.stats_detected_info_lineEdit.setObjectName("n_detected_info_lineEdit")
        self.stats_undetected_info_lineEdit.setGeometry(QtCore.QRect(10, 60, 113, 20))
        self.stats_undetected_info_lineEdit.setReadOnly(True)
        self.stats_undetected_info_lineEdit.setObjectName("n_undetected_info_lineEdit")
        self.stats_total_info_lineEdit.setGeometry(QtCore.QRect(10, 90, 113, 20))
        self.stats_total_info_lineEdit.setReadOnly(True)
        self.stats_total_info_lineEdit.setObjectName("n_total_info_lineEdit")
        self.stats_total_lineEdit.setGeometry(QtCore.QRect(130, 90, 113, 20))
        self.stats_total_lineEdit.setReadOnly(True)
        self.stats_total_lineEdit.setObjectName("n_total_lineEdit")
        self.stats_undetected_lineEdit.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.stats_undetected_lineEdit.setReadOnly(True)
        self.stats_undetected_lineEdit.setObjectName("n_questionable_lineEdit")
        self.stats_detected_lineEdit.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.stats_detected_lineEdit.setReadOnly(True)
        self.stats_detected_lineEdit.setObjectName("n_detected_lineEdit")
        self.save_path_lineEdit.setGeometry(QtCore.QRect(690, 610, 311, 41))
        self.save_path_lineEdit.setObjectName("save_path_lineEdit")
        self.photo_display_info_lineEdit.setGeometry(QtCore.QRect(750, 20, 151, 20))
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
        self.load_path_info_lineEdit.setGeometry(QtCore.QRect(70, 20, 161, 20))
        self.load_path_info_lineEdit.setReadOnly(True)
        self.load_path_info_lineEdit.setObjectName("load_path_info_lineEdit")
        self.save_info_lineEdit.setGeometry(QtCore.QRect(690, 580, 311, 20))
        self.save_info_lineEdit.setReadOnly(True)
        self.save_info_lineEdit.setObjectName("save_info_lineEdit")
        self.confidence_lineEdit.setGeometry(QtCore.QRect(180, 160, 101, 31))
        self.confidence_lineEdit.setReadOnly(False)
        self.confidence_lineEdit.setObjectName("confidence_lineEdit")
        self.max_depth_lineEdit.setGeometry(QtCore.QRect(180, 210, 101, 31))
        self.max_depth_lineEdit.setReadOnly(False)
        self.max_depth_lineEdit.setObjectName("max_depth_lineEdit_2")
        self.confidence_info_lineEdit.setGeometry(QtCore.QRect(20, 160, 151, 31))
        self.confidence_info_lineEdit.setReadOnly(True)
        self.confidence_info_lineEdit.setObjectName("confidence_info_lineEdit")
        self.max_depth_info_lineEdit.setGeometry(QtCore.QRect(20, 210, 151, 31))
        self.max_depth_info_lineEdit.setReadOnly(True)
        self.max_depth_info_lineEdit.setObjectName("max_depth_lineEdit")
        self.load_path_button.setGeometry(QtCore.QRect(290, 50, 51, 41))
        self.load_path_button.setObjectName("load_path_button")
        self.save_path_button.setGeometry(QtCore.QRect(1020, 610, 51, 41))
        self.save_path_button.setObjectName("save_path_button")
        self.alg_type_comboBox.setGeometry(QtCore.QRect(20, 275, 261, 21))
        self.alg_type_comboBox.setObjectName("alg_type_comboBox")
        self.alg_type_comboBox.addItem("HALF.IMAGES")
        self.alg_type_comboBox.addItem("QUARTER.IMAGES")
        self.model_comboBox.setGeometry(QtCore.QRect(20, 110, 261, 21))
        self.model_comboBox.setObjectName("model_comboBox")
        for filename in os.listdir("models"):
            self.model_comboBox.addItem(filename)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Photos searching"))
        self.load_path_lineEdit.setText(_translate("MainWindow", "C:\\Users\\Ja\\Desktop\\MyGallery"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.stats_groupBox.setTitle(_translate("MainWindow", "Search statistics"))
        self.stats_detected_info_lineEdit.setText(_translate("MainWindow", "Detected no:"))
        self.stats_undetected_info_lineEdit.setText(_translate("MainWindow", "Undetected no:"))
        self.stats_total_info_lineEdit.setText(_translate("MainWindow", "All photos no:"))
        self.stats_total_lineEdit.setText(_translate("MainWindow", "-"))
        self.stats_undetected_lineEdit.setText(_translate("MainWindow", "-"))
        self.stats_detected_lineEdit.setText(_translate("MainWindow", "-"))
        self.save_path_lineEdit.setText(_translate("MainWindow", "C:\\Users\\Ja\\Desktop\\SelectedFacesGallery"))
        self.photo_display_info_lineEdit.setText(_translate("MainWindow", "Photo preview"))
        self.next_button.setText(_translate("MainWindow", "Next"))
        self.swap_button.setText(_translate("MainWindow", "Swap gallery"))
        self.prev_button.setText(_translate("MainWindow", "Previous"))
        self.mark_with_button.setText(_translate("MainWindow", "Mark with"))
        self.mark_without_button.setText(_translate("MainWindow", "Mark without"))
        self.load_path_info_lineEdit.setText(_translate("MainWindow", "Path to load photos:"))
        self.save_info_lineEdit.setText(_translate("MainWindow", "Path to save detected photos:"))
        self.confidence_lineEdit.setText(_translate("MainWindow", "0.8"))
        self.max_depth_lineEdit.setText(_translate("MainWindow", "4"))
        self.confidence_info_lineEdit.setText(_translate("MainWindow", "Confidence (0-1):"))
        self.max_depth_info_lineEdit.setText(_translate("MainWindow", "Max depth:"))
        self.load_path_button.setText(_translate("MainWindow", "..."))
        self.save_path_button.setText(_translate("MainWindow", "..."))

        # self.save_path_button.setStyleSheet("background-color : lightblue")
        self.next_button.clicked.connect(self._next_photo)
        self.prev_button.clicked.connect(self._prev_photo)
        self.save_button.clicked.connect(self._save_photos_to_dir)
        self.save_path_button.clicked.connect(self._set_save_path)
        self.load_path_button.clicked.connect(self._set_load_path)
        self.mark_with_button.clicked.connect(self._marked_with)
        self.mark_without_button.clicked.connect(self._marked_without)
        self.swap_button.clicked.connect(self._swap_gallery)
        self.start_button.clicked.connect(self._start_algorithm)
        self.update_gallery_text()
        self.update_stats()

    def _start_algorithm(self):
        self.start_search()

    def _save_photos_to_dir(self):
        """
        Handler method for save_button.
        Saves to currently written path in "Save Path" lineEdit field.
        """
        save_path = self.save_path_lineEdit.text()
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        for photo in self.detected_photos:
            folder_path = os.path.join(save_path, os.path.basename(photo))
            shutil.copyfile(photo, folder_path)

    def _set_load_path(self):
        """
        Method to choose starting dataset using FileDialog. Updates load_path_info_lineEdit
        """
        path = str(QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, 'Select load Folder'))
        self.load_path_lineEdit.setText(path)

    def _set_save_path(self):
        """
        Method to choose writing location for selected photos using FileDialog. Updates "save_path" lineEdit
        """
        path = str(QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, 'Select save Folder'))
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
        """
        Updates lineEdit over gallery
        """
        if self.current_photos == self.detected_photos:
            self.photo_display_info_lineEdit.setText("Detected photos")
        elif self.current_photos == self.undetected_photos:
            self.photo_display_info_lineEdit.setText("Undetected photos")
        else:
            self.photo_display_info_lineEdit.setText("No photos")  # Do przetestowania

    def _swap_gallery(self):
        """
        Handler method for swap_button
        """
        if self.current_photos == self.detected_photos:
            self.current_photos = self.undetected_photos
        else:
            self.current_photos = self.detected_photos

        if len(self.current_photos) == 0:
            self.photo_display.setPixmap(QtGui.QPixmap())

        self.update_gallery_text()

    def update_confident_photos(self, photos):
        """
        Update photos array that gallery uses.
        :param photos: array of photo paths
        """
        if isinstance(photos, list):
            self.detected_photos = photos
            self.current_photos = self.detected_photos
        else:
            raise TypeError("To update photos array pass array of photo paths")

    def update_questionable_photos(self, photos):
        """
        Update photos array that gallery uses.
        :param photos: array of photo paths
        """
        if isinstance(photos, list):
            self.undetected_photos = photos
            self.current_photos = self.undetected_photos
        else:
            raise TypeError("To update photos array pass array of photo paths")

    def get_confidence(self):
        """
        Getter for confidence parameter
        """
        return self.confidence_lineEdit.text()

    def get_max_depth(self):
        """
        Getter for max depth parameter
        """
        return self.max_depth_lineEdit.text()

    def get_model_type(self):
        """
        Getter for model type
        """
        return self.model_comboBox.currentText()

    def get_load_path(self):
        """
        Getter for directory path with photos to use in algorithm
        """
        return self.load_path_lineEdit.text()

    def get_alg_type(self):
        """
        Getter for algorithm type - Half or quarter images
        """
        return self.alg_type_comboBox.currentText()

    def update_stats(self):
        """
        Updating statistics lineEdits
        """
        self.stats_detected_lineEdit.setText(str(len(self.detected_photos)))
        self.stats_undetected_lineEdit.setText(str(len(self.undetected_photos)))
        self.stats_total_lineEdit.setText(str(len(self.undetected_photos) + len(self.detected_photos)))

    def _marked_with(self):
        """
        Handler for mark_with_button
        """
        photo = self.detected_photos[self.curr_photo]
        if photo not in self.marked_with_array:
            self.marked_with_array.append(photo)

    def _marked_without(self):
        """
        Handler for mark_without_button
        """
        photo = self.detected_photos[self.curr_photo]
        if photo not in self.marked_without_array:
            self.marked_without_array.append(photo)

    def start_search(self):
        confidence_level = self.get_confidence()
        if confidence_level == '':
            confidence_level = None
        else:
            try:
                confidence_level = float(confidence_level)
                if not (0 <= confidence_level <= 1):
                    raise ValueError()
            except ValueError:
                raise ValueError("confidence level must be number from 0 to 1")

        max_depth = self.get_max_depth()
        print(max_depth, type(max_depth))
        if max_depth == '':
            max_depth = None
        else:
            try:
                max_depth = int(max_depth)
                if 0 > max_depth:
                    raise ValueError()
            except ValueError:
                raise ValueError("max depth level must be integer greater then 0")

        photos_path = self.get_load_path()
        parameters_path = "models/" + self.get_model_type()
        alg_type = self.get_alg_type()
        dir_with, dir_without = SearchSet(photos_path, parameters_path, max_depth, alg_type, confidence_level)
        print(dir_without)
        self.update_confident_photos(dir_with)
        self.update_stats()
        print(self.detected_photos)


