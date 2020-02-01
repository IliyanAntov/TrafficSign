import socket
import time
import sys
import select
import struct
import threading
import yaml
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

        self.knownDevices = {}
        self.LoadKnownDevices()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.SetupButtons()
        self.AdjustUI()
        self.connection = DataExchange()

    def SetupButtons(self):
        self.ui.SetSpeedLimitButton.clicked.connect(self.ShowSetSpeedLimitDialog)
        self.ui.RefreshButton.clicked.connect(self.UpdateDeviceList)
        self.ui.SetListEntryAliasButton.clicked.connect(self.UpdateDeviceAlias)

    def AdjustUI(self):
        self.setStyleSheet( """ QListWidget:item:selected:active {
                                     background: dodgerblue;
                                     color: white;
                                }
                                QListWidget:item:selected:!active {
                                     background: dodgerblue;
                                     color: white;
                                }
                                """
                                )

    def UpdateDeviceList(self):
        DataExchange().GetDevices()
        self.ui.DeviceList.setDisabled(True)
        self.ui.DeviceList.clear()

        deviceList = self.GenerateDeviceList()
        for device in deviceList:
            self.ui.DeviceList.addItem(device)
    
        self.ui.DeviceList.setDisabled(False)

    def UpdateDeviceAlias(self):
        pass


    def LoadKnownDevices(self):
        with open("./GUI_logic/DeviceAliases.yaml", 'r') as stream:
            try:
                self.knownDevices = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        print(self.knownDevices)

    def SaveKnownDevices(self):
        with open("./GUI_logic/DeviceAliases.yaml", 'w', encoding='utf-8') as outfile:
            yaml.dump(self.knownDevices, outfile, default_flow_style=False, allow_unicode=True)
            print('success')


    def GenerateDeviceList(self):
        deviceList = []
        for device in Connection().deviceList:
            device = device.decode('utf-8')
            if not self.knownDevices:
                self.knownDevices = {}

            if device not in self.knownDevices:
                self.knownDevices[device] = device

            deviceList.append(self.knownDevices[device])


        return deviceList



    def ShowSetSpeedLimitDialog(self):
        selectedDevice = self.GetSelectedDevice()
        if (selectedDevice):
            self.setSpeedLimitDialog = SetSpeedLimitDialog(selectedDevice)
            self.setSpeedLimitDialog.show()
        else:
            pass

    def GetSelectedDevice(self):
        deviceList = self.ui.DeviceList.selectedItems()
        if (len(deviceList) > 0):
            return deviceList[0].text()
        else:
            return None

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.SaveKnownDevices()
            Connection().Close()
            self.close()
        if event.key() == Qt.Key_Enter:
            self.ConnectClick()

    def closeEvent(self, event):
        print('close')

