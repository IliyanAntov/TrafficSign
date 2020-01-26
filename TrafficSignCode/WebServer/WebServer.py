import socket
import sys
import select
import struct
import threading
import time
from DataExchange.Connection import Connection
from DataExchange.TrafficSignConnection.TrafficSignConnectionHandler import TrafficSignConnectionHandler
from DataExchange.AdminConnection.AdminAppConnectionHandler import AdminAppConnectionHandler


if __name__ == '__main__':

    adminConnections = AdminAppConnectionHandler()
    deviceConnections = TrafficSignConnectionHandler()
    while True:
        adminConnection = adminConnections.WaitForConnection()
        deviceConnection = deviceConnections.WaitForConnection()
    #threading.Thread(target = AdminConnectionHandler).start()
    #threading.Thread(target = DeviceConnectionHandler).start()

#server_socket.close()