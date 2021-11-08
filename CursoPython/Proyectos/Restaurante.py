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
    for Meseseros in range(Cantidad):
        print(Meseros)
    # Especificar Meseros



    # Salida del servicio
    print('--------------------------------------')
    entrada = str(input('Desea seguir con el menu? y/n: '))
    if entrada == "n":
        interruptor = False
        break
print('--------------------------------------')