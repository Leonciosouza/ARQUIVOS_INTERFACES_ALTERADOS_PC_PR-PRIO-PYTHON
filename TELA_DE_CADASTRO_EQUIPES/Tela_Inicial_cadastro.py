# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tela_inicial_cadastro.ui'
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
        MainWindow.resize(261, 331)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 80, 47, 13))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 140, 47, 13))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 80, 141, 20))
        self.lineEdit.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 140, 141, 20))
        self.lineEdit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lineEdit_2.setDragEnabled(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 200, 75, 23))
        font2 = QFont()
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setFlat(True)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(90, 240, 75, 23))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(True)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(150, 200, 75, 24))
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(True)
        self.pushButton_3.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 261, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(True)
        self.pushButton_2.setDefault(True)
        self.pushButton_3.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Equipe:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Grupo:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
    # retranslateUi

