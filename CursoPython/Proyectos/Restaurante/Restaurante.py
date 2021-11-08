print('\n-------------------------------')
print('Bienvenido al sistema de propinas')
print('-------------------------------\n')
# Sistema en blucle

# Interruptor que definira si el blucle sigue o no
interruptor = True 

while interruptor:
    # ** inicio del bucle **

    # Listas puestas dentro del blucle para que se reincien
    Meseros = ['Juan', 'Pedro', 'Maria']

    # Se crea una copia de la lista para utilizar en la repartición
    MeserosCopia = Meseros.copy()
    Propina =[]
    # Lista Default para modificar mas adelante
    SubMeseros = []
    
    # Mostrar la lista desde un comienzo
    print(f'Meseros disponibles: {Meseros}\n')
    
    # Zona de ingreso 

    Cantidad = int(input('¿Cuantos meseros desean ingresar propinas?: '))
    while Cantidad > len(Meseros):
        print('\n** La Cantidad sobrepasa el limite de meseros registrados **')
        print(f'             Meseros dispobles actualmente {len(Meseros)}')
        print(f'     Meseros disponibles: {Meseros}\n')

        Cantidad = int(input('Ingrese nuevamente la cantidad: '))
  
     # Especificar Meseros
    for x in range(Cantidad):
        Nomb = str(input('Ingrese su nombre: '))

        #Chequea si esta en la lista
        while Nomb not in Meseros:
            print('\nEse mesero no esta registrado o ya fue ingresado')
            Nomb = str(input('Intente con otro nombre: '))

        # Utilizar la sublista junto con la propina emparejar con el metodo
        # dict(zip()) de los diccionarios

        SubMeseros.append(Nomb)
        # Eliminamos el mesero de la lista original para que no se repita
        Meseros.remove(Nomb)

        tips = float(input('Ingrese su propina: '))
        if tips >= 1000:
            print('\n-------------------------------')
            print('    Excelente aporte!')
            print('-------------------------------\n')
        else:
            print('\n-------------------------------')
            print('    Gracias por su aporte')
            print('-------------------------------\n')

        Propina.append(tips)
    
    Ask1 = str(input('¿Desea ver el registro de propinas del dia? y/n: '))
    # Preguntar si quiere ver la lista de las propinas con su mesero correspondiente
    while Ask1 != "y" and Ask1 != 'n':
        print('\n         Dato ingresado incorrecto')
        print('               y/n = Yes/No')
        Ask1 = input(str('\n¿Desea ver el registro de propinas del dia? y/n: '))
    if Ask1 == 'y':

        # Se establece un diccionario
        print('\nPropinas del dia: ')
        print(dict(zip(SubMeseros, Propina)))

    # Espacio para hacer calculos matematicos
    T_Propina = sum(Propina)
    Correspondiente = (T_Propina/len(MeserosCopia))
    

    print('\n---------------------------------------------------------------')
    print('El sistema esta basado en que cada mesero incluya la propina\nque gano en el dia y que todos reciban la misma parte por igual')
    print('---------------------------------------------------------------\n')

    print(f'{MeserosCopia} recibiran {Correspondiente:.2f} el dia de hoy')

    # Salida del servicio
    print('\n-----------------------------------------------')
    entrada = str(input('       ¿Desea seguir con el menu? y/n: '))
    # Solo entradas validas

    while entrada != "y" and entrada != 'n':
        print('\n         Dato ingresado incorrecto')
        print('               y/n = Yes/No')
        entrada = input(str('\n       ¿Desea seguir con el menu? y/n: '))

    if entrada == 'n':
        interruptor = False
print('-----------------------------------------------\n')
