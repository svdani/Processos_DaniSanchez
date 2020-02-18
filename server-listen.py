# Echo server program
import socket
import time
import threading

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50022             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen(3)

#CREA LLISTA
llistaCon = []

#ACEPTA CLIENTS
def acceptClient ():
    while True:
        llistaCon.append(s.accept())

        t2 = threading.Thread(target=recibir, args=(llistaCon[-1][0],))
        t2.daemon = True
        t2.start()


#INTERCEPTA MISSATGES
def recibir(conn):
    while True:
        m = conn.recv(1024)
        for x in llistaCon:
            #print x[0]
            #print conn
            #print m
            if x[0] != conn:
                x[0].sendall(m)

        if m == "Bye" or m =="Bye\n":

            conn.sendall(m)

#CREA THREAD
while True:

    t = threading.Thread(target=acceptClient)
    t.start()

    t.join()
s.close()


