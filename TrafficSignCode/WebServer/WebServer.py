import socket
import sys
import select
import struct
import threading
import time
from DataExchange.Connection import Connection
#from DataExchange.AdminAppDataExchange import AdminAppDataExchange
from DataExchange.TrafficSignDataExchange import TrafficSignDataExchange
from DataExchange.AdminAppConnectionHandler import AdminAppConnectionHandler


if __name__ == '__main__':

    adminConnections = AdminAppConnectionHandler()
    #deviceConnections = AdminAppConnectionHandler()
    while True:
        result = adminConnections.WaitForConnection()
    #threading.Thread(target = AdminConnectionHandler).start()
    #threading.Thread(target = DeviceConnectionHandler).start()

#server_socket.close()