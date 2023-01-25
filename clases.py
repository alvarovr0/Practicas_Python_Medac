class operaciones:

    numero1=10
    numero2=20

    def sumar(self):

        suma=self.numero1+self.numero2
        print("La suma es: ", suma)

    def __init__(self,a,b):
        self.numero1=a
        self.numero2=b
        
    def __str__(self):

        cadena="El objeto es: " + str(self.numero1) + " y " + str(self.numero2)
        return cadena

    def __add__(self, objeto2):
        suma= self.numero1 + objeto2.numero1
        return suma

    def restar(self):
        resta=self.numero1-self.numero2
        print("La resta es: ", resta)

    def mul(self):
        mult=self.numero1*self.numero2
        print("La multiplicacion es: ", mult)

oper=operaciones(3,4)

oper2=operaciones(5,4)

print(oper+oper2)

print(oper)
