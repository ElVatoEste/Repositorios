# Funcion Saludo

def saludo():
    print('Hola mundo')

saludo()

# Funcion suma

def suma(sum1, sum2):
    sum1 = int(input('Ingrese el primer valor: '))
    sum2 = int(input('Ingrese el segundo valor: '))
    Operacion = sum1 + sum2
    print (Operacion)

suma(1, 2)

def menu():
    while True:
        print('\n-----------------------------')
        print('-- OPC#1 -- SUMA DE VALORES --')
        print('-- OPC#2 -- RECORRIDO DE DIAS --')
        print('\n-----------------------------')
