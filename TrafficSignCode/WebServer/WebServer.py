import socket
import sys
import select
import struct

host = 'localhost'
port = 8220
address = (host, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(address)
server_socket.listen(5)

print ("Listening for client . . .")
conn, address = server_socket.accept()
print ("Connected to client at ", address)

def send_one_message(sock, data):
    length = len(data)
    sock.sendall(struct.pack('!I', length))
    sock.sendall(data)

def recv_one_message(sock):
    lengthbuf = recvall(sock, 4)
    length, = struct.unpack('!I', lengthbuf)
    return recvall(sock, length)

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf


username = recv_one_message(conn)
password = recv_one_message(conn)
print(username)
print(password)
if (username and password) != None:
    if (username == b"admin" and password == b"1234"):
        print("authorized")
        send_one_message(conn, b"auth")
        conn.close()
    else:
        print("not authorized")
        send_one_message(conn, b"nauth")
        conn.close()
        
else:
    conn.close()
server_socket.close()