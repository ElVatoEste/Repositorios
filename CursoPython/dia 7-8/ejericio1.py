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
    Dinero = float([])
    Numeros = float([])

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
        
    if Numeros[0] > Numeros[1] and Numeros[0] > Numeros[2] and Numeros[0] > Numeros[3] and Numeros[0] > Numeros[4] and Numeros[0] > Numeros[5] and Numeros[0] > Numeros[6] and Numeros[0] > Numeros[7] and Numeros[0] > Numeros[8] and Numeros[0] > Numeros[9]:
        Maximo = Numeros[0]
    else:
        if Numeros[1] > Numeros[0] and Numeros[1] > Numeros[2] and Numeros[1] > Numeros[3] and Numeros[1] > Numeros[4] and Numeros[1] > Numeros[5] and Numeros[1] > Numeros[6] and Numeros[1] > Numeros[7] and Numeros[1] > Numeros[8] and Numeros[1] > Numeros[9]:
            Maximo = Numeros[1]
        else:
            if Numeros[2] > Numeros[0] and Numeros[2] > Numeros[1] and Numeros[2] > Numeros[3] and Numeros[2] > Numeros[4] and Numeros[2] > Numeros[5] and Numeros[2] > Numeros[6] and Numeros[2] > Numeros[7] and Numeros[2] > Numeros[8] and Numeros[2] > Numeros[9]:
                Maximo = Numeros[2]
            else:
                if Numeros[3] > Numeros[0] and Numeros[2] > Numeros[1] and Numeros[2] > Numeros[3] and Numeros[2] > Numeros[4] and Numeros[2] > Numeros[5] and Numeros[2] > Numeros[6] and Numeros[2] > Numeros[7] and Numeros[2] > Numeros[8] and Numeros[2] > Numeros[9]:
                    Maximo = Numeros[3]
                else:
                    if Numeros[4] > Numeros[0] and Numeros[4] > Numeros[1] and Numeros[4] > Numeros[2] and Numeros[4] > Numeros[3] and Numeros[4] > Numeros[5] and Numeros[4] > Numeros[6] and Numeros[4] > Numeros[7] and Numeros[4] > Numeros[8] and Numeros[4] > Numeros[9]:
                        Maximo = Numeros[4]
                    else:
                        if Numeros[5] > Numeros[1] and Numeros[5] > Numeros[2] and Numeros[5] > Numeros[3] and Numeros[5] > Numeros[4] and Numeros[5] > Numeros[0] and Numeros[5] > Numeros[6] and Numeros[5] > Numeros[7] and Numeros[5] > Numeros[8] and Numeros[5] > Numeros[9]:
                            Maximo = Numeros[5]
                        else:
                            if Numeros[6] > Numeros[1] and Numeros[6] > Numeros[2] and Numeros[6] > Numeros[3] and Numeros[6] > Numeros[4] and Numeros[6] > Numeros[5] and Numeros[6] > Numeros[0] and Numeros[6] > Numeros[7] and Numeros[6] > Numeros[8] and Numeros[6] > Numeros[9]:
                                Maximo = Numeros[6]
                            else:
                                if Numeros[7] > Numeros[1] and Numeros[7] > Numeros[2] and Numeros[7] > Numeros[3] and Numeros[7] > Numeros[4] and Numeros[7] > Numeros[5] and Numeros[7] > Numeros[6] and Numeros[7] > Numeros[0] and Numeros[7] > Numeros[8] and Numeros[7] > Numeros[9]:
                                    Maximo = Numeros[7]
                                else:
                                    if Numeros[8] > Numeros[1] and Numeros[8] > Numeros[2] and Numeros[8] > Numeros[3] and Numeros[8] > Numeros[4] and Numeros[8] > Numeros[5] and Numeros[8] > Numeros[6] and Numeros[8] > Numeros[0] and Numeros[8] > Numeros[0] and Numeros[8] > Numeros[9]:
                                        Maximo = Numeros[8]
                                    else:
                                        if Numeros[9] > Numeros[1] and Numeros[9] > Numeros[2] and Numeros[9] > Numeros[3] and Numeros[9] > Numeros[4] and Numeros[9] > Numeros[5] and Numeros[9] > Numeros[6] and Numeros[9] > Numeros[0] and Numeros[9] > Numeros[8] and Numeros[9] > Numeros[0]:
                                            Maximo = Numeros[9]
                                        else: 
                                            pass

    if Numeros[0] < Numeros[1] and Numeros[0] < Numeros[2] and Numeros[0] < Numeros[3] and Numeros[0] < Numeros[4] and Numeros[0] < Numeros[5] and Numeros[0] < Numeros[6] and Numeros[0] < Numeros[7] and Numeros[0] < Numeros[8] and Numeros[0] < Numeros[9]:
        Minimo = Numeros[0]
    else:
        if Numeros[1] < Numeros[0] and Numeros[1] < Numeros[2] and Numeros[1] < Numeros[3] and Numeros[1] < Numeros[4] and Numeros[1] < Numeros[5] and Numeros[1] < Numeros[6] and Numeros[1] < Numeros[7] and Numeros[1] < Numeros[8] and Numeros[1] < Numeros[9]:
            Minimo = Numeros[1]
        else:
            if Numeros[2] < Numeros[0] and Numeros[2] < Numeros[1] and Numeros[2] <<Numeros[3] and Numeros[2] < Numeros[4] and Numeros[2] < Numeros[5] and Numeros[2] < Numeros[6] and Numeros[2] < Numeros[7] and Numeros[2] < Numeros[8] and Numeros[2] < Numeros[9]:
                Minimo = Numeros[2]
            else:
                if Numeros[3] < Numeros[0] and Numeros[2] < Numeros[1] and Numeros[2] < Numeros[3] and Numeros[2] < Numeros[4] and Numeros[2] < Numeros[5] and Numeros[2] < Numeros[6] and Numeros[2] < Numeros[7] and Numeros[2] < Numeros[8] and Numeros[2] < Numeros[9]:
                    Minimo = Numeros[3]
                else:
                    if Numeros[4] < Numeros[0] and Numeros[4] < Numeros[1] and Numeros[4] < Numeros[2] and Numeros[4] < Numeros[3] and Numeros[4] < Numeros[5] and Numeros[4] < Numeros[6] and Numeros[4] < Numeros[7] and Numeros[4] < Numeros[8] and Numeros[4] < Numeros[9]:
                        Minimo = Numeros[4]
                    else:
                        if Numeros[5] < Numeros[1] and Numeros[5] < Numeros[2] and Numeros[5] < Numeros[3] and Numeros[5] < Numeros[4] and Numeros[5] < Numeros[0] and Numeros[5] < Numeros[6] and Numeros[5] < Numeros[7] and Numeros[5] < Numeros[8] and Numeros[5] < Numeros[9]:
                            Minimo = Numeros[5]
                        else:
                            if Numeros[6] < Numeros[1] and Numeros[6] < Numeros[2] and Numeros[6] < Numeros[3] and Numeros[6] < Numeros[4] and Numeros[6] < Numeros[5] and Numeros[6] < Numeros[0] and Numeros[6] < Numeros[7] and Numeros[6] < Numeros[8] and Numeros[6] < Numeros[9]:
                                Minimo = Numeros[6]
                            else:
                                if Numeros[7] < Numeros[1] and Numeros[7] < Numeros[2] and Numeros[7] < Numeros[3] and Numeros[7] < Numeros[4] and Numeros[7] < Numeros[5] and Numeros[7] < Numeros[6] and Numeros[7] < Numeros[0] and Numeros[7] < Numeros[8] and Numeros[7] < Numeros[9]:
                                    Minimo = Numeros[7]
                                else:
                                    if Numeros[8] < Numeros[1] and Numeros[8] < Numeros[2] and Numeros[8] < Numeros[3] and Numeros[8] < Numeros[4] and Numeros[8] < Numeros[5] and Numeros[8] < Numeros[6] and Numeros[8] < Numeros[0] and Numeros[8] < Numeros[0] and Numeros[8] < Numeros[9]:
                                        Minimo = Numeros[8]
                                    else:
                                        if Numeros[9] < Numeros[1] and Numeros[9] < Numeros[2] and Numeros[9] < Numeros[3] and Numeros[9] < Numeros[4] and Numeros[9] < Numeros[5] and Numeros[9] < Numeros[6] and Numeros[9] < Numeros[0] and Numeros[9] < Numeros[8] and Numeros[9] < Numeros[0]:
                                            Minimo = Numeros[9]
                                        else:
                                            pass          

    print(f'La media es {Total/Cantidad:.2f} ')
    print(f'El salario maximo es {Maximo}')
    print(f'El salario maximo es {Maximo}')
    


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