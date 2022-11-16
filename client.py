import socket

serverPort = ("127.0.0.1", 65000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b"Hello UDP Server", serverPort)

serverMessage = sock.recvfrom(1024)
msg = "Message from Server {}".format(serverMessage[0])

print(msg)