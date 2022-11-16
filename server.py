import socket
import random
import time

Host = "127.0.0.1"
Port = 65000

server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
server_socket.bind((Host, Port))

print("UDP server listening")

byteAddressPair = server_socket.recvfrom(1024)
msg = byteAddressPair[0]
address = byteAddressPair[1]
c_msg = "Message from Client:{}".format(msg)
c_port = "Client IP Address:{}".format(address)

print(c_msg)
print(c_port)
print("program complete")