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
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QGraphicsView, QLabel, QMenuBar, QStatusBar, QWidget
from PySide6.QtCore import QRect, QMetaObject, QTimer
from PySide6.QtGui import QIcon
from qrcode_generator import *
from qrcode_scanner import *

QRcode_file = None


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

        # Connect the button to the function
        self.SelectQRcoded.clicked.connect(self.SelectQRcode_clicked)



    def SelectQRcode_clicked(self)->str:
        global QRcode_file
        print("SelectQRcode_clicked")
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(None, "Select QR Code File", "", "All Files (*);;PNG Files (*.png);;JPEG Files (*.jpg *.jpeg)", options=options)
        if file_name:
            print(f"Selected file: {file_name}")
            QRcode_file = file_name
            return QRcode_file
        return None



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"二维码生成器", None))
        self.SelectQRcoded.setText(QCoreApplication.translate("MainWindow", u"Select QR Code", None))
        self.GenerateQRcode.setText(QCoreApplication.translate("MainWindow", u"Generate QR Code", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"QR Code Scanner and Generator", None))
