print('\nBienvenido a la caluladora python\n')


class Calculadora():
    def __init__(self):
        self.primero = int(input('Ingrese el primer numero: '))
        self.segundo = int(input('Ingrese el segundo numero: '))
    
    def Suma(self):
        suma = self.primero + self.segundo
        print(f'\nEl resultado de la suma es: {suma}')
    
    def Resta(self):
        resta = self.primero - self.segundo
        print(f'\nEl resultado de la resta es: {resta}')

    def Multi(self):
        multi = self.primero*self.segundo
        print(f'\nEl resultado de la multiplicacion es: {multi}')
        
    def Divi(self):
        divi = self.primero/self.segundo
        print(f'\nEl resultado de la division es : {divi}')

C = Calculadora()

while True:
    print('\nQue opcion desea elegir:\n#1 Suma\n#2 Resta\n#3 Multiplicación\n#4 Division')
    Ask = int(input())

    if Ask == 1:
        C.Suma()
    if Ask == 2:
        C.Resta()
    if Ask == 3:
        C.Multi()
    if Ask == 4:
        C.Divi()