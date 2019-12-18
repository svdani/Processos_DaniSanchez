# -*- coding: utf8 -*-
import md5, random, sys, time
import time
from multiprocessing import Process, Semaphore, Pipe

def busca(x, s):
    s.acquire()
    f = open('fitxer.txt', 'r')
    fr = f.read()
    index = fr.find('\n'+x+',')
    index2 = fr.find('\n', index+1)
    if index == -1:
        pass
    else:
        print fr[index+1:index2]
        f.close()
    s.release()

def substitueix(x, y, s):
    s.acquire()
    f = open('fitxer.txt', 'r')
    fr = f.read()
    f.close()
    index = fr.find('\n'+x+',')
    index2 = fr.find('\n', index+1)
    if index == -1:
        print 'Aquest nombre no existeix'
        s.release()
    else:
        print "\n"+fr[index+1:index2]
        f = open('fitxer.txt', 'w')
        f.write(fr[:index+1])
        f.write(y + ',' + md5.md5(y).hexdigest()+ "\n")
        f.write(fr[index2+1:])
        f.close()
        s.release()
        busca(y, s)

def fill(canalB,s):
    while True:
        canalB.poll()
        x = canalB.recv()
        if x == "q":
            break
        y = canalB.recv()
        if y == "q":
            break
        else:
            substitueix(x,y,s)

def inici():
    f = open('fitxer.txt', 'w')
    for i in range(100):
        f.write(str(i)+ ',' + md5.md5(str(i)).hexdigest()+ "\n")
    f.close()
    #print open('fitxer.txt', 'ro').read()


if __name__ == '__main__' :

    canalA, canalB = Pipe()
    s = Semaphore()
    p = Process(target=fill, args=(canalB,s))
    inici()
    p.start()

    while True:
        time.sleep(1)
        x = raw_input("Intrudueix un nombre substituir:")

        if x.isdigit():
            canalA.send(x)
        else x == "q":
            print "Adeu"
            p.join()
            break

        y = raw_input("Intrudueix un nombre nou:")
        if y.isdigit():
            canalA.send(y)
        if y == "q":
            print "Adeu"
            p.join()
            break
