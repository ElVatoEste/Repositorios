# testeo del while

# Listas ***
Meseros = ['Juan', 'Pedro', 'Maria']
Propina =[]

interruptor = True 

while interruptor:
# Zona de ingreso 
    Cantidad = int(input('¿Cuantos meseros desean ingresar la propina?: '))
    while Cantidad > len(Meseros):
        print('Cantidad sobrepasa el limite de meseros registrados')
        print(f'Meseros dispobles actualmente {len(Meseros)}')
        Cantidad = int(input('Ingrese nuevamente la cantidad: '))
  
     # Especificar Meseros
    for x in range(Cantidad):
        Nom = str(input('Ingrese su nombre: '))

        #Chequea si esta en la lista
        while Nom not in Meseros:
            print('Ese mesero no esta registrado')
            Nom = str(input('Ingrese nuevamente el nombre: '))
        Sueldo = float(input('Ingrese su salario: '))
        Propina.append(Sueldo)

        # Ubicar meseros
        i = Meseros.get(Nom)
        print(i)


    Diccionario = dict(zip(Meseros, Propina))
    print(Diccionario)




    # Salida del servicio
    print('--------------------------------------')
    entrada = str(input('Desea seguir con el menu? y/n: '))
    if entrada == "n":
        interruptor = False
        break
print('--------------------------------------')