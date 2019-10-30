class EqPrimG:
    def __init__(self,s):
        self.a = " "
        self.b = " "
        self.operador = " "
        self.c = " "
        self.x = " "
        self.s_eq = s

    def calcula(self):
        print self.s_eq

    def extreuPart1(self):
        l = self.s_eq.split()
        a = l[0]
        x = a[-1]
        b = l[2]
        operador =l[1]
        c = l[4]

        a = a[:-1]
        print a,x,operador,b, "=",c

        if (operador == "+"):
            result = (float(c)-float(b))/float(a)


        if (operador == "-"):
            result = (float(c)+float(b))/float(a)

        print x,"=",result

eq = EqPrimG("20x - 70 = -30")
eq.extreuPart1()
