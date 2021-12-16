from time import sleep

# Mensaje de bievenida
print('\n------------------------------')
print('** Bienvenido a VatoCinemas **')
print('------------------------------\n')

# Defino mi diccionario
Cartelera={
    'Spiderman':{'Nombre': 'Spiderman', 'Dias': ["Lunes", "Miercoles", "Sabado", "Domingo"] , 'Tiempo': 120, 'Precio': 20},
    'Matrix':{'Nombre': 'Matrix', 'Dias': ["Lunes", "Martes", "Viernes"], 'Tiempo': 140, 'Precio': 17},
    'Olds':{'Nombre': 'Olds', 'Dias':["Lunes", "Miercoles", "Domingo"], 'Tiempo': 115, 'Precio' : 12}
}

# Editar mas adelante
Contraseña = ("a1b2")

# Mi menu de opciones
def Opciones():
    print('\n---------------------------------\nQue opcion desea elegir:\n#1 Ver Cartelera\n#2 Comprar tickets\n#3 Buscar pelicula\n#4 Editar (Admins Olny)\n#5 Salir\n---------------------------------')
    Ask = int(input('#'))

    # Llamar a la funcion deseada dependiendo de la opcion solicitada

    if Ask == 1:
        C.Mostrar()
    elif Ask == 2:
        C.Comprar()
    elif Ask == 3:
        C.Buscar()
    elif Ask == 4:
        C.Editar()
    elif Ask == 5:
        C.Salir()
    else:
        pass

def Cambiar():

    Pel = input(str(f'\nIngrese la pelicula que desea modificar {Cartelera.keys()}: '))
    while Pel not in Cartelera:
        Pel = input(str(f'\nIngrese un nombre valido {Cartelera.keys()}: '))
    
    Valor = input(str(f'Que valor desea cambiar {Cartelera[Pel].keys()}: '))
    while Valor not in Cartelera[Pel].keys():
        Valor = input(str(f'Ingrese un valor valido {Cartelera[Pel].keys()}: '))

    print(f'Cambio realizado por "{Cartelera[Pel][Valor]}"')

    if Valor == 'Nombre':
        Nuevo = input(str(f'Cual sera el nuevo valor de ({Cartelera[Pel][Valor]})?: '))
        Cambio = Cartelera[Pel][Valor] = Nuevo
        Cartelera[Nuevo] = Cartelera.pop(Pel)
    elif Valor == 'Tiempo' or Valor == 'Precio':
        Nuevo = int(input(f'Cual sera el nuevo valor de ({Cartelera[Pel][Valor]})?: '))
        Cambio = Cartelera[Pel][Valor] = Nuevo
    else:
        Nuevo = input(str(f'Cual sera el nuevo valor de ({Cartelera[Pel][Valor]})?: '))
        Cambio = Cartelera[Pel][Valor] = Nuevo

def Eliminar():
    Pel = input(str(f'\nIngrese la pelicula que desea borrar {Cartelera.keys()}: '))
    while Pel not in Cartelera:
        Pel = input(str(f'\nIngrese un nombre valido {Cartelera.keys()}: '))
    Cartelera.pop(Pel)


class Cinemas():

    # Defino init 
    def __init__(self):
        Nom = str(input('Tramite a nombre de: '))
        Cantidad = int(input('\n¿Cuantas personas entraran al cine?: '))

    # Defino la funcion Añadir
    def Mostrar(self):
        print('\n------------------------------------------')
        print('         ** C A R T E L E R A **  \n')
        for x in Cartelera:

            print('Pelicula:', Cartelera[x]['Nombre'])
            print('Dias:', Cartelera[x]['Dias'] )
            print('Tiempo', Cartelera[x]['Tiempo'], 'Minutos')
            print('Precio de la entrada', Cartelera[x]['Precio'], 'Dolares\n')
            print('------------------------------------------\n')
            sleep(1)
        
    def Comprar(self):
        NomPel = str(input(f'\nIngrese el nombre de la pelicula\nDispobible {Cartelera.keys()}\n'))
        while Comida not in Cartelera:
            Comida = str(input('Ha ingresado incorrectamente el nombre, vuelva a intentarlo: '))
            
        print(f'\nSu orden de {Comida}') 
        print('Se ha procesado exitosamente')
        print('Podra pagar con tarjeta o efectivo directamente con el motorizado.')

    def Buscar(self):
        print('\n---------------------------------------------------------')
        NCartelera = str(input('Ingrese el nombre del contacto que desea buscar: '))
        print('---------------------------------------------------------')
        # Hago un recorrido para que encuentre el contacto
        for x in Cartelera:
            if NCartelera in Cartelera[x]['Nombre']:
                print('\nInformacion encontrada de', Cartelera[x]['Nombre'])
                print('Dias:', Cartelera[x]['Dias'],'\nTiempo que dura:', Cartelera[x]['Tiempo'], 'minutos', '\nPrecio de la entrada:', Cartelera[x]['Precio'], '$')
                sleep(1)

    def Editar(self):
        ctr = str(input('Ingrese la contraseña: '))
        if ctr in Contraseña:
            ask = int(input('---------------------------\nQue accion desea realizar\n#1 Editar\n#2 Eliminar\n---------------------------\n'))
            if ask == 1:
                Cambiar()
            elif ask == 2:
                Eliminar()
            else:
                print('No existe esa opcion')
                pass
        else:
            print('Acceso denegado')

    def Salir(self):
        print('\nGracias por usar nuestros servicios \nVuelva pronto\n')
        exit()

# Acortar nombre de la clase
C = Cinemas()

# Un bucle infinito del sistema el cual solo terminara si se eleji la opcion salir
while True:
    Opciones()