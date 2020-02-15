import socket
import ssl
import time
import struct

# This class is responsible for creating a socket and sending information to the server
class Connection:
    # Creates an unwrapped IPv4 TCP socket object
    unwrapped = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations("./DataExchange/Certificates/TrafficSignAppAdminConnectionCert.pem")
    client_socket = context.wrap_socket(
        unwrapped, server_hostname = "TrafficSignAdminApp"  #The unwrapped socket
    )

    client_socket.settimeout(10)
    deviceList = []  # device IMEIs
    knownDevices = {}  # key == Alias, value == IMEI

    @staticmethod
    def SendMessage(data):
        length = len(data)
        Connection().client_socket.sendall(struct.pack("!I", length))
        Connection().client_socket.sendall(data)

    @staticmethod
    def ReceiveMessage():
        lengthbuf = Connection().ReceiveAll(4)
        if not lengthbuf:
            return None
        (length,) = struct.unpack("!I", lengthbuf)
        return Connection().ReceiveAll(length)

    @staticmethod
    def ReceiveAll(count):
        buf = b""
        while count:
            newbuf = Connection().client_socket.recv(count)
            if not newbuf:
                return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    @staticmethod
    def Close():
        print("Closing connection...")
        Connection().client_socket.close()
