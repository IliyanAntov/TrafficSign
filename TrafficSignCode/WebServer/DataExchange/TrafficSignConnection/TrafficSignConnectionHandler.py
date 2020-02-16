import socket

from DataExchange.TrafficSignConnection.TrafficSignDataExchange import (
    TrafficSignDataExchange,
)

# This class is responsible for:
#  - Creating sockets used for traffic sign device connections
#  - Establishing connections to the traffic sign devices
#  - Creating threads for every connected traffic sign device
class TrafficSignConnectionHandler:

    # Constructor method
    def __init__(self):
        super().__init__()
        self.address = "0.0.0.0"  # IPv4 address used for the web server socket (listen on all addresses)
        self.port = 19119  # Traffic sign device port

        # Create an unwrapped IPv4 TCP socket object
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Allow the server to bind to an address which is in a TIME_WAIT state
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind the socket to the given address and port
        self.socket.bind((self.address, self.port))
        # Enable the server to accept connections
        self.socket.listen()

    # Waits for an incoming traffic sign device connection
    def WaitForConnection(self):
        # Accept the connection
        self.deviceSocket, self.deviceAddress = self.socket.accept()
        print("Traffic sign connected at ", self.deviceAddress)
        # Create a data exchange thread for the connection
        deviceThread = TrafficSignDataExchange(self.deviceSocket)
        # Start the thread
        deviceThread.start()
        return True
