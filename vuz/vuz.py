import sqlite3
from PyQt6 import *
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QGroupBox, QScrollArea

import sys
import points
import Profil

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()



class Ui_MainWindow(object):
   

    def open_points_window(self, window_class):
        self.window = QtWidgets.QMainWindow()
        self.ui = window_class()
        self.ui.setupUi(self.window)

        self.window.close()  # закрыть текущее окно

        self.window.show()  # открыть новое окно
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(878, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 10, 81, 51))
        self.pushButton_6.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/img1"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(690, -10, 161, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 861, 71))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, -20, 161, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 590, 71, 51))
        self.pushButton_2.setToolTipDuration(-1)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./img/img2"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(lambda: self.open_points_window(points.Ui_MainWindow2))

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 640, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 590, 71, 51))
        self.pushButton_3.setToolTipDuration(-1)
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./img/img3"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(60, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 640, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(500, 590, 71, 51))
        self.pushButton_5.setToolTipDuration(-1)
        self.pushButton_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./img/img4"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 640, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(720, 590, 71, 51))
        self.pushButton_4.setToolTipDuration(-1)
        self.pushButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./img/img5"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.open_points_window(Profil.Ui_Dialog))
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(720, 640, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 878, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.scroll_area = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scroll_area.setGeometry(QtCore.QRect(200, 150, 500, 400))
        self.scroll_area.setObjectName("scroll_area")

        with sqlite3.connect("main.db") as db:
            ui = points.Ui_MainWindow2()
            # points_value = ui.points_input.text()
            # Используйте значение points_value
            cursor = db.cursor()
            # if points_value:
            #     cursor.execute("SELECT * FROM Universities WHERE Points >= ?", (points_value,))
            #     print("111111111111111111")
            # else:
            cursor.execute("SELECT * FROM Universities")
            print("22222222222")
            rows = cursor.fetchall()
            

            self.content_widget = QWidget()
            self.content_layout = QVBoxLayout(self.content_widget)
            

            # Add new data blocks
            for row in rows:
                group_box = QGroupBox(f"ID: {row[0]} | Университет: {row[1]}")
                group_box_layout = QVBoxLayout(group_box)
                group_box_layout.addWidget(QLabel(f"Предмет: {row[2]}"))
                group_box_layout.addWidget(QLabel(f"Балл: {row[3]}"))
                group_box_layout.addWidget(QLabel(f"Город: {row[4]}"))
                group_box.setStyleSheet("background-color: #f0f0f0; border: 2px solid #e0e0e0; border-radius: 5px; padding: 10px;")
                group_box_layout.setSpacing(10)
                self.content_layout.addWidget(group_box)
                group_box.setMinimumWidth(400)

            self.scroll_area.setWidget(self.content_widget)


        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Vuzopedia"))
        self.label_7.setText(_translate("MainWindow", "Вузы"))
        self.label_2.setText(_translate("MainWindow", "Баллы"))
        self.label_4.setText(_translate("MainWindow", "Вузы"))
        self.label_5.setText(_translate("MainWindow", "Профессии"))
        self.label_6.setText(_translate("MainWindow", "Профиль"))

def run():
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__": 
    run()
