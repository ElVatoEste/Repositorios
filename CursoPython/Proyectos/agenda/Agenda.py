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
        Telefono = int(input('¿Cual es el telefono de su contacto?: '))
        email = str(input('¿Cual es el correo de su contacto?: '))
        Contactos.setdefault(nom, {'Nombre': nom, 'Telefono':Telefono, 'Email':email})
    
    def Mostrar(self):
        for x in Contactos:
            print('\n')
            print(f'Nombre del contacto: {x}\nNumero:', Contactos[x]['Numero'],'\nCorreo Electronico:', Contactos[x]['Email'])

    def Buscar(self):
        NContacto = str(input('Ingrese el nombre del contacto que desea buscar'))
        for NContacto in Contactos:
            print('hola')

A = Agenda()

while True:
    print('\nQue opcion desea elegir:\n#1 Añadir\n#2 Mostrar\n#3 Buscar\n#4 Editar')
    Ask = int(input())

    if Ask == 1:
        A.Añadir()
    if Ask == 2:
        A.Mostrar()
    if Ask == 3:
        A.Buscar()