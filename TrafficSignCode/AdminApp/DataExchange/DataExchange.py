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

    def AttemptConnect(self):
        try:
            Connection().client_socket.connect(("localhost", 8220))
            print("Connection successful")
            return True
        except:
            print("Connection to server unsuccessful")
            return False

    def AttemptLogin(self, username, password):
        print("Attempting to log in...")
        try:
            Connection().SendMessage(Connection().client_socket, str.encode(username))
        except:
            return None
        try:
            Connection().SendMessage(Connection().client_socket, str.encode(password))
        except:
            return None
        data = self.WaitForData()
        if not data:
            Connection().Close()
        else:
            return data   

    def WaitForData(self):
        ready = select.select([Connection().client_socket], [], [], 2)
        if ready[0]:
            data = Connection().ReceiveMessage(Connection().client_socket).decode('utf-8')
            return data
        else:
            print("Connection timeout")
            return None
