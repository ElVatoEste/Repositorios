'''
Realice un programa en Python que leer los datos (nombre, edad y sueldo) de n empleados
(máximo 10) e imprima los trabajadores con sueldo máximo y mínimo, así como la media de
los sueldos
'''
# Validador de opciones tipo si y no pero en ingles xd
y_n = ['Y', 'N', 'n', 'y']

# Mensaje de bienvenida
print('\n*****************************')
print('** Sistema de trabajadores **')
print('*****************************\n')


# Bucle infinito
while True:

    # Listas y diccionarios asignados y vacios para llenarlos mas adelante
    Trabajadores = {}
    Dinero = []
    Numeros = []

    # Preguntar cantidad de trabajadores para pedir los datos con la misma exactitud
    Cantidad = int(input('¿Cuantos trabajadores desea agregar?: '))

    # si pone el numero cero es que no quiere nada y se va
    if Cantidad == 0:
        exit()

    # El numero maximo es de 10
    while Cantidad > 10:
        print('\nLa cantidad solicitada excede el maximo disponible (10)')
        print('Ingrese nuevamente...')
        Cantidad = int(input('\n¿Cuantos trabajadores desea agregar?: '))
    
    # Se usa for para hacer un recorrido la cantidad de veces que el usuario haya escogido en el rango de 1 a 10
    for x in range(Cantidad):
        Nombre = str(input('\nIngrese el nombre del trabajador: '))
        Edad = int(input('Ingrese la edad del trabajadro: '))
        Salario = float(input(f'Ingrese el salario de {Nombre}: '))
        
        
        Numeros.append(Salario)
        Dinero.append(Salario)

        Trabajadores.setdefault(x, {'Nombre': Nombre, 'Edad' :Edad, 'Salario': Salario})
    
    print('\n')

    for x in Trabajadores:
            print(f'{Trabajadores[x]["Nombre"]} tiene la edad de {Trabajadores[x]["Edad"]} años y un salario de {Trabajadores[x]["Salario"]} coordobas')
    
    Total = sum(Dinero)


    # Nota del 13/12/21, no se porque hice esta barbaridad de codigo pero sirve para comprovar numero mayores
    # y menores, le recomendaria bajar rapido para no mariarse  

    # Resumido... Se asigna a la variable maxima y minima el salario que cumpla con esas caracteristicas, simplemente
    # se hace una copia del valor pero con otro nombre.
    if Cantidad == 2:

        if Numeros[0] > Numeros[1]:
            Maximo = Numeros[0]
        else:
            Maximo = Numeros[1]

        if Numeros[0] < Numeros[1]:
            Minimo = Numeros[0]
        else:
            Minimo = Numeros[1]


    if Cantidad == 3:

        if Numeros[0] > Numeros[1] and Numeros[0] > Numeros[2]:
            Maximo = Numeros[0]
        else:
            if Numeros[1] > Numeros[0] and Numeros[1] > Numeros[2]:
                Maximo = Numeros[1]
            else:
                if Numeros[2] > Numeros[0] and Numeros[2] > Numeros[1]:
                    Maximo = Numeros[2]
                else:
                    pass

        if Numeros[0] < Numeros[1] and Numeros[0] < Numeros[2]:
            Minimo = Numeros[0]
        else:
            if Numeros[1] < Numeros[0] and Numeros[1] < Numeros[2]:
                Minimo = Numeros[1]
            else:
                if Numeros[2] < Numeros[0] and Numeros[2] < Numeros[1]:
                    Minimo = Numeros[2]
                else:
                    pass

    if Cantidad == 4:

        if Numeros[0] > Numeros[1] and Numeros[0] > Numeros[2] and Numeros[0] > Numeros[3]:
            Maximo = Numeros[0]
        else:
            if Numeros[1] > Numeros[0] and Numeros[1] > Numeros[2] and Numeros[1] > Numeros[3]:
                Maximo = Numeros[1]
            else:
                if Numeros[2] > Numeros[0] and Numeros[2] > Numeros[1] and Numeros[2] > Numeros[3]:
                    Maximo = Numeros[2]
                else:
                    if Numeros[3] > Numeros[0] and Numeros[2] > Numeros[1] and Numeros[2] > Numeros[3]:
                        Maximo = Numeros[3]
                    else:
                        pass

        if Numeros[0] < Numeros[1] and Numeros[0] < Numeros[2] and Numeros[0] < Numeros[3]:
            Minimo = Numeros[0]
        else:
            if Numeros[1] < Numeros[0] and Numeros[1] < Numeros[2] and Numeros[1] < Numeros[3]:
                Minimo = Numeros[1]
            else:
                if Numeros[2] < Numeros[0] and Numeros[2] < Numeros[1] and Numeros[2] < Numeros[3]:
                    Minimo = Numeros[2]
                else:
                    if Numeros[3] < Numeros[0] and Numeros[2] < Numeros[1] and Numeros[2] < Numeros[3]:
                        Minimo = Numeros[3]
                    else:
                        pass

    if Cantidad == 5:

        if Numeros[0] > Numeros[1] and Numeros[0] > Numeros[2] and Numeros[0] > Numeros[3] and Numeros[0] > Numeros[4]:
            Maximo = Numeros[0]
        else:
            if Numeros[1] > Numeros[0] and Numeros[1] > Numeros[2] and Numeros[1] > Numeros[3] and Numeros[1] > Numeros[4]:
                Maximo = Numeros[1]
            else:
                if Numeros[2] > Numeros[0] and Numeros[2] > Numeros[1] and Numeros[2] > Numeros[3] and Numeros[2] > Numeros[4]:
                    Maximo = Numeros[2]
                else:
                    if Numeros[3] > Numeros[0] and Numeros[2] > Numeros[1] and Numeros[2] > Numeros[3] and Numeros[2] > Numeros[4]:
                        Maximo = Numeros[3]
                    else:
                        if Numeros[4] > Numeros[0] and Numeros[4] > Numeros[1] and Numeros[4] > Numeros[2] and Numeros[4] > Numeros[3]:
                            Maximo = Numeros[4]
                        else:
                            pass

        if Numeros[0] < Numeros[1] and Numeros[0] < Numeros[2] and Numeros[0] < Numeros[3] and Numeros[0] < Numeros[4]:
            Minimo = Numeros[0]
        else:
            if Numeros[1] < Numeros[0] and Numeros[1] < Numeros[2] and Numeros[1] < Numeros[3] and Numeros[1] < Numeros[4]:
                Minimo = Numeros[1]
            else:
                if Numeros[2] < Numeros[0] and Numeros[2] < Numeros[1] and Numeros[2] < Numeros[3] and Numeros[2] < Numeros[4]:
                    Minimo = Numeros[2]
                else:
                    if Numeros[3] < Numeros[0] and Numeros[2] < Numeros[1] and Numeros[2] < Numeros[3] and Numeros[2] < Numeros[4]:
                        Minimo = Numeros[3]
                    else:
                        if Numeros[4] < Numeros[0] and Numeros[4] < Numeros[1] and Numeros[4] < Numeros[2] and Numeros[4] < Numeros[3]:
                            Minimo = Numeros[4]
                        else:
                            pass

    if Cantidad == 6:

        if Numeros[0] > Numeros[1] and Numeros[0] > Numeros[2] and Numeros[0] > Numeros[3] and Numeros[0] > Numeros[4] and Numeros[0] > Numeros[5]:
            Maximo = Numeros[0]
        else:
            if Numeros[1] > Numeros[0] and Numeros[1] > Numeros[2] and Numeros[1] > Numeros[3] and Numeros[1] > Numeros[4] and Numeros[1] > Numeros[5]:
                Maximo = Numeros[1]
            else:
                if Numeros[2] > Numeros[0] and Numeros[2] > Numeros[1] and Numeros[2] > Numeros[3] and Numeros[2] > Numeros[4] and Numeros[2] > Numeros[5]:
                    Maximo = Numeros[2]
                else:
                    if Numeros[3] > Numeros[0] and Numeros[2] > Numeros[1] and Numeros[2] > Numeros[3] and Numeros[2] > Numeros[4] and Numeros[2] > Numeros[5]:
                        Maximo = Numeros[3]
                    else:
                        if Numeros[4] > Numeros[0] and Numeros[4] > Numeros[1] and Numeros[4] > Numeros[2] and Numeros[4] > Numeros[3] and Numeros[4] > Numeros[5]:
                            Maximo = Numeros[4]
                        else:
                            if Numeros[5] > Numeros[1] and Numeros[5] > Numeros[2] and Numeros[5] > Numeros[3] and Numeros[5] > Numeros[4] and Numeros[5] > Numeros[0]:
                                Maximo = Numeros[5]
                            else:
                                pass

        if Numeros[0] < Numeros[1] and Numeros[0] < Numeros[2] and Numeros[0] < Numeros[3] and Numeros[0] < Numeros[4] and Numeros[0] < Numeros[5]:
            Minimo = Numeros[0]
        else:
            if Numeros[1] < Numeros[0] and Numeros[1] < Numeros[2] and Numeros[1] < Numeros[3] and Numeros[1] < Numeros[4] and Numeros[1] < Numeros[5]:             
                Minimo = Numeros[1]
            else:
                if Numeros[2] < Numeros[0] and Numeros[2] < Numeros[1] and Numeros[2] < Numeros[3] and Numeros[2] < Numeros[4] and Numeros[2] < Numeros[5]:
                    Minimo = Numeros[2]
                else:
                    if Numeros[3] < Numeros[0] and Numeros[2] < Numeros[1] and Numeros[2] < Numeros[3] and Numeros[2] < Numeros[4] and Numeros[2] < Numeros[5]:
                        Minimo = Numeros[3]
                    else:
                        if Numeros[4] < Numeros[0] and Numeros[4] < Numeros[1] and Numeros[4] < Numeros[2] and Numeros[4] < Numeros[3] and Numeros[4] < Numeros[5]: 
                            Minimo = Numeros[4]
                        else:
                            if Numeros[5] < Numeros[1] and Numeros[5] < Numeros[2] and Numeros[5] < Numeros[3] and Numeros[5] < Numeros[4] and Numeros[5] < Numeros[0]:
                                Minimo = Numeros[5]
                            else:
                                pass

    if Cantidad == 7:    
        if Numeros[0] > Numeros[1] and Numeros[0] > Numeros[2] and Numeros[0] > Numeros[3] and Numeros[0] > Numeros[4] and Numeros[0] > Numeros[5] and Numeros[0] > Numeros[6]:
            Maximo = Numeros[0]
        else:
            if Numeros[1] > Numeros[0] and Numeros[1] > Numeros[2] and Numeros[1] > Numeros[3] and Numeros[1] > Numeros[4] and Numeros[1] > Numeros[5] and Numeros[1] > Numeros[6]:
                Maximo = Numeros[1]
            else:
                if Numeros[2] > Numeros[0] and Numeros[2] > Numeros[1] and Numeros[2] > Numeros[3] and Numeros[2] > Numeros[4] and Numeros[2] > Numeros[5] and Numeros[2] > Numeros[6]:
                    Maximo = Numeros[2]
                else:
                    if Numeros[3] > Numeros[0] and Numeros[2] > Numeros[1] and Numeros[2] > Numeros[3] and Numeros[2] > Numeros[4] and Numeros[2] > Numeros[5] and Numeros[2] > Numeros[6]:
                        Maximo = Numeros[3]
                    else:
                        if Numeros[4] > Numeros[0] and Numeros[4] > Numeros[1] and Numeros[4] > Numeros[2] and Numeros[4] > Numeros[3] and Numeros[4] > Numeros[5] and Numeros[4] > Numeros[6]:
                            Maximo = Numeros[4]
                        else:
                            if Numeros[5] > Numeros[1] and Numeros[5] > Numeros[2] and Numeros[5] > Numeros[3] and Numeros[5] > Numeros[4] and Numeros[5] > Numeros[0] and Numeros[5] > Numeros[6]:
                                Maximo = Numeros[5]
                            else:
                                if Numeros[6] > Numeros[1] and Numeros[6] > Numeros[2] and Numeros[6] > Numeros[3] and Numeros[6] > Numeros[4] and Numeros[6] > Numeros[5] and Numeros[6] > Numeros[0]:
                                    Maximo = Numeros[6]
                                else:
                                    pass

        if Numeros[0] < Numeros[1] and Numeros[0] < Numeros[2] and Numeros[0] < Numeros[3] and Numeros[0] < Numeros[4] and Numeros[0] < Numeros[5] and Numeros[0] < Numeros[6]:
            Minimo = Numeros[0]
        else:
            if Numeros[1] < Numeros[0] and Numeros[1] < Numeros[2] and Numeros[1] < Numeros[3] and Numeros[1] < Numeros[4] and Numeros[1] < Numeros[5] and Numeros[1] < Numeros[6]:
                Minimo = Numeros[1]
            else:
                if Numeros[2] < Numeros[0] and Numeros[2] < Numeros[1] and Numeros[2] < Numeros[3] and Numeros[2] < Numeros[4] and Numeros[2] < Numeros[5] and Numeros[2] < Numeros[6]:
                    Minimo = Numeros[2]
                else:
                    if Numeros[3] < Numeros[0] and Numeros[2] < Numeros[1] and Numeros[2] < Numeros[3] and Numeros[2] < Numeros[4] and Numeros[2] < Numeros[5] and Numeros[2] < Numeros[6]:
                        Minimo = Numeros[3]
                    else:
                        if Numeros[4] < Numeros[0] and Numeros[4] < Numeros[1] and Numeros[4] < Numeros[2] and Numeros[4] < Numeros[3] and Numeros[4] < Numeros[5] and Numeros[4] < Numeros[6]:
                            Minimo = Numeros[4]
                        else:
                            if Numeros[5] < Numeros[1] and Numeros[5] < Numeros[2] and Numeros[5] < Numeros[3] and Numeros[5] < Numeros[4] and Numeros[5] < Numeros[0] and Numeros[5] < Numeros[6]:
                                Minimo = Numeros[5]
                            else:
                                if Numeros[6] < Numeros[1] and Numeros[6] < Numeros[2] and Numeros[6] < Numeros[3] and Numeros[6] < Numeros[4] and Numeros[6] < Numeros[5] and Numeros[6] < Numeros[0]:
                                    Minimo = Numeros[6]
                                else:
                                    pass


    if Cantidad == 8:    
        if Numeros[0] > Numeros[1] and Numeros[0] > Numeros[2] and Numeros[0] > Numeros[3] and Numeros[0] > Numeros[4] and Numeros[0] > Numeros[5] and Numeros[0] > Numeros[6] and Numeros[0] > Numeros[7]:                
            Maximo = Numeros[0]
        else:
            if Numeros[1] > Numeros[0] and Numeros[1] > Numeros[2] and Numeros[1] > Numeros[3] and Numeros[1] > Numeros[4] and Numeros[1] > Numeros[5] and Numeros[1] > Numeros[6] and Numeros[1] > Numeros[7]:
                Maximo = Numeros[1]
            else:
                if Numeros[2] > Numeros[0] and Numeros[2] > Numeros[1] and Numeros[2] > Numeros[3] and Numeros[2] > Numeros[4] and Numeros[2] > Numeros[5] and Numeros[2] > Numeros[6] and Numeros[2] > Numeros[7]:
                    Maximo = Numeros[2]
                else:
                    if Numeros[3] > Numeros[0] and Numeros[2] > Numeros[1] and Numeros[2] > Numeros[3] and Numeros[2] > Numeros[4] and Numeros[2] > Numeros[5] and Numeros[2] > Numeros[6] and Numeros[2] > Numeros[7]:
                        Maximo = Numeros[3]
                    else:
                        if Numeros[4] > Numeros[0] and Numeros[4] > Numeros[1] and Numeros[4] > Numeros[2] and Numeros[4] > Numeros[3] and Numeros[4] > Numeros[5] and Numeros[4] > Numeros[6] and Numeros[4] > Numeros[7]:
                            Maximo = Numeros[4]
                        else:
                            if Numeros[5] > Numeros[1] and Numeros[5] > Numeros[2] and Numeros[5] > Numeros[3] and Numeros[5] > Numeros[4] and Numeros[5] > Numeros[0] and Numeros[5] > Numeros[6] and Numeros[5] > Numeros[7]:
                                Maximo = Numeros[5]
                            else:
                                if Numeros[6] > Numeros[1] and Numeros[6] > Numeros[2] and Numeros[6] > Numeros[3] and Numeros[6] > Numeros[4] and Numeros[6] > Numeros[5] and Numeros[6] > Numeros[0] and Numeros[6] > Numeros[7]:
                                    Maximo = Numeros[6]
                                else:
                                    if Numeros[7] > Numeros[1] and Numeros[7] > Numeros[2] and Numeros[7] > Numeros[3] and Numeros[7] > Numeros[4] and Numeros[7] > Numeros[5] and Numeros[7] > Numeros[6] and Numeros[7] > Numeros[0]:
                                        Maximo = Numeros[7]
                                    else:
                                        pass

        if Numeros[0] < Numeros[1] and Numeros[0] < Numeros[2] and Numeros[0] < Numeros[3] and Numeros[0] < Numeros[4] and Numeros[0] < Numeros[5] and Numeros[0] < Numeros[6] and Numeros[0] < Numeros[7]:
            Minimo = Numeros[0]
        else:
            if Numeros[1] < Numeros[0] and Numeros[1] < Numeros[2] and Numeros[1] < Numeros[3] and Numeros[1] < Numeros[4] and Numeros[1] < Numeros[5] and Numeros[1] < Numeros[6] and Numeros[1] < Numeros[7]:
                Minimo = Numeros[1]
            else:
                if Numeros[2] < Numeros[0] and Numeros[2] < Numeros[1] and Numeros[2] < Numeros[3] and Numeros[2] < Numeros[4] and Numeros[2] < Numeros[5] and Numeros[2] < Numeros[6] and Numeros[2] < Numeros[7]:
                    Minimo = Numeros[2]
                else:
                    if Numeros[3] < Numeros[0] and Numeros[2] < Numeros[1] and Numeros[2] < Numeros[3] and Numeros[2] < Numeros[4] and Numeros[2] < Numeros[5] and Numeros[2] < Numeros[6] and Numeros[2] < Numeros[7]:
                        Minimo = Numeros[3]
                    else:
                        if Numeros[4] < Numeros[0] and Numeros[4] < Numeros[1] and Numeros[4] < Numeros[2] and Numeros[4] < Numeros[3] and Numeros[4] < Numeros[5] and Numeros[4] < Numeros[6] and Numeros[4] < Numeros[7]:
                            Minimo = Numeros[4]
                        else:
                            if Numeros[5] < Numeros[1] and Numeros[5] < Numeros[2] and Numeros[5] < Numeros[3] and Numeros[5] < Numeros[4] and Numeros[5] < Numeros[0] and Numeros[5] < Numeros[6] and Numeros[5] < Numeros[7]:
                                Minimo = Numeros[5]
                            else:
                                if Numeros[6] < Numeros[1] and Numeros[6] < Numeros[2] and Numeros[6] < Numeros[3] and Numeros[6] < Numeros[4] and Numeros[6] < Numeros[5] and Numeros[6] < Numeros[0] and Numeros[6] < Numeros[7]:
                                    Minimo = Numeros[6]
                                else:
                                    if Numeros[7] < Numeros[1] and Numeros[7] < Numeros[2] and Numeros[7] < Numeros[3] and Numeros[7] < Numeros[4] and Numeros[7] < Numeros[5] and Numeros[7] < Numeros[6] and Numeros[7] < Numeros[0]:
                                        Minimo = Numeros[7]
                                    else:
                                        pass

    if Cantidad == 9:    
        if Numeros[0] > Numeros[1] and Numeros[0] > Numeros[2] and Numeros[0] > Numeros[3] and Numeros[0] > Numeros[4] and Numeros[0] > Numeros[5] and Numeros[0] > Numeros[6] and Numeros[0] > Numeros[7] and Numeros[0] > Numeros[8]:
            Maximo = Numeros[0]
        else:
            if Numeros[1] > Numeros[0] and Numeros[1] > Numeros[2] and Numeros[1] > Numeros[3] and Numeros[1] > Numeros[4] and Numeros[1] > Numeros[5] and Numeros[1] > Numeros[6] and Numeros[1] > Numeros[7] and Numeros[1] > Numeros[8]:
                Maximo = Numeros[1]
            else:
                if Numeros[2] > Numeros[0] and Numeros[2] > Numeros[1] and Numeros[2] > Numeros[3] and Numeros[2] > Numeros[4] and Numeros[2] > Numeros[5] and Numeros[2] > Numeros[6] and Numeros[2] > Numeros[7] and Numeros[2] > Numeros[8]:
                    Maximo = Numeros[2]
                else:
                    if Numeros[3] > Numeros[0] and Numeros[2] > Numeros[1] and Numeros[2] > Numeros[3] and Numeros[2] > Numeros[4] and Numeros[2] > Numeros[5] and Numeros[2] > Numeros[6] and Numeros[2] > Numeros[7] and Numeros[2] > Numeros[8]:
                        Maximo = Numeros[3]
                    else:
                        if Numeros[4] > Numeros[0] and Numeros[4] > Numeros[1] and Numeros[4] > Numeros[2] and Numeros[4] > Numeros[3] and Numeros[4] > Numeros[5] and Numeros[4] > Numeros[6] and Numeros[4] > Numeros[7] and Numeros[4] > Numeros[8]:
                            Maximo = Numeros[4]
                            if Numeros[5] > Numeros[1] and Numeros[5] > Numeros[2] and Numeros[5] > Numeros[3] and Numeros[5] > Numeros[4] and Numeros[5] > Numeros[0] and Numeros[5] > Numeros[6] and Numeros[5] > Numeros[7] and Numeros[5] > Numeros[8]:
                                Maximo = Numeros[5]
                            else:
                                if Numeros[6] > Numeros[1] and Numeros[6] > Numeros[2] and Numeros[6] > Numeros[3] and Numeros[6] > Numeros[4] and Numeros[6] > Numeros[5] and Numeros[6] > Numeros[0] and Numeros[6] > Numeros[7] and Numeros[6] > Numeros[8]:
                                    Maximo = Numeros[6]
                                else:
                                    if Numeros[7] > Numeros[1] and Numeros[7] > Numeros[2] and Numeros[7] > Numeros[3] and Numeros[7] > Numeros[4] and Numeros[7] > Numeros[5] and Numeros[7] > Numeros[6] and Numeros[7] > Numeros[0] and Numeros[7] > Numeros[8]:
                                        Maximo = Numeros[7]
                                    else:
                                        if Numeros[8] > Numeros[1] and Numeros[8] > Numeros[2] and Numeros[8] > Numeros[3] and Numeros[8] > Numeros[4] and Numeros[8] > Numeros[5] and Numeros[8] > Numeros[6] and Numeros[8] > Numeros[0] and Numeros[8] > Numeros[0]:
                                            Maximo = Numeros[8]
                                        else:
                                            pass

        if Numeros[0] < Numeros[1] and Numeros[0] < Numeros[2] and Numeros[0] < Numeros[3] and Numeros[0] < Numeros[4] and Numeros[0] < Numeros[5] and Numeros[0] < Numeros[6] and Numeros[0] < Numeros[7] and Numeros[0] < Numeros[8]:
            Minimo = Numeros[0]
        else:
            if Numeros[1] < Numeros[0] and Numeros[1] < Numeros[2] and Numeros[1] < Numeros[3] and Numeros[1] < Numeros[4] and Numeros[1] < Numeros[5] and Numeros[1] < Numeros[6] and Numeros[1] < Numeros[7] and Numeros[1] < Numeros[8]:
                Minimo = Numeros[1]
            else:
                if Numeros[2] < Numeros[0] and Numeros[2] < Numeros[1] and Numeros[2] < Numeros[3] and Numeros[2] < Numeros[4] and Numeros[2] < Numeros[5] and Numeros[2] < Numeros[6] and Numeros[2] < Numeros[7] and Numeros[2] < Numeros[8]:
                    Minimo = Numeros[2]
                else:
                    if Numeros[3] < Numeros[0] and Numeros[2] < Numeros[1] and Numeros[2] < Numeros[3] and Numeros[2] < Numeros[4] and Numeros[2] < Numeros[5] and Numeros[2] < Numeros[6] and Numeros[2] < Numeros[7] and Numeros[2] < Numeros[8]:
                        Minimo = Numeros[3]
                    else:
                        if Numeros[4] < Numeros[0] and Numeros[4] < Numeros[1] and Numeros[4] < Numeros[2] and Numeros[4] < Numeros[3] and Numeros[4] < Numeros[5] and Numeros[4] < Numeros[6] and Numeros[4] < Numeros[7] and Numeros[4] < Numeros[8]:
                            Minimo = Numeros[4]
                        else:
                            if Numeros[5] < Numeros[1] and Numeros[5] < Numeros[2] and Numeros[5] < Numeros[3] and Numeros[5] < Numeros[4] and Numeros[5] < Numeros[0] and Numeros[5] < Numeros[6] and Numeros[5] < Numeros[7] and Numeros[5] < Numeros[8]:
                                Minimo = Numeros[5]
                            else:
                                if Numeros[6] < Numeros[1] and Numeros[6] < Numeros[2] and Numeros[6] < Numeros[3] and Numeros[6] < Numeros[4] and Numeros[6] < Numeros[5] and Numeros[6] < Numeros[0] and Numeros[6] < Numeros[7] and Numeros[6] < Numeros[8]:
                                    Minimo = Numeros[6]
                                else:
                                    if Numeros[7] < Numeros[1] and Numeros[7] < Numeros[2] and Numeros[7] < Numeros[3] and Numeros[7] < Numeros[4] and Numeros[7] < Numeros[5] and Numeros[7] < Numeros[6] and Numeros[7] < Numeros[0] and Numeros[7] < Numeros[8]:
                                        Minimo = Numeros[7]
                                    else:
                                        if Numeros[8] < Numeros[1] and Numeros[8] < Numeros[2] and Numeros[8] < Numeros[3] and Numeros[8] < Numeros[4] and Numeros[8] < Numeros[5] and Numeros[8] < Numeros[6] and Numeros[8] < Numeros[0] and Numeros[8] < Numeros[0]:
                                            Minimo = Numeros[8]
                                        else:
                                            pass          

    if Cantidad == 10:    
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
                if Numeros[2] < Numeros[0] and Numeros[2] < Numeros[1] and Numeros[2] < Numeros[3] and Numeros[2] < Numeros[4] and Numeros[2] < Numeros[5] and Numeros[2] < Numeros[6] and Numeros[2] < Numeros[7] and Numeros[2] < Numeros[8] and Numeros[2] < Numeros[9]:
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


    # Para que muestre los maximo y minimos si hay mas dos o más salarios
    if Cantidad > 1:
        print('\n--------------------------------------')
        print(f'La media es {Total/Cantidad:.2f} ')
        print('--------------------------------------')
        print(f'El salario maximo es {Maximo}')
        print('--------------------------------------')
        print(f'El salario minimo es {Minimo}')
        print('--------------------------------------')


    # esto se explica solo...
    print('\n¿Desea volver a ingresar los datos de los trabajadores?')
    print('** Si desea continuar tiene que tomar en cuenta que los trabajadores ingresados se reiniciaran... **')
    print('En caso contrario el sistema de detendra')
    

    # Salida del sistema.
    
    Salida = str(input('¿Desea continuar? y/n: '))

    
    while Salida not in y_n:
        print(f'\n-----------------------------------------')
        print('           Caracter no valido')
        print('-----------------------------------------')
        Salida = str(input('¿Desea continuar? y/n'))
    
    if Salida == 'N' or Salida == 'n':
        print('\nGracias por usar nuestro sistema\n')
        exit()