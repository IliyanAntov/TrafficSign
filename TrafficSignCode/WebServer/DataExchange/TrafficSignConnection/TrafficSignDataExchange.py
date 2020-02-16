import socket

from threading import Thread

from DataExchange.Connection import Connection

# This class is responsible for:
#  - Receiving the IMEI of each connected traffic sign device
#  - Adding entries in the list of available devices
class TrafficSignDataExchange(Thread):

    # Constructor method
    def __init__(self, socket):
        super().__init__()
        # Traffic sign device socket
        self.socket = socket

    # Executes when the thread.start() method is called
    def run(self):
        # Add the current device socket to the list of available devices
        self.AddDevice(self.socket)

    # Adds the socket to the available device list
    def AddDevice(self, socket):
        # Receive the device's IMEI
        incoming = socket.recv(30)
        # Split the received data for easier manipulation
        data = incoming.decode("utf-8").split(" ")
        # If the IMEI was received correctly:
        if data[0] == "IMEI:" and len(data) > 1:
            # Add the socket to the deviceList dictionary
            # (key == IMEI, value == socket)
            Connection().deviceList[data[1]] = socket
            print("Success")
        # If the IMEI was not received correctly:
        else:
            print("Something went wrong")
