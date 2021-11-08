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

    # Zona de ingreso 

    Cantidad = int(input('¿Cuantos meseros desean ingresar propinas?: '))
    while Cantidad > len(Meseros):
        print('\n** La Cantidad sobrepasa el limite de meseros registrados **')
        print(f'           Meseros dispobles actualmente {len(Meseros)}\n')
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

        tips = float(input('\nIngrese su propina: '))
        if tips >= 1000:
            print('Excelente aporte!\n')
        else:
            print('Gracias por su aporte\n')

        Propina.append(tips)
    print('Propinas del dia: ')
    # Se establece el diccionario para que cada mesero tenga su propina correspondiente
    Diccionario = dict(zip(SubMeseros, Propina))
    print = Diccionario





    # Salida del servicio
    print('--------------------------------------')
    entrada = str(input('Desea seguir con el menu? y/n: '))
    if entrada == "n":
        interruptor = False
        break
print('--------------------------------------\n')
