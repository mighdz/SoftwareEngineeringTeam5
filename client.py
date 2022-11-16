import socket

serverPort = ("127.0.0.1", 65000)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(b"Hello UDP Server", serverPort)

serverMessage = client_socket.recvfrom(1024)
msg = "Message from Server {}".format(serverMessage[0])

print(msg)