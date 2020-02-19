import socket
import time
import select
from DataExchange.Connection import Connection

# This class is responsible for:
#  - Establishing and maintaining a connection to the web server
#  - Sending requests to the web server when required by the user
#  - Receiving responses from the web server
class DataExchange:

    # Constructor method
    def __init__(self):
        super().__init__()
        self.serverAddress = (
            "3.125.80.10"  # Static public IPv4 address of the web server
        )
        self.serverPort = 26418  # Application port

    # Attempts to establish a connection to the web server
    def AttemptConnect(self):
        try:
            # Attempt to connect the socket to the given address and port
            Connection().client_socket.connect((self.serverAddress, self.serverPort))
            print("Connection successful")
            # Return True if the connection was successful
            return True
        except:
            print("Connection to server unsuccessful")
            # Return False if an error occurred and the connection was unsuccessful
            return False

    # Attempts to send the entered login information to the web server
    def AttemptLogin(self, username, password):
        print("Attempting to log in...")
        try:
            # Attempt to send the username
            Connection().SendMessage(str.encode(username))
        except:
            # Return None if an error occurred
            return None
        try:
            # Attempt to send the password
            Connection().SendMessage(str.encode(password))
        except:
            # Return None if an error occurred
            return None
        # Wait for a response from the web server
        data = self.WaitForData()
        if not data:
            # If no response is received, close the connection
            Connection().Close()
        else:
            # Return the response
            return data

    # Retrieves the list of available devices from the web server
    def GetDevices(self):
        # Send the "GET devices" request message
        Connection().SendMessage(str.encode("GET devices"))
        # Receive the number of available devices
        deviceLen = self.WaitForData()
        if(deviceLen == "nocon" or deviceLen == "timeout"):
            return deviceLen
        # Clear the device list
        Connection().deviceList.clear()
        if deviceLen:
            # Receive all available devices
            for i in range(int(deviceLen)):
                # Receive the device IMEI
                device = self.WaitForData()
                # Add it to the device list
                Connection().deviceList.append(device)

    # Requests details about one of the available devices
    def GetDeviceDetails(self, target):
        # Send the "GET details <IMEI>" request message
        Connection().SendMessage(str.encode("GET details " + target))
        # Receive the device details message
        details = self.WaitForData()
        # Return the details message
        return details

    # Sends a request to the web server to alter a certain device to display a speed limit sign
    def SetSpeedLimit(self, target, speedLimit):
        # Send the "SET <Target device IMEI> speed <Speed limit>" request message
        Connection().SendMessage(str.encode("SET " + target + " speed " + speedLimit))
        # Receive the server response message
        response = self.WaitForData()
        # Return the response
        return response

    # Sends a request to the web server to alter a certain device to display a warning sign
    def SetWarning(self, target, request):
        # Send the "SET <Target device IMEI> warning <Warning sign>" request message
        Connection().SendMessage(str.encode("SET " + target + " warning " + request))
        # Recieve the server response message
        response = self.WaitForData()
        # Return the response
        return response

    # Waits for data from the web server
    def WaitForData(self):
        # Wait for incoming data on the socket; timeout after 9 seconds
        ready = select.select([Connection().client_socket], [], [], 9)
        if ready[0]:
            try:
                # Read the available message
                data = Connection().ReceiveMessage().decode("utf-8")
                # Return the received message
                return data
            except:
                print("Lost connection to the server")
                # Return connection loss error
                return "nocon"
        else:
            print("Connection timeout")
            # Return timeout error
            return "timeout"
