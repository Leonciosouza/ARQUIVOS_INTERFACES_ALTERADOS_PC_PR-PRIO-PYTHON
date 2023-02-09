# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface2.ui'
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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(329, 431)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(80, 30, 151, 31))
        self.listWidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 70, 256, 161))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 280, 90, 30))
        font = QFont()
        font.setBold(True)
        font.setUnderline(False)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setStyleSheet(u"<BUTTON; style, background-color: \"rgb(85, 85, 255)\"; font size: \"8\"; color: \"green\";\n"
"border-right-color: \"rgb(85, 255, 127)\";>")
        self.pushButton.setAutoDefault(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 329, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\" bgcolor=\"#008000\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:696; color:#ff0000;\">RELA\u00c7\u00c3O DAS EQUIPES</span></p></body></html>", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"1-", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"2-", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"3-", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"4-", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"5-", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"6-", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"7-", None));
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"8-", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"confirmar", None))
    # retranslateUi

