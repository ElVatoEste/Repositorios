'''
Realice un programa en Python que leer los datos (nombre, edad y sueldo) de n empleados
(máximo 10) e imprima los trabajadores con sueldo máximo y mínimo, así como la media de
los sueldos
'''

y_n = ['Y', 'N', 'n', 'y']




print('\n*****************************')
print('** Sistema de trabajadores **')
print('*****************************\n')

while True:

    Trabajadores = {}
    Dinero = []

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
        
        Dinero.append(Salario)

        Trabajadores.setdefault(x, {'Nombre': Nombre, 'Edad' :Edad, 'Salario': Salario})
    
        for x in Trabajadores:
            print(f' {Trabajadores[x]["Nombre"]} tiene la edad de {Trabajadores[x]["Edad"]} años y un salario de {Trabajadores[x]["Salario"]} coordobas')
    
        Total = sum(Salario)
        
        

        print(f'La media es {Total/Cantidad:.2f} ')





    print('\n¿Desea volver a ingresar los datos de los trabajadores?')
    print('** Si desea continuar tiene que tomar en cuenta que los trabajadores ingresados se reiniciaran... **')
    print('En caso contrario el sistema de detendra')
    Salida = str(input('¿Desea continuar? y/n: '))

    
    while Salida not in y_n:
        print(f'\n-----------------------------------------')
        print('           Caracter no valido')
        print('-----------------------------------------')
    
    if Salida == 'N' or Salida == 'n':
        exit()