# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interfacegraficaproj.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(612, 526)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setBackground(QColor(0, 170, 255));
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        brush1 = QBrush(QColor(0, 0, 255, 255))
        brush1.setStyle(Qt.NoBrush)
        font2 = QFont()
        font2.setBold(True)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font2);
        __qtablewidgetitem9.setBackground(brush1);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem12)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 70, 571, 185))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QSize(16000000, 16000000))
        self.tableWidget.setSizeIncrement(QSize(4, 4))
        self.tableWidget.setBaseSize(QSize(1, 1))
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(45)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_2 = QTableWidget(self.centralwidget)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(60, 271, 341, 161))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 612, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Partidas", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio da partida", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Data da partida", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Placar da partida", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Inform.", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"jogo1", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"jogo 2", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"jogo 3", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"jogo 4", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem9 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Alemanha x Argentina", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"        -15:00 P.m-", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"        20/09/1988", None));
        ___qtablewidgetitem12 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"              _x_", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi




