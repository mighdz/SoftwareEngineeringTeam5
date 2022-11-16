import socket
import random
import time

Host = "127.0.0.1"
Port = 7500

server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
server_socket.bind((Host, Port))

print("UDP server listening")

byteAddressPair = server_socket.recvfrom(7501)
msg = byteAddressPair[0]
address = byteAddressPair[1]
c_msg = "Message from Client:{}".format(msg)
c_port = "Client IP Address:{}".format(address)

print(c_msg)
print(c_port)

red1 = random.randint(1,5)
red2 = random.randint(1,5)
while (red1 == red2):
    red2 = random.randint(1,5)

red1 = str(red1)
red2 = str(red2)

green1 = random.randint(6,10)
green2 = random.randint(6,10)
while (green1 == green2):
    green2 = random.randint(6,10)

green1 = str(green1)
green2 = str(green2)

counter = random.randint(1,10)
print(counter)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

i = 0
total_msg = ""
redPoints = 0
greenPoints = 0

while i < int(counter):
    if random.randint(1,2) == 1:
        redplayer = red1
    else:
        redplayer = red2
    if random.randint(1,2) == 1:
        greenplayer = green1
    else:
        greenplayer = green2
    
    if random.randint(1,2) == 1:
        msg = "Red player " + redplayer + " shot Green player " + greenplayer
        redPoints += 1
    else:
        msg = "Green player " + greenplayer + " shot Red player " + redplayer
        greenPoints += 1
    
    if i == 0:
        total_msg += msg
    else:
        total_msg += " , " + msg
    i += 1

server_socket.sendto(str.encode(str(total_msg)), address)
server_socket.sendto(str.encode(str(redPoints)), address)
server_socket.sendto(str.encode(str(greenPoints)), address)
time.sleep(random.randint(1,3))
print("program complete")