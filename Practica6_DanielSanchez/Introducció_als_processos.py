from multiprocessing import Process
import time
import datetime


def t(s):
    while (True):
        time.sleep(s)
        print(datetime.datetime.now().time())

def main():
    p = Process(target=t,args=(1,))
    p.start()

    for i in range(10):
        time.sleep(0.5)
        print(p.pid)
    p.terminate()
    print "fi"
if __name__ == '__main__':

    main()
