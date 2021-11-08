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
    Propina =[]

    # Lista Default para modificar mas adelante
    SubMeseros = ()

    # Zona de ingreso 

    Cantidad = int(input('¿Cuantos meseros desean ingresar propinas?: '))
    while Cantidad > len(Meseros):
        print('** La Cantidad sobrepasa el limite de meseros registrados **')
        print(f'Meseros dispobles actualmente {len(Meseros)}')
        Cantidad = int(input('Ingrese nuevamente la cantidad: '))
  
     # Especificar Meseros
    for x in range(Cantidad):
        Nomb = str(input('Ingrese su nombre: '))

        #Chequea si esta en la lista
        while Nomb not in Meseros:
            print('Ese mesero no esta registrado')
            Nomb = str(input('Ingrese nuevamente el nombre: '))

        # Utilizar la sublista junto con la propina emparejar con el metodo
        # dict(zip()) de los diccionarios

        SubMeseros.append(Nomb)

        tips = float(input('Ingrese su propina: '))
        if tips >= 1000:
            print('Excelente aporte!')
        else:
            print('Gracias por su aporte')

        Propina.append(tips)
    





    # Salida del servicio
    print('--------------------------------------')
    entrada = str(input('Desea seguir con el menu? y/n: '))
    if entrada == "n":
        interruptor = False
        break
print('--------------------------------------')