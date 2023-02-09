# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tela_secundaria_Login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(288, 351)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 90, 47, 13))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 150, 47, 13))
        self.label_2.setFont(font)
        self.label_2.setInputMethodHints(Qt.ImhSensitiveData)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 90, 161, 21))
        self.lineEdit.setInputMethodHints(Qt.ImhNoEditMenu)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 150, 161, 20))
        font1 = QFont()
        font1.setUnderline(False)
        font1.setStrikeOut(True)
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setTabletTracking(False)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 210, 75, 23))
        self.pushButton.setMinimumSize(QSize(2, 2))
        self.pushButton.setSizeIncrement(QSize(1, 1))
        self.pushButton.setBaseSize(QSize(3, 3))
        font2 = QFont()
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"<style-button, backgound: \"rgb(0, 170, 255\"); color:\"blue\";>\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"selection-color: \"rgb(255, 170, 255)\";>")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 210, 71, 23))
        font3 = QFont()
        font3.setBold(True)
        font3.setStrikeOut(False)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setStyleSheet(u"<style-button {\n"
"	background: \"blue\";\n"
"	color: \"white\";\n"
"	border-style: outset;\n"
"	color: \"rgb(255, 255, 0);qconicalgradient(cx:0, cy:0, angle:135, stop:0 			rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69))\n"
"	border-color: #0066A2\";\n"
"	height: \"50px\";\n"
"	width: \"100px\";\n"
"	font: \"bold15px arial,sans-serif;\n"
"text-shadow: none\n"
"\";\n"
"}>")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 288, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Equipe", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
    # retranslateUi

