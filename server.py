import socket
import random
import time

Host = "127.0.0.1"
Port = 65000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((Host, Port))

print("UDP server listening")

byteAddressPair = sock.recvfrom(1024)
msg = byteAddressPair[0]
address = byteAddressPair[1]
c_msg = "Message from Client:{}".format(msg)
c_port = "Client IP Address:{}".format(address)

print(c_msg)
print(c_port)
print("program complete")