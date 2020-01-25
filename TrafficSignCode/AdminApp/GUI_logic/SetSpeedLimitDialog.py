import socket
import time
import sys
import select
import struct
import threading
# from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QRegExpValidator
from PyQt5.QtCore import pyqtSlot, Qt, QRegExp
from GUI.MainWindow.MainWindow import Ui_MainWindow
from GUI.SetSpeedLimitDialog.SetSpeedLimitDialog import Ui_SetSpeedLimitDialog
from GUI.LoginDialog.LoginDialog import Ui_LoginDialog
from DataExchange.DataExchange import DataExchange
from DataExchange.Connection import Connection

class SetSpeedLimitDialog(QDialog):
    def __init__(self, target):
        super().__init__()
        self.target = target
        self.ui = Ui_SetSpeedLimitDialog()
        self.ui.setupUi(self)
        self.SetupFunctionality()
        self.connection = DataExchange()
    
    def SetupFunctionality(self):
        inputRegEx = QRegExp("[1-9]\d{0,2}")
        validator = QRegExpValidator(inputRegEx)
        self.ui.SpeedLimitTextBox.setValidator(validator)
        self.ui.ConfirmButton.clicked.connect(self.SendSpeedLimit)
        self.ui.CancelButton.clicked.connect(self.QuitDialog)

    def SendSpeedLimit(self):
        speedLimit = self.ui.SpeedLimitTextBox.text()
        Connection().SendMessage(str.encode("Target:" + self.target + " " "SpeedLim:" + speedLimit))
        self.accept()
 
    def QuitDialog(self):
        self.reject() 
