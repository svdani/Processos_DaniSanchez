#-*- coding: UTF-8 -*-

"""Per comencar et demana que junt amb l'execucio del programa indiquis un “argument” que ha de ser un numero entre 0 i 994 sino el programa dona error.
El programa mostra la quantitat de nombres primers que tu hagis indicat en ordre de mes petit a mes gran,
el programa comenca sempre amb una llista vuida y cuando troba una vuida fa que sigui una llista de 2."""
import sys
class llista_primers:

    def __init__(self, n):
        """Declarem la clase “llista_primers” i dins la clase definim la funcio  “__init__”
        que necessita uns arguments en aquest cas un numero al executar el programa el guarda en  “n”,
        y a continuacio crida la funcio “busca()”."""
        self.n = n
        self.llista = []
        self.busca()

    def busca(self):
        """Aqui es declara la funcio “busca()
        Dins la funcio podem veure que el primer de tot es un if que revisa la llista.

        Si la llista te una llargada de 0  agegeix el 2 a la llista i torna a cridar la funcio.

        (sempre esta vuida al principi del programa per tant sempre entra)

        Torna a revisar ara la mida de la llista no es 0 pero si es mes petita que “n”  entra, dins mante el boolean “trobat” en false. En la variable “seguent” guarda el ultim numero de la llista +1.

        Entra en el while que no surt fins que  “trobat”  es true, tot seguit entra en un for que recorre la llista. Dins tenim un if que compara si el numero de la variable  “seguent” dividit per “i” es 0  es mante en False suma +1 a “seguent” i acaba el if. Si pel contrari no dona 0 “trobat” es converteix en True.

        Aqui guarda la variable “seguent” en la llista i torna a cridar la funcio “busca()” de forma recursiva fins que es doni la condicio per acabar el programa """
        if (len(self.llista) == 0):
            self.llista.append(2)
            self.busca()

        elif (len(self.llista) < self.n):
            trobat = False
            seguent = self.llista[-1]+1
            while not trobat:
                for i in self.llista:
                    print(i)
                    if seguent%i == 0:
                        seguent += 1

                        print(self.llista)
                        print(seguent)
                        trobat = False
                        break

                    else:
                        trobat = True
            self.llista.append(seguent)
            self.busca()


if __name__ == '__main__':
    """Per altre banda al final del programa hi ha un if name = main que fa que quan executem el programa desde el mateix arxius executi i mostri tot l'indicat mentre que si la funcio es crida desde un altre nomes fara las operacions i no mostra res"""
    l = llista_primers(int(sys.argv[1]))
    print l.llista
