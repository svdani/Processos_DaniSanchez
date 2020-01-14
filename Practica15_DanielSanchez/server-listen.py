# Echo server program
import socket
import time

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST,PORT))


while True:
    m = s.recvfrom(1024)
    if m[0] == "Bye":
        sleep(1)
    else:
        print m[0]
s.close()
