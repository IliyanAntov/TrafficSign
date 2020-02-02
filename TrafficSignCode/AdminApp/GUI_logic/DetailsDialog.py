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
from GUI.DetailsDialog.DetailsDialog import Ui_DetailsDialog
from DataExchange.DataExchange import DataExchange
from DataExchange.Connection import Connection

class DetailsDialog(QDialog):
    def __init__(self, alias, IMEI, status, value):
        super().__init__()
        self.alias = alias
        self.IMEI = IMEI
        self.status = status
        self.value = value
        self.ui = Ui_DetailsDialog()
        self.ui.setupUi(self)
        self.SetupFunctionality()
    
    def SetupFunctionality(self):
        self.setWindowIcon(QIcon('./GUI/images/icon.png'))
        self.ui.CurrentAliasLabel.setText(self.alias)
        self.ui.IMEILabel.setText(self.IMEI)
        self.ui.StatusLabel.setText(self.status)
        self.ui.ValueLabel.setText(self.value)
        self.ui.CloseButton.clicked.connect(self.QuitDialog)
 
    def QuitDialog(self):
        self.reject() 
