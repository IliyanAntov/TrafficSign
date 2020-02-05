import socket
import sys
import select
import struct
import threading
import time
from threading import Thread
from DataExchange.Connection import Connection
from DataExchange.TrafficSignConnection.TrafficSignDataExchange import TrafficSignDataExchange


class AdminAppDataExchange(Thread):

    def __init__(self, socket):
        super().__init__()
        self.socket = socket

    def run(self):
        self.ListenToUser()

    def ListenToUser(self):
        while True:
            data = Connection().ReceiveMessage(self.socket)
            print(data)
            if(data == None):
                print('Closing thread...')
                self.socket.close()
                return
            else:
                self.HandleUserRequest(data.decode('utf-8'))
                #data = str.decode(data, 'utf-8')

    def HandleUserRequest(self, data):
        commands = data.split(' ')
        if(len(commands) > 1):
            request = commands.pop(0)
            if(request == "GET"):
                self.HandleGetRequest(commands)
            elif(request == "SET"):
                self.HandleSetRequest(commands)
        else:
            print("Something went wrong")
    
    def HandleGetRequest(self, request):
        if(request[0] == "devices"):
            devicesLength = len(Connection().deviceList)
            Connection().SendMessage(self.socket, str.encode(str(devicesLength), encoding="utf-8"))
            for i in Connection().deviceList:
                Connection().SendMessage(self.socket, str.encode(str(i), encoding="utf-8"))
            return

        elif(request[0] == "details"):
            targetIMEI = request[1]
            details = Connection().SendGetRequest(targetIMEI, 'dtl')
            if not details:
                details = b'error'
            Connection().SendMessage(self.socket, details)

        else:
            print('Unknown request')
            return
        

    def HandleSetRequest(self, commands):
        targetIMEI = commands.pop(0)
        request = commands.pop(0)
        value = commands.pop(0)

        Connection().SendSetRequest(targetIMEI, request, value)
        


    
