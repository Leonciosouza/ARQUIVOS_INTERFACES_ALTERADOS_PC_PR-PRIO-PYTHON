# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tabella_equipes_confr.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(592, 558)
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(85, 170, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-30, 0, 631, 71))
        self.label.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"font: 900 italic 20pt \"Segoe UI\";")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 160, 91, 56))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(127, 254, 188);")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"background-color: rgb(112, 176, 255);")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 80, 611, 31))
        self.label_2.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(110, 190, 77, 61))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"background-color: rgb(227, 255, 137);")

        self.verticalLayout_2.addWidget(self.pushButton_10)

        self.pushButton_9 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.verticalLayout_2.addWidget(self.pushButton_9)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(200, 250, 77, 80))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_14 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"background-color: rgb(85, 255, 127);")

        self.verticalLayout_3.addWidget(self.pushButton_14)

        self.pushButton_13 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"background-color: rgb(255, 255, 127);")

        self.verticalLayout_3.addWidget(self.pushButton_13)

        self.pushButton_15 = QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(310, 280, 75, 24))
        self.pushButton_15.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 230, 91, 56))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"background-color: rgb(127, 254, 188);")

        self.verticalLayout_4.addWidget(self.pushButton_6)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"background-color: rgb(112, 176, 255);")

        self.verticalLayout_4.addWidget(self.pushButton_4)

        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 300, 91, 56))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"background-color: rgb(127, 254, 188);")

        self.verticalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background-color: rgb(112, 176, 255);")

        self.verticalLayout_5.addWidget(self.pushButton_3)

        self.verticalLayoutWidget_6 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 370, 91, 61))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"background-color: rgb(127, 254, 188);;")

        self.verticalLayout_6.addWidget(self.pushButton_8)

        self.pushButton = QPushButton(self.verticalLayoutWidget_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(112, 176, 255);")

        self.verticalLayout_6.addWidget(self.pushButton)

        self.verticalLayoutWidget_7 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(110, 330, 81, 61))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_11 = QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"background-color: rgb(227, 255, 137);")

        self.verticalLayout_7.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.verticalLayout_7.addWidget(self.pushButton_12)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 130, 91, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 160, 91, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 220, 81, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(320, 250, 41, 16))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(160, 422, 283, 81))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.pushButton_16 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        font = QFont()
        font.setBold(True)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet(u"background-color: rgb(202, 202, 202);")

        self.horizontalLayout.addWidget(self.pushButton_16)

        self.textEdit = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"\n"
"background-color: rgb(170, 170, 255);")

        self.horizontalLayout.addWidget(self.textEdit)

        self.pushButton_17 = QPushButton(self.centralwidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(230, 510, 75, 24))
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet(u"background-color: rgb(139, 139, 139);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.pushButton_11)
        QWidget.setTabOrder(self.pushButton_11, self.pushButton_12)
        QWidget.setTabOrder(self.pushButton_12, self.pushButton_14)
        QWidget.setTabOrder(self.pushButton_14, self.pushButton_13)
        QWidget.setTabOrder(self.pushButton_13, self.pushButton_15)
        QWidget.setTabOrder(self.pushButton_15, self.pushButton_16)
        QWidget.setTabOrder(self.pushButton_16, self.textEdit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#ffffff;\">TABELA DE TIMES</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"TIME=01", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"TIME=02", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#ffffff;\">CAMPEONATO IFRN DE FUTEBOL PARNAMIRIM</span></p></body></html>", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"TIME=", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"TIME=", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"TIME=", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"TIME=", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Campe\u00e3o!", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"TIME=03", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"TIME=04", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"TIME=05", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"TIME=06", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"TIME=07", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"TIME=08", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"TIME=", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"TIME=", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Primeira rodada</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Seguna Rodada</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Semi final</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Final</span></p></body></html>", None))
        self.label_7.setText("")
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"gerarConfronto", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; color:#000000;\">TIME=01        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; color:#000000;\">TIME=02</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; color:#000000;\">TIME=03</span></p>\n"
"<p style=\" margin-top:0p"
                        "x; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; color:#000000;\">TIME=04</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; color:#000000;\">TIME=05</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; color:#000000;\">TIME=06</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; color:#000000;\">TIME=07</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; color:#000"
                        "000;\">TIME=08</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:12pt; color:#55aa7f;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:12pt; color:#55aa7f;\"><br /></p></body></html>", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
    # retranslateUi

