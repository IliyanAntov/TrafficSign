import socket
import sys
import select
import struct
import threading
import time
from threading import Thread
from DataExchange.Connection import Connection

class TrafficSignDataExchange(Thread):

    def __init__(self, socket):
        super().__init__()
        self.socket = socket

    def run(self):
        self.ExchangeInformation(self.socket)

    def ExchangeInformation(self, socket):
        Connection().deviceList.append('Oshte edin')
        data = socket.recv(30)
        IMEI = data.decode('utf-8')
        socket.send(b'ok')
        Connection().deviceList.append(IMEI)
        while True:
            #request = b'details'
            #self.deviceSocket.send(request)
            data = socket.recv(30)
            print(data.decode('utf-8'))
            socket.send(b'zdrasti')
