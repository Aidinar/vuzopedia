import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets
import sys

import points
import vuz


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()

class Ui_Dialog(object):
    def open_window(self, window_class):
        self.window = QtWidgets.QMainWindow()
        self.ui = window_class()
        self.ui.setupUi(self.window)

        Dialog.close()

        self.window.show()


    def save_user(self):
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()

        # Check if the user already exists
        user = (self.lineEdit.text(), self.lineEdit_3.text(), self.lineEdit_2.text())
        self.c.execute("SELECT * FROM Users WHERE Username = ? AND Password = ?", (user[0], user[2]))
        existing_user = self.c.fetchone()

        if existing_user:
                # User already exists, display a message
                print("You are logged in, can use points'")
        else:
                # Insert the new user
                self.c.execute("INSERT INTO Users (Username, City, Password) VALUES (?, ?, ?)", user)
                self.conn.commit()
                print("You've already been logged in")

        self.conn.close()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(945, 794)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(160, 10, 161, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 670, 121, 71))
        self.pushButton_2.setToolTipDuration(-1)
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/img2"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.open_window(points.Ui_MainWindow2))
        self.pushButton_6 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 20, 121, 71))
        self.pushButton_6.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./img/img1"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 750, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(340, 750, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(540, 750, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(800, 750, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 670, 121, 71))
        self.pushButton_3.setToolTipDuration(-1)
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./img/img3"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(90, 70))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.open_window(vuz.Ui_MainWindow))
        self.pushButton_4 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(780, 670, 121, 71))
        self.pushButton_4.setToolTipDuration(-1)
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./img/img4"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_4.setObjectName("pushButton_4")
        


        self.pushButton_5 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(530, 670, 121, 71))
        self.pushButton_5.setToolTipDuration(-1)
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./img/img5"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(65, 65))
        self.pushButton_5.setObjectName("pushButton_5")
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(260, 100, 451, 541))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"    background: #333\n"
"}\n"
"QLabel\n"
"{\n"
"    color: white;\n"
"}\n"
"QLineEdit \n"
"{\n"
"    background:transparent;\n"
"    border: none;\n"
"    color:#717072;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(150, 70, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 470, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"color:white;\n"
"background:red;\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"color:#333;\n"
"background:#49ebff;\n"
"border-radius: 20px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save_user)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 160, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit \n"
"{\n"
"    backround:transparent;\n"
"    border:none;\n"
"    color:#717072;\n"
"    border-bottom:1px solid #717072;\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 280, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit \n"
"{\n"
"    backround:transparent;\n"
"    border:none;\n"
"    color:#717072;\n"
"    border-bottom:1px solid #717072;\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 120, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 220, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.frame)
        self.label_9.setGeometry(QtCore.QRect(30, 340, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 390, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit \n"
"{\n"
"    backround:transparent;\n"
"    border:none;\n"
"    color:#717072;\n"
"    border-bottom:1px solid #717072;\n"
"}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit_3.setCursorPosition(0)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.toolButton = QtWidgets.QToolButton(parent=Dialog)
        self.toolButton.setGeometry(QtCore.QRect(430, 50, 111, 101))
        self.toolButton.setStyleSheet("#toolButton\n"
"{\n"
"background:red;\n"
"border-radius: 40px;\n"
"}")
        self.toolButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./img/img5"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton.setIcon(icon5)
        self.toolButton.setIconSize(QtCore.QSize(80, 80))
        self.toolButton.setObjectName("toolButton")
        self.label.raise_()
        self.pushButton_2.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.frame.raise_()
        self.toolButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Прифиль"))
        self.label_2.setText(_translate("Dialog", "Баллы"))
        self.label_4.setText(_translate("Dialog", "Вузы"))
        self.label_5.setText(_translate("Dialog", "Профессии"))
        self.label_6.setText(_translate("Dialog", "Профиль"))
        self.label_3.setText(_translate("Dialog", "Авторизация "))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Password"))
        self.label_7.setText(_translate("Dialog", "Введите имя"))
        self.label_8.setText(_translate("Dialog", "Введите пароль"))
        self.label_9.setText(_translate("Dialog", "Введите город"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "City"))


def run4():
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

if __name__ == "__main__":
     run4()












