# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QRCODE_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from qrcode_generator import *
from qrcode_scanner import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AddressBookNew))
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.SelectQRcoded = QPushButton(self.centralwidget)
        self.SelectQRcoded.setObjectName(u"SelectQRcode")
        self.SelectQRcoded.setGeometry(QRect(140, 390, 131, 41))
        self.QRcodeDisplayer = QGraphicsView(self.centralwidget)
        self.QRcodeDisplayer.setObjectName(u"QRcodeDisplayer")
        self.QRcodeDisplayer.setGeometry(QRect(240, 80, 291, 231))
        self.GenerateQRcode = QPushButton(self.centralwidget)
        self.GenerateQRcode.setObjectName(u"GenerateQRcode")
        self.GenerateQRcode.setGeometry(QRect(510, 390, 131, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 10, 471, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        def SelectQRcode_clicked()->str:
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            file_name, _ = QFileDialog.getOpenFileName(None, "Select QR Code File", "", "All Files (*);;PNG Files (*.png);;JPEG Files (*.jpg *.jpeg)", options=options)
            if file_name:
                print(file_name)  # You can replace this with any action you want to perform with the selected file
                return file_name
            return None
        

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e91\u5e73\u53f0\u4e8c\u7ef4\u7801\u751f\u6210\u5668", None))
        self.SelectQRcoded.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8bfe\u7a0b\u4e8c\u7ef4\u7801", None))
        self.GenerateQRcode.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u8bfe\u7a0b\u4e8c\u7ef4\u7801", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

