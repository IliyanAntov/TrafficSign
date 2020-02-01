import socket
import time
import sys
import select
import struct
import threading
# from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QRegExpValidator, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt, QRegExp
from GUI.MainWindow.MainWindow import Ui_MainWindow
from GUI.SetSpeedLimitDialog.SetSpeedLimitDialog import Ui_SetSpeedLimitDialog
from GUI.LoginDialog.LoginDialog import Ui_LoginDialog
from GUI.SetAliasDialog.SetAliasDialog import Ui_SetAliasDialog
from GUI.TrafficSignPreview.TrafficSignPreview import Ui_TrafficSignPreview
from DataExchange.DataExchange import DataExchange
from DataExchange.Connection import Connection

class TrafficSignPreview(QDialog):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.ui = Ui_TrafficSignPreview()
        self.ui.setupUi(self)
        self.SetupFunctionality()
    
    def SetupFunctionality(self):
        pixmap = QPixmap(self.image)
        self.ui.TrafficSignImage.setPixmap(pixmap)

    def QuitDialog(self):
        self.reject() 
