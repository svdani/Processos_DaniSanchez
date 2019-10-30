class EqPrimG:
    def __init__(self,s):
        self.a = " "
        self.b = " "
        self.operador = " "
        self.c = " "
        self.x = " "
        self.s_eq = s


    def calcula(self):
        try:
            self.result = " "
            self.l = self.s_eq.split()
            self.a = self.l[0]

            self.b = self.l[2]
            self.operador = self.l[1]
            self.c = self.l[4]
            self.a = self.a[:-1]
        except:
            return ("l'equacio no segueix el format: " + self.s_eq)


        print self.a,self.x,self.operador,self.b, "=",self.c
        try:
            if (self.operador == "+"):
                self.result = (float(self.c)-float(self.b))/float(self.a)

            elif (self.operador == "-"):
                self.result = (float(self.c)+float(self.b))/float(self.a)
            else:
                self.result = "Operador no valid: "+self.operador
            return self.result

        except:
            return ("l'equacio conte caracter no calculables: " + self.s_eq)
