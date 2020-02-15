import socket
import select
import struct


class Connection:

    deviceList = {"5432552352345": "glupost", "7223462356245": "pak glupost"}

    @staticmethod
    def SendMessage(sock, data):
        length = len(data)
        sock.sendall(struct.pack("!I", length))
        sock.sendall(data)

    @staticmethod
    def ReceiveMessage(sock):
        lengthbuf = Connection().ReceiveAll(sock, 4)
        if not lengthbuf:
            return None
        (length,) = struct.unpack("!I", lengthbuf)
        return Connection().ReceiveAll(sock, length)

    @staticmethod
    def ReceiveAll(sock, count):
        buf = b""
        while count:
            newbuf = sock.recv(count)
            if not newbuf:
                return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    @staticmethod
    def SendSetRequest(targetIMEI, request, value):
        if targetIMEI in Connection().deviceList:
            deviceSocket = Connection().deviceList[targetIMEI]

            request = Connection().CompressRequest(request)
            value = Connection().CompressValue(value)

            toSend = "SET " + request + " " + value + "\n"
            print(toSend)
            try:
                deviceSocket.send(str.encode(toSend))
            except:
                return "nosend"

            ready = select.select([deviceSocket], [], [], 5)

            if ready[0]:
                data = deviceSocket.recv(2)
                return "success"
            else:
                print("Error, device not responding")
                Connection().deviceList.pop(targetIMEI)
                return "noresp"

            # deviceSocket.send(str.encode(amount + "\n"))
        else:
            print("Requested device not found")
            return "notfound"

    @staticmethod
    def CompressRequest(request):
        if request == "speed":
            return "spd"
        elif request == "warning":
            return "wrn"

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

    @staticmethod
    def SendGetRequest(targetIMEI, request):
        if targetIMEI in Connection().deviceList:
            deviceSocket = Connection().deviceList[targetIMEI]
            try:
                deviceSocket.send(str.encode("GET " + request + "\n"))
            except:
                print("Requested device not found")
                return None

            ready = select.select([deviceSocket], [], [], 5)

            if ready[0]:
                data = deviceSocket.recv(20)
                return data
            else:
                print("Error, device not responding")
                Connection().deviceList.pop(targetIMEI)
                return None

