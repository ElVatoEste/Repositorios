'''
num = int(input('Ingrese un numero: '))

x = 1

while (x <= num):
    print(f'El recorrido es {x}')
    x = x+1

print('****** fin *******')
'''
# primer ejemplo arriba


Clave = int(input('\n Ingrese su contraseña: '))

while Clave != 123:
    print('Clave incorrecta')
    Clave = input('Ingrese su contraseña: ')

print('Bienvenido')