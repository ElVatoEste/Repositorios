'''
Un banco, desea que usted desarrolle un programa que permita a sus clientes poder
solicitar préstamos y que el cliente pueda saber cuánto será el pago total incluyendo
los intereses, deberá solicitar los siguientes datos:
Bienvenido al Sistema de préstamos del Banco Industrial Python.
Nombre completo:
Numero de cedula:
Ingresos mensuales:
Si el ingreso mensual es mayor o igual a 5000.00 córdobas entonces podrá aprobarse el
préstamo y darle la bienvenida a la consulta de los préstamos si no rechazar el préstamo y
agradecer por su interés al banco

'''


y_n = ['Y', 'N', 'n', 'y']

interes = 2

print('\n********************************************************************')
print('** Bienvenido al Sistema de préstamos del Banco Industrial Python **')
print('********************************************************************\n')

print(f'En nuestro banco puedes solicitar prestamos para montar su negocion cobramos tan\nsolo con el 2% de interes [simple] mensualmente sobre el prestamo solicitado\nPara aplicar solo llena el siguiente formulario:')

Pedir = str(input('\nDesea aplicar para el prestamo? y/n: '))

while Pedir not in y_n:
    print('\n-----------------------------------------')
    print('           Caracter no valido')
    print('-----------------------------------------\n')
    Pedir = str(input('Desea aplicar para el prestamo? y/n: '))

if Pedir == 'n' or Pedir == 'N':
    print('\n**  Usted ha salido del sistema **')
    print('    !Que tenga un bonito dia!\n')

print('\nIngrese su nombre completo: ')
Nombre = str(input(''))

print('\nIngrese su numero de cedula\nEjemplo: 001-260204-1234J')
Cedula = str(input(''))

while len(Cedula)!=16:
    print('\n                 Cedula invalida')
    print("    tienes que introducir 14 digitos validos")
    print('** Utilize - para separar la cadena de digitoa **\n')
    Cedula = str(input(''))

Ingresos = float(input('\nIngrese la cantidad de ingresos mensuales: '))

if Ingresos >= 5000.00:
    print('\n ** Solicitdud aceptada **')

    