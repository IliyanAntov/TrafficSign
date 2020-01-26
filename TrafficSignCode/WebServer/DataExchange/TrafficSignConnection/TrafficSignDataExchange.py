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
        incoming = socket.recv(30)
        data = incoming.decode('utf-8').split(' ')
        if(data[0] == "IMEI:" and len(data) > 1):
            Connection().deviceList[data[1]] = socket
            print("Success")
        else:
            print("Something went wrong")
        socket.send(b'ok')

        # while True:
        #     #request = b'details'
        #     #self.deviceSocket.send(request)
        #     data = socket.recv(30)
        #     print(data.decode('utf-8'))
        #     socket.send(b'zdrasti')
