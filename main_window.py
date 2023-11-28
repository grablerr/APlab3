import sys
import os

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QMessageBox, QFileDialog

from Script1 import run1
from Script2 import run2
from Script3 import run3
from Script5 import Iterator1_txt

class Ui_MainWindow(QWidget):
    """this class implements the execution of all tasks and the transition to a new window"""
    def setupUi(self, MainWindow) -> None:
        """function for working with a GUI object"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.folder = None
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 10, 311, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 90, 211, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 90, 201, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 90, 201, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 150, 201, 32))
        self.pushButton_5.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 24))
        self.menubar.setObjectName("menubar")
        self.menuMenu1 = QtWidgets.QMenu(self.menubar)
        self.menuMenu1.setObjectName("menuMenu1")
        self.menuMenu2 = QtWidgets.QMenu(self.menubar)
        self.menuMenu2.setObjectName("menuMenu2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuMenu1.addSeparator()
        self.menubar.addAction(self.menuMenu1.menuAction())
        self.menubar.addAction(self.menuMenu2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow) -> None:
        """a function for translating the text of buttons and working with buttons"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать путь к датасету"))
        self.pushButton_2.setText(_translate("MainWindow", "Создание Аннотации Task1"))
        self.pushButton_3.setText(_translate("MainWindow", "Создание Аннотации Task2"))
        self.pushButton_4.setText(_translate("MainWindow", "Создание Аннотации Task3"))
        self.pushButton_5.setText(_translate("MainWindow", "Работа с рецензиями"))

        self.pushButton.clicked.connect(self.get_folder)
        self.pushButton_2.clicked.connect(self.task1)
        self.pushButton_3.clicked.connect(self.task2)
        self.pushButton_4.clicked.connect(self.task3)
        self.pushButton_5.clicked.connect(self.openDialog)

    def get_folder(self) -> None:
        """function for selecting the path to the project"""
        self.folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Выбрать папку исходного датасета")
        try:
            os.chdir(self.folder)
            print(self.folder)
        except:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Папка не выбрана")
            error.exec()

    def task1(self) -> None:
        """function to execute task1"""
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "CSV files (*.csv)")

        if file_path:
            run1(self.folder, 'responses', file_path)
            complete = QMessageBox()
            complete.setWindowTitle("OK")
            complete.setText("Задача выполнена")
            complete.exec()

    def task2(self) -> None:
        """function to execute task2"""
        folder_path = QFileDialog.getExistingDirectory(self, "Выбрать папку", QtCore.QDir.homePath())

        if folder_path:
            dataset_task2_folder = os.path.join(folder_path, "AIODataset")
            os.makedirs(dataset_task2_folder, exist_ok=True)
            run2(self.folder, dataset_task2_folder, "!AIOAnnotation.csv")

            complete = QMessageBox()
            complete.setWindowTitle("OK")
            complete.setText("Задача выполнена")
            complete.exec()
            
    def task3(self) -> None:
        """function to execute task3"""
        folder_path = QFileDialog.getExistingDirectory(self, "Выбрать папку", QtCore.QDir.homePath())
        
        if folder_path:
            dataset_task3_folder = os.path.join(folder_path, 'RandomDataset')
            os.makedirs(dataset_task3_folder, exist_ok=True)
            run3(self.folder, '!RDAnnotation.csv', dataset_task3_folder)
            compleate = QMessageBox()
            compleate.setWindowTitle("OK")
            compleate.setText("Задача выполнена")
            compleate.exec()

    def openDialog(self) -> None:
        """function for opening a new window"""
        dialog = ClssDialog(self)
        dialog.exec()

class ClssDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)
        #C:\Users\Professional\Desktop\SSAU\PP\APlabs\APlab3
        self.__iterator = Iterator1_txt(os.path.join("/Users", "Professional", "Desktop", "SSAU", "PP", "APlabs", "APlab3"), "1", "dataset")
        self.resize(640, 650)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)

        self.text_display = QtWidgets.QLabel(self)
        self.verticalLayout.addWidget(self.text_display)

        self.pushButton = QtWidgets.QPushButton('Дальше', self)
        self.pushButton.clicked.connect(self.__nextButton)
        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QtWidgets.QPushButton('Закрыть', self)
        self.pushButton_3.clicked.connect(self.btnClosed)
        self.verticalLayout.addWidget(self.pushButton_3)

        self.radio_buttons = []
        for i in range(1, 6):
            radio_button = QtWidgets.QRadioButton(str(i), self)
            radio_button.setAccessibleName(str(i))
            radio_button.clicked.connect(self.buttonClicked)
            self.radio_buttons.append(radio_button)
            self.verticalLayout.addWidget(radio_button)

        self.setWindowTitle("Рецензия")

    def buttonClicked(self):
        sender = self.sender()
        self.__iterator.setName(sender.text())
        self.__iterator.getName()

    def __nextButton(self):
        try:
            file_path = os.path.join(os.path.join(self.__iterator.dataset, self.__iterator.path, self.__iterator.name), self.__iterator.__next__()) 
            with open(file_path, 'r', encoding='utf-8') as file:
                text_content = file.read()
                self.text_display.setText(text_content)
        except StopIteration:
            error1 = QtWidgets.QMessageBox()
            error1.setWindowTitle("Ошибка")
            error1.setText("Закончились отзывы")
            error1.exec_()

    def btnClosed(self):
        self.close()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setStyleSheet("#MainWindow{border-image:url(ls.jpg)}")
    MainWindow.show()
    sys.exit(app.exec())