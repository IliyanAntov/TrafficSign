import socket
import sys
import select
import struct
import threading
import time
from DataExchange.Connection import Connection
from DataExchange.AdminAppDataExchange import AdminAppDataExchange
from DataExchange.TrafficSignDataExchange import TrafficSignDataExchange

if __name__ == '__main__':

    adminSocket = AdminAppDataExchange()
    trafficSignSocket = TrafficSignDataExchange()

    while True:
        if adminSocket.WaitForConnection():
            threading.Thread(target = adminSocket.ListenToUser).start()
        if trafficSignSocket.WaitForConnection():
            threading.Thread(target = trafficSignSocket.ExchangeInformation).start()

#server_socket.close()