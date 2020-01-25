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


class Connection():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    deviceList = []
    
    @staticmethod
    def SendMessage(data):
        length = len(data)
        Connection().client_socket.sendall(struct.pack('!I', length))
        Connection().client_socket.sendall(data)

    @staticmethod
    def ReceiveMessage():
        lengthbuf = Connection().ReceiveAll(4)
        if not lengthbuf:
            return None
        length, = struct.unpack('!I', lengthbuf)
        return Connection().ReceiveAll(length)

    @staticmethod
    def ReceiveAll(count):
        buf = b''
        while count:
            newbuf = Connection().client_socket.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    @staticmethod
    def Close():
        print("Closing connection...")
        Connection().client_socket.close()
