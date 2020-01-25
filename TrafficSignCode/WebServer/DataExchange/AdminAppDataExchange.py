import socket
import sys
import select
import struct
import threading
from threading import Thread
import time
from DataExchange.Connection import Connection


class AdminAppDataExchange(Thread):

    def __init__(self, socket):
        super().__init__()
        self.socket = socket

    def run(self):
        self.ListenToUser(self.socket)

    def ListenToUser(self, socket):
        while True:
            data = Connection().ReceiveMessage(socket)
            print(data)
            if(data == None):
                break
            else:
                #data = str.decode(data, 'utf-8')
                if(data == b"GetDevices"):
                    Connection().SendMessage(socket, str.encode(str(len(Connection().deviceList))))
                    for i in range(len(Connection().deviceList)):
                        Connection().SendMessage(socket, str.encode(Connection().deviceList[i]))
        socket.close()
