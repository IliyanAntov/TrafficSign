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

    @staticmethod
    def SendMessage(sock, data):
        length = len(data)
        sock.sendall(struct.pack('!I', length))
        sock.sendall(data)

    @staticmethod
    def ReceiveMessage(sock):
        lengthbuf = Connection().ReceiveAll(sock, 4)
        if not lengthbuf:
            return None
        length, = struct.unpack('!I', lengthbuf)
        return Connection().ReceiveAll(sock, length)

    @staticmethod
    def ReceiveAll(sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    def Close():
        print("Closing connection...")
        Connection().client_socket.close()
