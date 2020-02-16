import socket
import select
import struct


class Connection:

    # Traffic sign device list
    deviceList = {"5432552352345": "not_a_socket1", "7223462356245": "not_a_socket2"}

    # Sends a message to the socket in the agreed format
    @staticmethod
    def SendMessage(sock, data):
        length = len(data)
        # Send the length of the message
        sock.sendall(
            struct.pack("!I", length)  # Pack the length in unsigned int format
        )
        # Send the message itself
        sock.sendall(data)

    # Receives a message from the the socket
    @staticmethod
    def ReceiveMessage(sock):
        # Receive the message length
        bufferLength = Connection().ReceiveAll(sock, 4)
        if not bufferLength:
            return None
        # Unpack the length
        (length,) = struct.unpack("!I", bufferLength)
        # Receive the whole message
        return Connection().ReceiveAll(sock, length)

    # Receives the requested <count> bytes from the socket
    @staticmethod
    def ReceiveAll(sock, count):
        # Create a byte buffer to store the message
        buffer = b""
        # Receive <count> bytes
        while count:
            # Receive all currently available bytes (max <count>)
            newBuffer = sock.recv(count)
            if not newBuffer:
                return None
            # Write to the buffer
            buffer += newBuffer
            # Substract the length of the received bytes from the expected amount
            count -= len(newBuffer)
        # Return the message
        return buffer

    # Sends a SET request to the target traffic sign device
    @staticmethod
    def SendSetRequest(targetIMEI, request, value):
        # If the requested traffic sign device is available:
        if targetIMEI in Connection().deviceList.keys():
            # Get the device socket
            deviceSocket = Connection().deviceList[targetIMEI]

            # Compress the request and value into the required format for traffic sign device messages
            request = Connection().CompressRequest(request)
            value = Connection().CompressValue(value)

            # Generate the string that is going to be sent to the device
            toSend = "SET " + request + " " + value + "\n"
            print(toSend)

            try:
                # Send the request to the appropriate socket
                deviceSocket.send(str.encode(toSend))
            except:
                return "nosend"

            # Wait for device response; timeout after 5 seconds
            ready = select.select([deviceSocket], [], [], 5)

            if ready[0]:
                # Read the acknowledgement
                data = deviceSocket.recv(2)
                return "success"
            else:
                print("Error, device not responding")
                # Remove the device from the list of available devices
                Connection().deviceList.pop(targetIMEI)
                return "noresp"
        # If the requested traffic sign device is not available:
        else:
            print("Requested device not found")
            return "notfound"

    # Compresses the request received by the admin application to 3 letters
    # (Suitable for traffic sign device messages)
    @staticmethod
    def CompressRequest(request):
        if request == "speed":
            return "spd"
        elif request == "warning":
            return "wrn"

    # Compresses the value received by the admin application to 3 letters
    # (Suitable for traffic sign device messages)
    @staticmethod
    def CompressValue(value):
        if value == "StopSign":
            return "stp"
        elif value == "GeneralWarning":
            return "gnr"
        elif value == "TrafficLight":
            return "tfl"
        elif value == "NoEntry":
            return "nen"
        elif value == "ForwardOnly":
            return "fon"
        elif value == "LeftOnly":
            return "lon"
        elif value == "RightOnly":
            return "ron"
        else:
            return value

    # Sends a GET request to the target traffic sign device
    @staticmethod
    def SendGetRequest(targetIMEI, request):
        #  If the requested traffic sign device is available:
        if targetIMEI in Connection().deviceList:
            # Get the device socket
            deviceSocket = Connection().deviceList[targetIMEI]
            try:
                #  Send the request to the appropriate socket
                deviceSocket.send(str.encode("GET " + request + "\n"))
            except:
                print("Requested device not found")
                return "nosend"

            # Wait for device response; timeout after 5 seconds
            ready = select.select([deviceSocket], [], [], 5)

            if ready[0]:
                # Read the details message
                data = deviceSocket.recv(20)
                # Return the details message
                return data
            else:
                print("Error, device not responding")
                # Remove the device from the list of available devices
                Connection().deviceList.pop(targetIMEI)
                return "noresp"
        # If the requested traffic sign device is not available:
        else:
            print("Requested device not found")
            return "notfound"

