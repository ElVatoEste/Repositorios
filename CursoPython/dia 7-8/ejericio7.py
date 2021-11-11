'''
Los empleados de una fábrica trabajan en dos turnos diurno y nocturno, se desea Calcular el
jornal diario y el total devengado de cada uno de ellos durante una semana de trabajo de
acuerdo con el siguiente criterio:

• Tarifa diurna 18000 Córdobas
• Tarifa nocturna 27000 Córdobas

Caso de ser domingo la tarifa se incrementará en 2000 pesos diurno y 3000 nocturno
Atributos:
nombre: tipo cadena (debe ser nombre y apellido)
turnoA: tipo cadena y turnoB: tipo cadena
tarifaD y tarifaN: tipo int
día: tipo cadena

'''


print('\n-------------------------------')
print('Sistemas de tarifas laborales')
print('-------------------------------\n')


# Definir la tarifa semanal de cada turno

TurnoA = 18000
TurnoB = 27000

#Trabajo domingos 
ExtraA = 2000
ExtraB = 3000

# Establecer listas

Trabajadores = []
Salario = []

# Zona de calculos
DiaTurnoA = TurnoA/6
DiaTurnoB = TurnoB/6

MensualA = TurnoA*4
MensualB = TurnoB*4


while True:
    Nomb = str(input('Ingrese el nombre del trabajador: '))
    Apellido = str(input('Ingrese el apellido del trabajador: '))
    
    #Junto el nombre
    NombCompleto = Nomb+(' ')+Apellido

    # Lo agrego en la lista
    Trabajadores.append(NombCompleto)

    Turno = int(input(f'{NombCompleto} opto por:\n1. Turno Diuno\n2. Turno Nocturno\n'))

    while Turno != 1 and Turno != 2:
        print('La opcion que eligio no corresponde a ninguna de la lista')
        Turno = int(input(f'{NombCompleto} opto por:\n1. Turno Diuno\n2. Turno Nocturno\n'))
    
    if Turno == 1:
        Salario.append(TurnoA)
        
    else:
        Salario.append(TurnoB)


    Extra = str(input(f'{NombCompleto} va a trabajar extra? y/n:'))
    while Extra != 'y' and Extra != 'n':
            print('Caracter no valido')
            Extra = input(str(f'{NombCompleto} va a trabajar extra? y/n: '))
    if Extra == 'y':
        Contador = int(input('Cuantos Domingos desea trabajar? [1-4]: '))
        while Contador > 4:
            print('La cantidad sobrepasa el limite maximo por semana [4]')
            Contador = int(input('Cuantos Domingos desea trabajar? [1-4]: '))
            Salario.append(ExtraA*Contador)
    else:
        pass
    
    TotalDomingo = sum(Salario)
    print(f'{NombCompleto}')
   a
    
    Menu = input(str('Desea salir del sistema? y/n: '))
    if Menu == ('y'):
        exit()