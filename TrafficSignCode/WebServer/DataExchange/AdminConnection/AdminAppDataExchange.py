import socket

from threading import Thread

from DataExchange.Connection import Connection

# This class is responsible for:
#  - Receiving requests from the admin application
#  - Forwarding the requests to the appropriate traffic sign device
#  - Sending responses to the admin application
class AdminAppDataExchange(Thread):

    # Constructor method
    def __init__(self, socket):
        super().__init__()
        # Admin application socket
        self.socket = socket

    # Executes when the thread.start() method is called
    def run(self):
        # Listen to user requests
        self.ListenToUser()

    # Reads and processes user requests
    def ListenToUser(self):
        # Run until the connection is closed
        while True:
            # Receive message from the admin application
            data = Connection().ReceiveMessage(self.socket)
            print(data)
            # If the connection was closed:
            if data == None:
                print("Closing thread...")
                # Close the socket
                self.socket.close()
                # End the infinite loop (close the thread)
                return
            else:
                # Handle the received request
                self.HandleUserRequest(data.decode("utf-8"))

    # Handles the received user request
    def HandleUserRequest(self, data):
        # Split the commands for easier manipulation
        commands = data.split(" ")
        # If the command is in a valid format:
        if len(commands) > 1:
            # Save the request
            request = commands.pop(0)
            if request == "GET":
                # Handle the GET request
                self.HandleGetRequest(commands)
            elif request == "SET":
                # Handle the SET request
                self.HandleSetRequest(commands)
        # If something went wrong and the command is invalid:
        else:
            print("Something went wrong")

    # Handles any received GET requests
    def HandleGetRequest(self, request):
        # "GET devices" request
        if request[0] == "devices":
            # Calculate the amount of available devices
            devicesLength = len(Connection().deviceList)
            # Send the device length to the admin application
            Connection().SendMessage(
                self.socket, str.encode(str(devicesLength), encoding="utf-8")
            )
            # Send the IMEI of every available device to the admin application
            for i in Connection().deviceList:
                Connection().SendMessage(
                    self.socket, str.encode(str(i), encoding="utf-8")
                )
            return
        # "GET details <IMEI>" request
        elif request[0] == "details":
            # Save the target device IMEI
            targetIMEI = request[1]
            # Send a "GET dtl" request to the appropriate device
            details = Connection().SendGetRequest(targetIMEI, "dtl")
            # If the device is unavailable:
            if not details:
                # Generate error
                details = b"error"
            # Send the details to the admin application
            Connection().SendMessage(self.socket, str.encode(details, encoding="utf-8"))
        # Request unknown:
        else:
            # Do nothing
            print("Unknown request")
            return

    # Handles any received SET requests
    def HandleSetRequest(self, commands):
        # Save the target device IMEI
        targetIMEI = commands.pop(0)
        # Save the request
        request = commands.pop(0)
        # Save the value
        value = commands.pop(0)
        # Send a SET request to the device and save the response
        response = Connection().SendSetRequest(targetIMEI, request, value)
        # Send the response to the admin application
        Connection().SendMessage(self.socket, str.encode(response))

