import socket
import sys
import select
import struct
import threading
import time
from DataExchange.Connection import Connection


class AdminAppDataExchange():

    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('localhost', 8220))
        self.socket.listen(5)

    def WaitForConnection(self):
        print ("Listening for client . . .")
        self.adminSocket, self.adminAddress = self.socket.accept()
        print ("Connected to client at ", self.adminAddress)
        maxConnectionAttempts = 1
        connectionAttemptsCount = 1
        while True:
            returnCode = self.AuthenticateUser()
            if(returnCode == 0): #Username or password incorrect
                connectionAttemptsCount+=1
                if(connectionAttemptsCount > maxConnectionAttempts):
                    print("Too many login attempts, closing connection...")
                    self.adminSocket.close()
                    return False
            elif(returnCode == 1): #Username and password correct
                print("Authenticated")
                return True
            elif(returnCode == 2): #Connection closed by client
                print("Connection closed by remote client")
                return False

    def AuthenticateUser(self):
        username = Connection().ReceiveMessage(self.adminSocket)
        if(username == None):
            return 2 #Connection closed by client
        else:
            password = Connection().ReceiveMessage(self.adminSocket)

        if (username and password) != None:
            if (username == b"admin" and password == b"1234"):
                print("Client at ",self.adminAddress, " authorized")
                Connection().SendMessage(self.adminSocket, b"auth")
                return 1 #Username and password correct
            else:
                print("Client at ",self.adminAddress, " not authorized")
                Connection().SendMessage(self.adminSocket, b"nauth")
                return 0 #Username or password incorrect
        else:
            print("Something went wrong...")
            self.adminSocket.close()

    def ListenToUser(self):
        while True:
            data = Connection().ReceiveMessage(self.adminSocket)
            print(data)
            if(data == None):
                break
            else:
                #data = str.decode(data, 'utf-8')
                if(data == b"GetDevices"):
                    Connection().SendMessage(self.adminSocket, str.encode(str(len(Connection().deviceList))))
                    for i in range(len(Connection().deviceList)):
                        Connection().SendMessage(self.adminSocket, str.encode(Connection().deviceList[i]))
        self.adminSocket.close()
