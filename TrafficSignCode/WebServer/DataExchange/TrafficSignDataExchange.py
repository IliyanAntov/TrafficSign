import socket
import sys
import select
import struct
import threading
import time
from DataExchange.Connection import Connection

class TrafficSignDataExchange():

    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('localhost', 65432))
        self.socket.listen(100)

    def WaitForConnection(self):
        self.deviceSocket, self.deviceAddress = self.socket.accept()
        print ("Traffic sign connected at ", self.deviceAddress)
        return True

    def ExchangeInformation(self):
        Connection().deviceList.append('Oshte edin')
        while True:
            request = b'details'
            self.deviceSocket.send(request)
            data = self.deviceSocket.recv(100)
