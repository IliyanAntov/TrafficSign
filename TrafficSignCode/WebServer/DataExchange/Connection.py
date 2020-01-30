import socket
import sys
import select
import struct
import threading
import time

class Connection():

    deviceList = {"TestDevice1": 'glupost'}

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
            if not newbuf:
                return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    @staticmethod
    def SendSetRequest(targetIMEI, request, amount):
        if(targetIMEI in Connection().deviceList):
            deviceSocket = Connection().deviceList[targetIMEI]
            if(request == 'speed'):
                request = 'spd'
            elif(request == 'warning'):
                request = 'wrn'
            toSend = "SET " + request + " " + amount + "\n"
            print(toSend)
            deviceSocket.send(str.encode(toSend))
            #deviceSocket.send(str.encode(amount + "\n"))
        else:
            print("Requested device not found")
            return

