from qrcode_scanner import *
from qrcode_generator import *
from PIL import Image
from QRCODE_UI import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

if __name__ == "__main__":

    # 创建应用程序实例
    app = QApplication(sys.argv)

    # 创建主窗口实例
    MainWindow = QMainWindow()

    # 创建UI实例并设置UI
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # 显示主窗口
    MainWindow.show()

    # 运行应用程序
    sys.exit(app.exec())
