import socket
import sys
import select
import struct
import threading
import time
from DataExchange.Connection import Connection
from DataExchange.AdminConnection.AdminAppDataExchange import AdminAppDataExchange


class AdminAppConnectionHandler():

    def __init__(self):
        super().__init__()
        self.address = '0.0.0.0'
        self.port = 26418
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.address, self.port))
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
                adminThread = AdminAppDataExchange(self.adminSocket)
                adminThread.start()
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
