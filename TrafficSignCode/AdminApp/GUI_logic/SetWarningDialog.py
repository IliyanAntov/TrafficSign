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
from GUI.SetWarningDialog.SetWarningDialog import Ui_SetWarningDialog
from GUI_logic.TrafficSignPreview import TrafficSignPreview
from DataExchange.DataExchange import DataExchange
from DataExchange.Connection import Connection

class SetWarningDialog(QDialog):
    def __init__(self, target):
        super().__init__()
        self.target = target
        self.ui = Ui_SetWarningDialog()
        self.ui.setupUi(self)
        self.connection = DataExchange()
        self.SetupFunctionality()
    
    def SetupFunctionality(self):
        self.setWindowIcon(QIcon('./GUI/images/icon.png'))
        self.ui.CancelButton.setFocus()
        self.UpdateImage()
        self.ui.SelectionBox.currentTextChanged.connect(self.UpdateImage)
        self.ui.ConfirmButton.clicked.connect(self.SetWarning)
        self.ui.CancelButton.clicked.connect(self.QuitDialog)

    def GetCurrentSelection(self):
        selection = str(self.ui.SelectionBox.currentText())
        if(selection == "Stop sign"):
            return "StopSign"
        elif(selection == "General warning"):
            return "GeneralWarning"
        elif(selection == "Traffic light"):
            return "TrafficLight"
        elif(selection == "No entry"):
            return "NoEntry"
        elif(selection == "Forward only"):
            return "ForwardOnly"
        elif(selection == "Left only"):
            return "LeftOnly"
        elif(selection == "Right only"):
            return "RightOnly"
        else:
            return None

    def UpdateImage(self):
        self.currentSelection = self.GetCurrentSelection()
        if(self.currentSelection):
            image = "./GUI/images/" + self.currentSelection + ".png"
            pixmap = QPixmap(image)
            self.ui.ImageLabel.setPixmap(pixmap)


    def SetWarning(self):
        print(self.currentSelection)
        self.connection.SetWarning(Connection().knownDevices[self.target], self.currentSelection)
        self.accept()
        # self.connection.SetSpeedLimit(Connection().knownDevices[self.target], speedLimit)
        # self.accept()

    def QuitDialog(self):
        self.reject() 