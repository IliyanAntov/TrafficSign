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
from GUI_logic.LoginDialog import LoginDialog
from GUI_logic.SetSpeedLimitDialog import SetSpeedLimitDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.SetupButtons()
        self.connection = DataExchange()
        threading.Thread(target = DataExchange().RequestDevices).start()

    def SetupButtons(self):
        self.ui.SetSpeedLimitButton.clicked.connect(self.ShowSetSpeedLimitDialog)
        self.ui.RefreshButton.clicked.connect(self.UpdateDeviceList)

    def UpdateDeviceList(self):
        DataExchange().RequestDevices()
        self.ui.DeviceList.setDisabled(True)
        self.ui.DeviceList.clear()
        for i in range(len(Connection().deviceList)):
            device = Connection().deviceList[i]
            self.ui.DeviceList.addItem(device.decode('utf-8'))        
        self.ui.DeviceList.setDisabled(False)

    @pyqtSlot()
    def ShowSetSpeedLimitDialog(self):
        deviceList = self.ui.DeviceList.selectedItems()
        if (len(deviceList) > 0):
            target = deviceList[0].text()
            self.setSpeedLimitDialog = SetSpeedLimitDialog(target)
            self.setSpeedLimitDialog.show()
        else:
            pass

    def KeyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.connection.Close()
            self.reject()
        if event.key() == Qt.Key_Enter:
            self.ConnectClick()

