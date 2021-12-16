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

# Una lista para definir los caracteres validos
from tkinter.constants import CHAR


y_n = ['Y', 'N', 'n', 'y']


# Bienvenida al sistema
print('\n********************************************************************')
print('** Bienvenido al Sistema de préstamos del Banco Industrial Python **')
print('********************************************************************\n')

#Explicacion del sistema del banco
print(f'En nuestro banco puedes solicitar prestamos para montar su negocion cobramos tan\nsolo con el 2% de interes [simple] mensualmente sobre el prestamo solicitado\nPara aplicar solo llena el siguiente formulario:')

# Si desea, se le pide sus datos, si no pues se cierra el sistema
Pedir = str(input('\nDesea aplicar para el prestamo? y/n: '))

#Validacion
while Pedir not in y_n:
    print('\n-----------------------------------------')
    print('           Caracter no valido')
    print('-----------------------------------------\n')
    Pedir = str(input('Desea aplicar para el prestamo? y/n: '))

# Mensaje de salida
if Pedir == 'n' or Pedir == 'N':
    print('\n**  Usted ha salido del sistema **')
    print('    !Que tenga un bonito dia!\n')

# Peticion de datos
else:
    print('\nIngrese su nombre completo: ')
    Nombre = str(input(''))

    print('\nIngrese su numero de cedula\nEjemplo: 001-260204-1234J')
    Cedula = str(input(''))

    while len(Cedula) != 16:
        print('\n                 Cedula invalida')
        print("    tienes que introducir 14 digitos validos")
        print('** Utilize - para separar la cadena de digitos **\n')
        Cedula = str(input(''))

    Ingresos = float(input('\nIngrese la cantidad de ingresos mensuales: '))

    if Ingresos >= 5000.00:
        print('\n                           ** Solicitud aceptada **                          ')

        print('\n-----------------------------------------------------------------------------')
        Prestamo = float(input('Ingrese la cantidad de dinero a solicitar para el prestamo: '))
        print('-----------------------------------------------------------------------------')
        Meses = int(input('¿Cuantas cuotas mensuales desea realiazar para completar su prestamo?: '))
        print('-----------------------------------------------------------------------------')

        Cuotas =  Prestamo/Meses
        Extra = Cuotas+(Cuotas*0.02)

        Total = (Extra)*Meses

        print('\nSu prestamo se ha procesado...')   
        print(f'\nPrestamo exitoso, el pago final sera de {Total} en cuotas de {Extra} por {Meses} meses')
        print('Gracias por su tiempo, gracias por confiar en B.I.P\nVuelva pronto\n')
    else:
        print('\nLo sentiento pero usted no cumple con los requisitos...')
        print('Gracias por su tiempo, gracias por confiar en B.I.P\nVuelva pronto\n')