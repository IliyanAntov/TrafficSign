import socket
import sys
import select
import struct


# def send_one_message(sock, data):
#     length = len(data)
#     sock.sendall(struct.pack('!I', length))
#     sock.sendall(data)

# def recv_one_message(sock):
#     lengthbuf = recvall(sock, 4)
#     if not lengthbuf:
#         sock.close()
#     else:
#         length, = struct.unpack('!I', lengthbuf)
#         return recvall(sock, length)

# def recvall(sock, count):
#     buf = b''
#     while count:
#         newbuf = sock.recv(count)
#         if not newbuf: return None
#         buf += newbuf
#         count -= len(newbuf)
#     return buf


class Connection():
    def __init__(self):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('localhost', 8220))
        self.server_socket.listen(5)

    def WaitForAdminConnection(self):
        print ("Listening for client . . .")
        self.admin_socket, self.admin_address = self.server_socket.accept()
        print ("Connected to client at ", self.admin_address)
        maxConnectionAttempts = 1
        connectionAttemptsCount = 1
        while True:
            returnCode = self.AuthenticateAdminConnection()
            if(returnCode == 0): #Username or password incorrect
                connectionAttemptsCount+=1
                if(connectionAttemptsCount > maxConnectionAttempts):
                    print("Too many login attempts, closing connection...")
                    self.admin_socket.close()
                    return False
            elif(returnCode == 1): #Username and password correct
                print("Authenticated")
                return True
            elif(returnCode == 2): #Connection closed by client
                print("Connection closed by remote client")
                return False



    def AuthenticateAdminConnection(self):
        username = self.ReceiveMessage(self.admin_socket)
        if(username == None):
            return 2 #Connection closed by client
        else:
            password = self.ReceiveMessage(self.admin_socket)

        if (username and password) != None:
            if (username == b"admin" and password == b"1234"):
                print("authorized")
                self.SendMessage(self.admin_socket, b"auth")
                return 1 #Username and password correct
            else:
                print("not authorized")
                self.SendMessage(self.admin_socket, b"nauth")
                return 0 #Username or password incorrect
        else:
            print("error")
            self.admin_socket.close()

    def SendMessage(self, sock, data):
        length = len(data)
        sock.sendall(struct.pack('!I', length))
        sock.sendall(data)

    def ReceiveMessage(self, sock):
        lengthbuf = self.ReceiveAll(sock, 4)
        if not lengthbuf:
            return None
        length, = struct.unpack('!I', lengthbuf)
        return self.ReceiveAll(sock, length)

    def ReceiveAll(self, sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf

if __name__ == '__main__':
    connection = Connection()
    while True:
        if connection.WaitForAdminConnection():
            print("success")

#server_socket.close()