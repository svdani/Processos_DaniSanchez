# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    n = raw_input("Introdueix text")
    s.sendto(n, (HOST,PORT))
    if n in "Bye":
        break
s.close()
