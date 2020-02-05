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
from GUI_logic.TrafficSignPreview import TrafficSignPreview
from DataExchange.DataExchange import DataExchange
from DataExchange.Connection import Connection

class SetSpeedLimitDialog(QDialog):
    def __init__(self, target):
        super().__init__()
        self.target = target
        self.ui = Ui_SetSpeedLimitDialog()
        self.ui.setupUi(self)
        self.connection = DataExchange()
        self.SetupFunctionality()
    
    def SetupFunctionality(self):
        self.setWindowIcon(QIcon('./GUI/images/icon.png'))
        self.ui.CancelButton.setFocus()
        inputRegEx = QRegExp("[1-9]\d{0,2}")
        validator = QRegExpValidator(inputRegEx)
        self.ui.SpeedLimitTextBox.setValidator(validator)
        self.ui.ConfirmButton.clicked.connect(self.SetSpeedLimit)
        self.ui.CancelButton.clicked.connect(self.QuitDialog)
        self.ui.PreviewButton.clicked.connect(self.DisplayPreview)
 
    def SetSpeedLimit(self):
        speedLimit = self.ui.SpeedLimitTextBox.text()
        response = self.connection.SetSpeedLimit(Connection().knownDevices[self.target], speedLimit)
        result = self.HandleResponse(response)
        if(result):
            self.accept()
        else:
            self.reject()

    def HandleResponse(self, response):
        if(response == 'nosend'):
            QMessageBox.warning(self, "Error", "Couldn't send message to device", QMessageBox.Ok)
            return False
        elif(response == 'notfound'):
            QMessageBox.warning(self, "Error", "Requested device not found", QMessageBox.Ok)
            return False
        elif(response == 'noresp'):
            QMessageBox.warning(self, "Error", "Device didn't respond", QMessageBox.Ok)
            return False
        elif(response == 'success'):
            QMessageBox.information(self, "Success", "Successfuly sent request to device", QMessageBox.Ok)
            return True

    def DisplayPreview(self):
        self.previewDialog = TrafficSignPreview('./GUI/images/SpeedLimit.png')
        self.previewDialog.show()

    def QuitDialog(self):
        self.reject() 
