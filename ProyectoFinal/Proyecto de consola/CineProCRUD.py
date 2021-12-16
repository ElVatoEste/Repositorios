from time import sleep

# Mensaje de bievenida
print('\n------------------------------')
print('** Bienvenido a VatoCinemas **')
print('------------------------------\n')

# Defino mi diccionario
Cartelera={
    'Spiderman':{'Nombre': 'Spiderman', 'Dias': ["Lunes", "Miercoles", "Sabado", "Domingo"] , 'Tiempo': 120}, 'Precio': 20,
    'Matrix':{'Nombre': 'Matrix', 'Dias': ["Lunes", "Martes", "Viernes"], 'Tiempo': 140}, 'Precio': 17,
    'Olds':{'Nombre': 'Olds', 'Dias':["Lunes", "Miercoles", "Domingo"], 'Tiempo': 115}, 'Precio' : 12
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

    Pel = input(str(f'\nIngrese el nombre del contacto que desea modificar {Cartelera.keys()}: '))
    while Pel not in Cartelera:
        Pel = input(str(f'\nIngrese un nombre valido {Cartelera.keys()}: '))
    
    Valor = input(str(f'Ingrese el valor que desea cambiar {Cartelera[Pel].keys()}: '))
    while Valor not in Cartelera[Pel].keys():
        Valor = input(str(f'Ingrese el valor que desea cambiar {Cartelera[Pel].keys()}: '))

    print(f'Cambio realizado por "{Cartelera[Pel][Valor]}"')


    if Valor == 'Nombre':
        Nuevo = input(str(f'Cual sera el nuevo valor de ({Cartelera[Pel][Valor]})?: '))
        Cambio = Cartelera[Pel][Valor] = Nuevo
        Cartelera[Nuevo] = Cartelera.pop(Pel)


class Cinemas():

    # Defino init 
    def __init__(self):
        Opciones()

    # Defino la funcion Añadir
    def Mostrar(self):
        for x in Cartelera:
            print('   ** C A R T E L E R A **  ')

            print(f'Pelicula: {Cartelera[x]}       ')
            print('Dias:', Cartelera[x]['Dias'] )
            print('Tiempo', Cartelera[x]['Tiempo'], 'Minutos')
            print('Precio de la entrada', Cartelera[x]['Precio'], '$')
            sleep(1)
        
    def Comprar(self):
        print('Hola')

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
            # Si el nombre o patron de caracteres no se encuentra, avisara que el contacto no se ha encontrado
            else:
                print("Contacto no encontrado")

    def Editar(self):
        ctr = str(input('Ingrese la contraseña'))
        if ctr in Contraseña:
            print('a')
        else:
            print('Acceso denegado')

    def Salir(self):
        print('\nGracias por usar nuestros servicios uwu\nVuelva pronto\n')
        exit()

# Acortar nombre de la clase
C = Cinemas()

# Un bucle infinito del sistema el cual solo terminara si se eleji la opcion salir
while True:
    Opciones()