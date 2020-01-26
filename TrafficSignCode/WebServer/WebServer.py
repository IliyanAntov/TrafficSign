import socket
import sys
import select
import struct
import threading
import time
from DataExchange.Connection import Connection
from DataExchange.TrafficSignConnection.TrafficSignConnectionHandler import TrafficSignConnectionHandler
from DataExchange.AdminConnection.AdminAppConnectionHandler import AdminAppConnectionHandler


def HandleAdminConnections():
    while True:
        adminConnection = adminConnections.WaitForConnection()

def HandleDeviceConnections():
    while True:
         deviceConnection = deviceConnections.WaitForConnection()

if __name__ == '__main__':

    adminConnections = AdminAppConnectionHandler()
    deviceConnections = TrafficSignConnectionHandler()

    threading.Thread(target=HandleAdminConnections).start()
    threading.Thread(target=HandleDeviceConnections).start()

    #threading.Thread(target = AdminConnectionHandler).start()
    #threading.Thread(target = DeviceConnectionHandler).start()


#server_socket.close()