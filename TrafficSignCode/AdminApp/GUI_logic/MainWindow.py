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
from GUI.SetAliasDialog.SetAliasDialog import Ui_SetAliasDialog
from GUI.LoginDialog.LoginDialog import Ui_LoginDialog
from GUI.DetailsDialog.DetailsDialog import Ui_DetailsDialog
from DataExchange.DataExchange import DataExchange
from DataExchange.Connection import Connection
from GUI_logic.LoginDialog import LoginDialog
from GUI_logic.SetSpeedLimitDialog import SetSpeedLimitDialog
from GUI_logic.SetAliasDialog import SetAliasDialog
from GUI_logic.DetailsDialog import DetailsDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.LoadKnownDevices()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.SetupButtons()
        self.AdjustUI()
        self.connection = DataExchange()

    def SetupButtons(self):
        self.ui.SetSpeedLimitButton.clicked.connect(self.ShowSetSpeedLimitDialog)
        self.ui.RefreshButton.clicked.connect(self.UpdateDeviceList)
        self.ui.SetListEntryAliasButton.clicked.connect(self.ShowSetAliasDialog)
        self.ui.DetailsButton.clicked.connect(self.ShowDetailsDialog)

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
        self.setWindowIcon(QIcon('./GUI/images/icon.png'))


    def UpdateDeviceList(self):
        DataExchange().GetDevices()
        self.ui.DeviceList.setDisabled(True)
        self.ui.DeviceList.clear()

        deviceList = self.GenerateDeviceList()
        for device in deviceList:
            self.ui.DeviceList.addItem(device)
    
        self.ui.DeviceList.setDisabled(False)

    def GenerateDeviceList(self):
        deviceList = []
        for device in Connection().deviceList:
            device = device.decode('utf-8')
            if device not in Connection().knownDevices.values():
                Connection().knownDevices[device] = device

            deviceList.append(list(Connection().knownDevices.keys())[list(Connection().knownDevices.values()).index(device)])

        return deviceList


    def LoadKnownDevices(self):
        with open("./GUI_logic/DeviceAliases.yaml", 'r') as stream:
            try:
                loaded = yaml.safe_load(stream)
                for key, value in loaded.items():
                    Connection().knownDevices[key] = value

                print(Connection().knownDevices)
            except yaml.YAMLError as exc:
                print(exc)

    def SaveKnownDevices(self):
        with open("./GUI_logic/DeviceAliases.yaml", 'w', encoding='utf-8') as outfile:
            yaml.dump(Connection().knownDevices, outfile, default_flow_style=False, allow_unicode=True)


    def ShowSetSpeedLimitDialog(self):
        selectedDevice = self.GetSelectedDevice()
        if (selectedDevice):
            self.setSpeedLimitDialog = SetSpeedLimitDialog(selectedDevice)
            self.setSpeedLimitDialog.show()
        else:
            pass

    def ShowSetAliasDialog(self):
        selectedDevice = self.GetSelectedDevice()
        if (selectedDevice):
            self.setAliasDialog = SetAliasDialog(selectedDevice)
            result = self.setAliasDialog.exec_()
            if(result == QDialog.Accepted):
                self.UpdateDeviceList()
        else:
            pass

    def ShowDetailsDialog(self):
        alias = self.GetSelectedDevice()
        IMEI = Connection().knownDevices[alias]
        incoming = self.connection.GetDeviceDetails(IMEI)
        if(incoming == 'Unreachable'):
            return
        details = incoming.split(' ')
        status = details[0]
        if(status == 'unk'):
            status = 'No information'
        elif(status == 'spd'):
            status = "Speed limit"
        value = details[1]
        if(value == 'unk'):
            value = 'No information'
        self.detailsDialog = DetailsDialog(alias, IMEI, status, value)
        result = self.detailsDialog.exec_()


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

    def closeEvent(self, event):
        self.SaveKnownDevices()
        Connection().Close()
        self.close()

