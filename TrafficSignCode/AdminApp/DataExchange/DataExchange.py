import socket
import time
import sys
import select
import struct
# from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QRegExpValidator
from PyQt5.QtCore import pyqtSlot, Qt, QRegExp
from DataExchange.Connection import Connection


class DataExchange():

    def __init__(self):
        super().__init__()
        #self.serverAddress = "3.125.80.10"
        self.serverAddress = "localhost"
        self.serverPort = 26418

    def AttemptConnect(self):
        try:
            Connection().client_socket.connect((self.serverAddress, self.serverPort))
            print("Connection successful")
            return True
        except:
            print("Connection to server unsuccessful")
            return False

    def AttemptLogin(self, username, password):
        print("Attempting to log in...")
        try:
            Connection().SendMessage(str.encode(username))
        except:
            return None
        try:
            Connection().SendMessage(str.encode(password))
        except:
            return None
        data = self.WaitForData()
        if not data:
            Connection().Close()
        else:
            return data   

    def GetDevices(self):
        Connection().SendMessage(str.encode("GET devices"))
        deviceLen = Connection().ReceiveMessage()
        Connection().deviceList.clear()
        for i in range (int(deviceLen)):
            device = Connection().ReceiveMessage()
            Connection().deviceList.append(device)

    def GetDeviceDetails(self, target):
        Connection().SendMessage(str.encode("GET details " + target))
        details = Connection().ReceiveMessage().decode('utf-8')
        return details

    def SetSpeedLimit(self, target, speedLimit):
        Connection().SendMessage(str.encode("SET " + target +  " speed " + speedLimit))

    def SetWarning(self, target, request):
        Connection.SendMessage(str.encode("SET " + target + " warning " + request))


    def WaitForData(self):
        ready = select.select([Connection().client_socket], [], [], 2)
        if ready[0]:
            data = Connection().ReceiveMessage().decode('utf-8')
            return data
        else:
            print("Connection timeout")
            return None
