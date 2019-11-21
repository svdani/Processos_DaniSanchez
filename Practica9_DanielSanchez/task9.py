#-*- coding: utf8 -*-
#4523

# 40 / 2 = 20
# 40 / 4 = 10
from datetime import datetime
import multiprocessing
from multiprocessing import Pool

def primers(num):
    for i in range(2, num/2):
        if num % i == 0:
            return False
        else:
            pass
    return True

if __name__ == '__main__':
    #l = range(40000000, 40000100)#[45445535, 56534563, 43566487, 43635453, 52346557, 53454433, 43546453, 26847357, 54577647]
    start = datetime.now()
    pool = multiprocessing.Pool(processes=1)
    results = pool.map(primers, range(40000000, 40000100))
    print (results)
    #for i in l:
    #    s = primers(i)
    #    print i, s
    print datetime.now() - start
#processes=10  0:02:59.477146
#processes=3   0:00:55.479283
#porcesses=2   0:01:01.447212
#porcesses=4   0:00:56.231540
#porcesses=5   0:01:03.510401
#porcesses=1   0:01:09.347565
#EL PROCES MES RAPID A SIGUT AMB 3 Y A CONTINUACIO 4 AMB UNA DIFERENCIA DE 1 SEGON, CREC QUE
#ES PERQUE SON ELS MES PROPER AL MAXIM DE PROCESADOR DEL ORDINADOR Y CREC QUE EL DE 3 ES ALGO 
#MES RAPID PERQUE TE MARGE A TENIR UN PROCESADOR LLIURE
