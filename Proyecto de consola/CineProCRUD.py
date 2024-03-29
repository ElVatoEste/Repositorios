# Sleep para mostrar lentamente
from time import sleep

# Mensaje de bievenida
print('\n------------------------------')
print('** Bienvenido a VatoCinemas **')
print('------------------------------\n')

# Servira para hacer la factura
Nom = str(input('Tramite a nombre de: '))
Cantidad = int(input('\n¿Cuantas personas entraran al cine?: '))

# Defino mi diccionario
Cartelera={
    'Spiderman':{'Nombre': 'Spiderman', 'Dia': "Domingo" , 'Tiempo': 120, 'Precio': 20},
    'Matrix':{'Nombre': 'Matrix', 'Dia': "Martes", 'Tiempo': 140, 'Precio': 17},
    'Olds':{'Nombre': 'Olds', 'Dia': "Miercoles",'Tiempo': 115, 'Precio' : 12}
}

# Contraseña de administrador
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

# Esta parte es tecnicamente el CRUD pero sin el ver porque ya esta como una opcion 
# del menu en la clase que se encuentra mas abajo

def Cambiar():

    Pel = input(str(f'\nIngrese la pelicula que desea modificar {Cartelera.keys()}: '))
    while Pel not in Cartelera:
        Pel = input(str(f'\nIngrese un nombre valido {Cartelera.keys()}: '))
    
    Valor = input(str(f'Que valor desea cambiar {Cartelera[Pel].keys()}: '))
    while Valor not in Cartelera[Pel].keys():
        Valor = input(str(f'Ingrese un valor valido {Cartelera[Pel].keys()}: '))

    # Subdivido la funcion cambiar ya que dentro de ella hay valores int y str, asi como el el caso del nombre
    # en el que tiene que haber tanto un cambio de llave como de valor
    if Valor == 'Nombre':
        Nuevo = input(str(f'Cual sera el nuevo valor de ({Cartelera[Pel][Valor]})?: '))
        Cambio = Cartelera[Pel][Valor] = Nuevo
        Cartelera[Nuevo] = Cartelera.pop(Pel)
    elif Valor == 'Tiempo' or Valor == 'Precio':
        Nuevo = int(input(f'Cual sera el nuevo valor de ({Cartelera[Pel][Valor]})?: '))
        Cambio = Cartelera[Pel][Valor] = Nuevo
    else:
        Nuevo = str(input(f'Cual sera el nuevo valor de ({Cartelera[Pel][Valor]})?: '))
        Cambio = Cartelera[Pel][Valor] = Nuevo

# Se elimina completamente toda la pelicula y su informacion, esto para no percudicar al programa
# mas adelante
def Eliminar():
    Pel = input(str(f'\nIngrese la pelicula que desea borrar {Cartelera.keys()}: '))
    while Pel not in Cartelera:
        Pel = input(str(f'\nIngrese un nombre valido {Cartelera.keys()}: '))
    Cartelera.pop(Pel)

# En el agregar solo se piden los valores que se necesitan y se agrega todo con un setdefault
# del crud sinceramente siento yo que es lo mas facil
def Agregar():
    Npel = str(input('Ingrese el nombre de la comida que desea agregar: '))
    Dpel = str(input(f'Cuando se exhibirá {Npel}?: '))
    Tpel = int(input('Cuantos minutos durara?: '))
    Ppel = int(input('Cuanto dolares costara la entrada: '))
    Cartelera.setdefault(Npel,{'Nombre':Npel, 'Dia':Dpel, 'Tiempo':Tpel, 'Precio':Ppel})


# Defino mi clase llamada cinemas

class Cinemas():

    # Defino init 
    def __init__(self, Nom, Cantidad):
       self.Nom = Nom
       self.Cantidad = Cantidad

    # Creo la funcion mostrar y le hago un poco de decoracion y formato utilizando el sleep para mostrar toda
    # la lista suavemente y no se vea muy feo y de golpe
    def Mostrar(self):
        print('\n------------------------------------------')
        print('         ** C A R T E L E R A **  \n')
        for x in Cartelera:

            print('Pelicula:', Cartelera[x]['Nombre'])
            print('Dia:', Cartelera[x]['Dia'] )
            print('Tiempo', Cartelera[x]['Tiempo'], 'Minutos')
            print('Precio de la entrada', Cartelera[x]['Precio'], 'Dolares\n')
            print('------------------------------------------\n')
            sleep(1)
        
    # En comprar se validan datos y se reutiliza el nombre y la cantidad de persona que pedimos al principio
    # Esto para llevar a cabo la factura, luego se sale del programa

    def Comprar(self):
        NomPel = str(input(f'\nIngrese el nombre de la pelicula\nDispobible {Cartelera.keys()}\n'))
        while NomPel not in Cartelera:
            NomPel = str(input('Ha ingresado incorrectamente el nombre, vuelva a intentarlo: '))

        PPrecio = Cartelera[NomPel]['Precio']
        Total = PPrecio * self.Cantidad 
        print('\nEspere un momento...')
        sleep(2)
        print(f'\nEstimad@ {self.Nom}, su compra se ha realizado exitosamente') 
        print('\n         ** R E C I B O **         ')
        print(f'factura a nombre de: {self.Nom}')
        print(f'Monto a pagar: {Total}$')
        print(f'Dia de la funcion', Cartelera[NomPel]['Dia'])
        print(f'Duracion:', Cartelera[NomPel]['Tiempo'], 'min')
        print('************************************\n')

        print('Muchas gracias por su compra, regrese pronto\n\n')
        exit()


    # Buscar consiste en realizar un reccorido por toda la lista, no importa si no te sabes el nombre completo
    # Solo al ingresar un caracter hace relacion con lo que encuentra, sin embargo imprime todo lo que lleve
    # esa cadena de caracter
    def Buscar(self):
        print('\n---------------------------------------------------------')
        NCartelera = str(input('Ingrese el nombre de la pelicula que desea buscar: '))
        print('---------------------------------------------------------')
       
        # Da una informacion detallada de lo encontrado y lentamente        
        for x in Cartelera:
            if NCartelera in Cartelera[x]['Nombre']:
                print('\nInformacion encontrada de', Cartelera[x]['Nombre'])
                print('Dia:', Cartelera[x]['Dia'],'\nTiempo que dura:', Cartelera[x]['Tiempo'], 'minutos', '\nPrecio de la entrada:', Cartelera[x]['Precio'], '$')
                sleep(1)

    # Editar es una funcion reservada para administradores, osea yo y la persona que logre ver el codigo
    # Al tener acceso lograra hacer el resto de las funciones del CRUD
    def Editar(self):
        ctr = str(input('Ingrese la contraseña: '))
        if ctr in Contraseña:
            ask = int(input('---------------------------\nQue accion desea realizar\n#1 Editar\n#2 Eliminar\n#3 Añadir\n---------------------------\n'))
            if ask == 1:
                Cambiar()
            elif ask == 2:
                Eliminar()
            elif ask == 3:
                Agregar()
            else:
                print('No existe esa opcion')
                pass
        else:
            print('Acceso denegado')

    # Funcion salir es simplemente salir del sistema xd
    def Salir(self):
        print('\nGracias por usar nuestros servicios \nVuelva pronto\n')
        exit()

# Al entroducir las variables dentro del parentesis me pertite reutilizarla en todo lo que va de la clase
C = Cinemas(Nom, Cantidad)

# Un bucle infinito del sistema el cual solo terminara si se eleji la opcion salir
while True:
    Opciones()