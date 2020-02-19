# Echo server program
import socket
import time
import threading

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50026             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen(3)

#CREA LLISTA
llistaCon = []

#ACEPTA CLIENTS
def acceptClient ():
    while True:
        llistaCon.append(s.accept())

        t2 = threading.Thread(target=recibir, args=(llistaCon[-1],))
        t2.daemon = True
        t2.start()


#INTERCEPTA MISSATGES
def recibir(conn):
    while True:
        m = conn[0].recv(1024)
        #print m
        for x in llistaCon:
            #print x[0]
            #print x[1]
            #print conn
            #print m
            if x[0] != conn[0]:
                x[0].sendall(m)
        if len(m.split(";")) == 2:
            #print m.split(";")[0]

            if m.split(";")[0] == 'Bye\n':
                conn[0].close()
                llistaCon.remove(conn)
                break

#CREA THREAD

t = threading.Thread(target=acceptClient)
t.start()

t.join()
s.close()

"""
conn, addr = s.accept()
conn2, addr2 = s.accept()

def recibir(conn,conn2):
    while True:
        m = conn.recv(1024)

        print m
        conn.sendall(m)
        conn2.sendall(m)

        if m == "Bye":
            conn.sendall(m)

def recibir2(conn,conn2):
    while True:
        m2 = conn2.recv(1024)

        print m2
        conn.sendall(m2)
        conn2.sendall(m2)

        if m2 == "Bye":
            conn.sendall(m2)
"""
"""
t1 = threading.Thread(target=recibir2, args=(conn,conn2))
t1.daemon = True
t1.start()


t2 = threading.Thread(target=recibir, args=(conn,conn2))
t2.start()

#t1.join()
t2.join()

s.close()
"""
