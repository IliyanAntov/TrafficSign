import socket
import sys
import select
import struct
import threading
import time
from DataExchange.Connection import Connection
from DataExchange.AdminAppDataExchange import AdminAppDataExchange
from DataExchange.TrafficSignDataExchange import TrafficSignDataExchange


adminConnections = AdminAppDataExchange()
deviceConnections = TrafficSignDataExchange()



def AdminConnectionHandler():
    while True:
        adminSocket = adminConnections.WaitForConnection()
        if adminSocket:
            threading.Thread(target = adminConnections.ListenToUser).start()
            threading.Thread(target = AdminConnectionHandler).start()

def DeviceConnectionHandler():
    while True:
        deviceSocket = deviceConnections.WaitForConnection()
        if deviceSocket:
            threading.Thread(target = deviceConnections.ExchangeInformation).start()
            deviceSocket = None
            


if __name__ == '__main__':

    threading.Thread(target = AdminConnectionHandler).start()
    threading.Thread(target = DeviceConnectionHandler).start()

#server_socket.close()