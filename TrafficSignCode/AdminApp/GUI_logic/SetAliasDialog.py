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
from GUI.SetAliasDialog.SetAliasDialog import Ui_SetAliasDialog
from DataExchange.DataExchange import DataExchange
from DataExchange.Connection import Connection

class SetAliasDialog(QDialog):
    def __init__(self, target):
        super().__init__()
        self.target = target
        self.ui = Ui_SetAliasDialog()
        self.ui.setupUi(self)
        self.connection = DataExchange()
        self.SetupFunctionality()
    
    def SetupFunctionality(self):
        self.ui.CurrentNameTextBox.setText(self.target)
        self.ui.ConfirmButton.clicked.connect(self.SetAlias)
        self.ui.CancelButton.clicked.connect(self.QuitDialog)
 
    def SetAlias(self):
        IMEI = Connection().knownDevices.pop(self.target)
        newName = self.ui.NewNameTextBox.text()
        Connection().knownDevices[newName] = IMEI
        self.accept()

    def QuitDialog(self):
        self.reject() 
