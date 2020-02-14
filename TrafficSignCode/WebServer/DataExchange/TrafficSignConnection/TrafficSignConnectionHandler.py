import socket

from DataExchange.TrafficSignConnection.TrafficSignDataExchange import TrafficSignDataExchange

class TrafficSignConnectionHandler():

    def __init__(self):
        super().__init__()
        self.address = '0.0.0.0'
        self.port = 19119
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.address, self.port))
        self.socket.listen(100)

    def WaitForConnection(self):
        self.deviceSocket, self.deviceAddress = self.socket.accept()
        print ("Traffic sign connected at ", self.deviceAddress)
        deviceThread = TrafficSignDataExchange(self.deviceSocket)
        deviceThread.start()
        return True