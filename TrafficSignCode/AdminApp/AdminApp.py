import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 8220))

for index in range(5):
    data = ("GET\nSONAR%d\n\n" % index)
    print ('send to server: %s' %data)
    client_socket.send(str.encode(data))
    while client_socket.recv(2048).decode("utf-8") != "ack":
        print ("waiting for ack")
    print ("ack received!")

#send disconnect message                                                                                                                           
dmsg = b"disconnect"
print ("Disconnecting")
client_socket.send(dmsg)

client_socket.close()