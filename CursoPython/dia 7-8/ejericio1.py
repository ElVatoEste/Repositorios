'''
Realice un programa en Python que leer los datos (nombre, edad y sueldo) de n empleados
(máximo 10) e imprima los trabajadores con sueldo máximo y mínimo, así como la media de
los sueldos
'''

y_n = ['Y', 'N', 'n', 'y']


Trabajadores = {}

print('\n*****************************')
print('** Sistema de trabajadores **')
print('*****************************\n')

while True:

    Cantidad = int(input('¿Cuantos trabajadores desea agregar?: '))

    if Cantidad == 0:
        exit()

    while Cantidad > 10:
        print('\nLa cantidad solicitada excede el maximo disponible (10)')
        print('Ingrese nuevamente...')
        Cantidad = int(input('\n¿Cuantos trabajadores desea agregar?: '))
    
    for x in range(Cantidad):
        Nombre = str(input('\nIngrese el nombre del trabajador: '))
        Edad = int(input('Ingrese la edad del trabajadro: '))
        Salario = float(input(f'Ingrese el salario de {Nombre}: '))
        
        Trabajadores.setdefault(x, {'Nombre': Nombre, 'Edad' :Edad, 'Salario': Salario})
    
    Salida = str(input('¿Desea seguir agregando trabajadores? y/n: '))
    
    while Salida not in y_n:
        print(f'\n-----------------------------------------')
        print('           Caracter no valido')
        print('-----------------------------------------')

        for x in Trabajadores:
            print(f' {Trabajadores[x]["Nombre"]} tiene la edad de {Trabajadores[x]["Edad"]} años y un salario de {Trabajadores[x]["Salario"]} coordobas')
        