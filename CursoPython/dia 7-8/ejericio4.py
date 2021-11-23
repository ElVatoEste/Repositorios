'''
Un restaurante tiene la necesidad de presentar su menú de forma virtual por ende se necesita de un
programa el cual muestre en pantalla el menú del restaurante con sus precios y el tiempo a esperar,
cual solicite al cliente que platillo que le gustaría  degustar he imprimir en pantalla pedido exitoso
El desglose sería el siguiente: La opción pollo frito seguido del precio y del tiempo a esperar
'''


Menu = {
    1:{'Nombre': 'Pollo Frito', 'Precio': 150, 'Tiempo': 15},
    2:{'Nombre': 'Pizza', 'Precio': 220, 'Tiempo': 20},
    3:{'Nombre': 'Hamburgesa', 'Precio': 120, 'Tiempo': 10}
}

print('\n---------------------------------------------------')
print('         Bienvenido al restaurante el jefe         ')
print('---------------------------------------------------\n')

while True:

    Ask = int(input('Opciones del restaurante\n#1 Menu de comidas\n#2 Solicitar plato\n#3 Agregar platillo\n#4 Salir\n'))

    if Ask == 1:
        for x in Menu:
            print('\nNombre del plato:',Menu[x]['Nombre'], '\nPrecio del plato:',Menu[x]['Precio'], '\nEsta orden se prepara en',Menu[x]['Tiempo'], 'min\n')
    
    if Ask == 2:
        Comida = str(input())
        while Comida not in Menu:
            Comida = str(input('Comida inexistente o dato ingresado no es el mismo de la base de datos...\nEscriba especificamente el plato solicitado: '))
        print('Su orden de:', Menu[x][{Comida}])

    if Ask == 3:
        

    if Ask == 4:
        print('Gracias por visitarnos, regrese pronto')