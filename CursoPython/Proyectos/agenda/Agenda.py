
# Importo la libreria time para usar la funcion sleep
import time

# Bienvenida
print('\n-----------------------------------')
print('** Bienvenido a la agenda python **')
print('-----------------------------------\n')

# Defino mi diccionario
Contactos={}

# Mi menu de opciones
def Opciones():
    print('\n---------------------------------\nQue opcion desea elegir:\n#1 Añadir\n#2 Mostrar\n#3 Buscar\n#4 Editar\n#5 Salir\n---------------------------------')
    Ask = int(input('#'))

    # Llamar a la funcion deseada dependiendo de la opcion solicitada

    if Ask == 1:
        A.Añadir()
    elif Ask == 2:
        A.Mostrar()
    elif Ask == 3:
        A.Buscar()
    elif Ask == 4:
        A.Editar()
    elif Ask == 5:
        A.Salir()
    else:
        pass

# Creacion de la clase llamada Agenda

class Agenda():

    # Defino init 
    def __init__(self):
        Cantidad = int(input('Cuantos contactos desea agregar?: '))
        for x in range(Cantidad):
            nom = str(input('\n¿Cual es el nombre de su contacto?: '))
            numero = int(input('¿Cual es el telefono de su contacto?: '))
            email = str(input('¿Cual es el correo de su contacto?: '))
            Contactos.setdefault(nom, {'Nombre': nom, 'Numero':numero, 'Email':email})

    # Defino la funcion Añadir
    def Añadir(self):
        nom = str(input('\n¿Cual es el nombre de su contacto?: '))
        numero = int(input('¿Cual es el telefono de su contacto?: '))
        email = str(input('¿Cual es el correo de su contacto?: '))
        Contactos.setdefault(nom, {'Nombre': nom, 'Numero':numero, 'Email':email})
    
    # Defino la funcion Mostrar
    def Mostrar(self):
        for x in Contactos:
            print('\n-------------------------------------')
            print(f'Nombre del contacto: {x}\nNumero:', Contactos[x]['Numero'],'\nCorreo Electronico:', Contactos[x]['Email'])
            print('-------------------------------------')
            time.sleep(1)

    # Defino la funcion buscar
    def Buscar(self):
        print('\n---------------------------------------------------------')
        NContacto = str(input('Ingrese el nombre del contacto que desea buscar: '))
        print('---------------------------------------------------------')
        # Hago un recorrido para que encuentre el contacto
        for x in Contactos:
            if NContacto in Contactos[x]['Nombre']:
                print('\nInformacion del contacto de', Contactos[x]['Nombre'])
                print('Numero:', Contactos[x]['Numero'],'\nCorreo Electronico:', Contactos[x]['Email'])
                time.sleep(1)
            # Si el nombre o patron de caracteres no se encuentra, avisara que el contacto no se ha encontrado
            else:
                print("Contacto no encontrado")
    
    # Definir funcion Editar
    def Editar(self):
        if len(Contactos) == 0:
            print("Usted no tiene a nadie registrado")
            Opciones()
        
        # Muestra todos los contactos disponibles
        Cct = input(str(f'\nIngrese el nombre del contacto que desea modificar {Contactos.keys()}: '))
        while Cct not in Contactos:
            Cct = input(str(f'\nIngrese un nombre valido {Contactos.keys()}: '))
        
        # Muestra todos los valores disponibles
        Valor = input(str(f'Ingrese el valor que desea cambiar {Contactos[Cct].keys()}: '))
        while Valor not in Contactos[Cct].keys():
            Valor = input(str(f'Ingrese el valor que desea cambiar {Contactos[Cct].keys()}: '))

        print(f'Cambio realizado por "{Contactos[Cct][Valor]}"')

        # Al tener duplicado el nombre como llave y valor, tenia que ser mas preciso en los cambios
        # por lo que tenia que hacer acciones distintas en cada campo, ya sea por ser un int o un str
        if Valor == 'Nombre':
            Nuevo = input(str(f'Cual sera el nuevo valor de ({Contactos[Cct][Valor]})?: '))
            Cambio = Contactos[Cct][Valor] = Nuevo
            Contactos[Nuevo] = Contactos.pop(Cct)
        elif Valor == 'Numero':
            Nuevo = int(input(f'Cual sera el nuevo valor de ({Contactos[Cct][Valor]})?: '))
            Cambio = Contactos[Cct][Valor] = Nuevo
        else:
            Nuevo = input(str(f'Cual sera el nuevo valor de ({Contactos[Cct][Valor]})?: '))
            Cambio = Contactos[Cct][Valor] = Nuevo

    # Salida del sistema
    def Salir(self):
        print('\nGracias por usar nuestros servicios uwu\nVuelva pronto\n')
        exit()

# Acortar nombre de la clase
A = Agenda()

# Un bucle infinito del sistema el cual solo terminara si se eleji la opcion salir
while True:
    Opciones()