import socket
import ssl
import time
import struct

# This class is responsible for:
#  - Creating and discarding a socket object
#  - Sending messages to the web server in the correct format
#  - Receiving messages from the web server
class Connection:
    # Create an unwrapped IPv4 TCP socket object
    unwrapped = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Create an SSLContext object
    context = ssl.SSLContext(
        ssl.PROTOCOL_TLS_CLIENT  # Client side connection (auto-negotiate highest supported SSL/TLS version)
    )

    # Load the certificate used for the application
    context.load_verify_locations(
        "./DataExchange/Certificates/TrafficSignAppAdminConnectionCert.pem"
    )

    # Create a protected SSL/TLS TCP socket if the server hostname is correct
    client_socket = context.wrap_socket(
        sock=unwrapped, server_hostname="TrafficSignAdminApp"
    )

    # Blocking socket operations timeout after 10 seconds
    client_socket.settimeout(10)

    deviceList = []  # Holds all currently available devices' IMEIs
    knownDevices = (  # Holds all known custom user aliases (key == Alias, value == IMEI)
        {}
    )

    # Sends a message to the web server in the agreed format
    @staticmethod
    def SendMessage(data):
        length = len(data)

        # Send the length of the message
        Connection().client_socket.sendall(
            struct.pack("!I", length)  # Pack the length in unsigned int format
        )

        # Send the message itself
        Connection().client_socket.sendall(data)

    # Receives a message from the web server
    @staticmethod
    def ReceiveMessage():
        # Receive the message length
        lengthbuf = Connection().ReceiveAll(4)
        if not lengthbuf:
            return None

        # Unpack the length
        (length,) = struct.unpack("!I", lengthbuf)

        # Receive the whole message
        return Connection().ReceiveAll(length)

    # Receives the requested <count> bytes from the socket
    @staticmethod
    def ReceiveAll(count):
        # Create a byte buffer to store the message
        buf = b""

        # Receive <count> bytes
        while count:
            # Receive all currently available bytes (max <count>)
            newbuf = Connection().client_socket.recv(count)
            if not newbuf:
                return None

            # Write to the buffer
            buf += newbuf

            # Substract the length of the received bytes from the expected amount
            count -= len(newbuf)

        # Return the message
        return buf

    # Closes the socket to the server
    @staticmethod
    def Close():
        print("Closing connection...")

        # Call the .close() method of the socket object
        Connection().client_socket.close()
