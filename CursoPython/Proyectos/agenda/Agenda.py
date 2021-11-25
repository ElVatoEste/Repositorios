print('\nBienvenido a la agenda python\n')



Contactos={}

class Agenda():
    def __init__(self):
        Cantidad = int(input('Cuantos contactos desea agregar?: '))
        for x in range(Cantidad):
            nom = str(input('\n¿Cual es el nombre de su contacto?: '))
            numero = int(input('¿Cual es el telefono de su contacto?: '))
            email = str(input('¿Cual es el correo de su contacto?: '))
            Contactos.setdefault(nom, {'Nombre': nom, 'Numero':numero, 'Email':email})

    def Añadir(self):
        nom = str(input('\n¿Cual es el nombre de su contacto?: '))
        numero = int(input('¿Cual es el telefono de su contacto?: '))
        email = str(input('¿Cual es el correo de su contacto?: '))
        Contactos.setdefault(nom, {'Nombre': nom, 'Numero':numero, 'Email':email})
    
    def Mostrar(self):
        for x in Contactos:
            print('\n-------------------------------------')
            print(f'Nombre del contacto: {x}\nNumero:', Contactos[x]['Numero'],'\nCorreo Electronico:', Contactos[x]['Email'])
            print('-------------------------------------')
    def Buscar(self):
        NContacto = str(input('\nIngrese el nombre del contacto que desea buscar: '))
        for x in Contactos:
            if NContacto in Contactos[x]['Nombre']:
                print('\nInformacion del contacto:')
                print('Numero:', Contactos[x]['Numero'],'\nCorreo Electronico:', Contactos[x]['Email'])
    def Salir(self):
        print('\nGracias por usar nuestros servicios uwu\nVuelva pronto\n')
        exit()

A = Agenda()

while True:
    print('\n---------------------------------\nQue opcion desea elegir:\n#1 Añadir\n#2 Mostrar\n#3 Buscar\n#4 Editar\n#5 Salir\n---------------------------------')
    Ask = int(input('#'))

    if Ask == 1:
        A.Añadir()
    if Ask == 2:
        A.Mostrar()
    if Ask == 3:
        A.Buscar()
    if Ask == 5:
        A.Salir()