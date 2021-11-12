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
# Zona de colores -----------------------
Red = '\033[91m'
Green = '\033[92m'
Yellow ='\033[93m'
Blue = '\033[94m'
Magenta = '\033[95m'
Cyan = '\033[96m'
White = '\033[97m'
Black = '\033[98m'
Gray = '\033[90m'
# ----------------------- Zona de colores


# Saludo 
print(f'{Blue}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'~~~ {Red}Sistemas de tarifas laborales {Blue}~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')


# Definir la tarifa semanal de cada turno

TurnoA = 18000
TurnoB = 27000

#Trabajo domingos 
ExtraA = 2000
ExtraB = 3000

# Establecer diccionario

Trabajadores = {}

# Zona de calculos
DiaTurnoA = TurnoA/6
DiaTurnoB = TurnoB/6

MensualA = TurnoA*4
MensualB = TurnoB*4


while True:

    # Dejo dentro del bucle para reiniciar mi sistema de suma
    Salario = [] 

    Nomb = str(input(f'{Yellow}Ingrese el nombre del trabajador:{Green} '))
    Apellido = str(input(f'{Yellow}Ingrese el apellido del trabajador:{Green} '))
    
    #Junto el nombre
    NombCompleto = Nomb+(' ')+Apellido

    Turno = int(input(f'{Yellow}\n{NombCompleto} opto por:\n1. Turno Diuno = {TurnoA} semanal\n2. Turno Nocturno = {TurnoB} semanal\n{Green}'))

    while Turno != 1 and Turno != 2:
        print(f'\n{Red}La opcion que eligio no corresponde a ninguna de la lista')
        Turno = int(input(f'{Yellow}\n{NombCompleto} opto por:\n1. Turno Diuno = {TurnoA} semanal\n2. Turno Nocturno = {TurnoB} semanal\n{Green}'))
    
    if Turno == 1:
        Salario.append(TurnoA)
        
    else:
        Salario.append(TurnoB)


    Extra = str(input(f'{Yellow}\n¿{NombCompleto} va a trabajar extra? y/n:{Green} '))
    while Extra != 'y' and Extra != 'n':
            print(f'\n{Red}Caracter no valido')
            Extra = str(input(f'{Yellow}\n¿{NombCompleto} va a trabajar extra? y/n:{Green} '))

    if Extra == 'y':
        Contador = int(input(f'{Yellow}\nCuantos Domingos desea trabajar? [1-4]: '))

        while Contador > 4:
            print(f'{Red}\nLa cantidad sobrepasa el limite maximo por semana [4]')
            Contador = int(input(f'{Yellow}\nCuantos Domingos desea trabajar? [1-4]: '))

        TurnoExtra = int(input(f'{Yellow}\n{NombCompleto} los domingos hace:\n1. Turno Diuno = {ExtraA} el dia\n2. Turno Nocturno = {ExtraB} el dia\n'))

        while TurnoExtra != 1 and TurnoExtra != 2:
            print(f'{Red}\nLa opcion que eligio no corresponde a ninguna de la lista')
            TurnoExtra = int(input(f'{Yellow}\n{NombCompleto} los domingos hace:\n1. Turno Diuno = {ExtraA} el dia\n2. Turno Nocturno = {ExtraB} el dia\n'))

        if TurnoExtra == 1:
            Salario.append(ExtraA*Contador)

        else:
            Salario.append(ExtraB*Contador)

    else:
        pass
    
    Total = sum(Salario)
    Trabajadores.setdefault(NombCompleto, Total)
    
    if Turno == 1:
        if Extra == 'y':
            if TurnoExtra == 1:
                print(f'{Blue}\nA {NombCompleto} le pagaran {DiaTurnoA} diario mensaulmente son {MensualA} al hacer {Contador} domingos extra, se le agregara a su salario {ExtraA*Contador}')
            else:
                print(f'{Blue}\nA {NombCompleto} le pagaran {DiaTurnoA} diario mensaulmente son {MensualA} al hacer {Contador} domingos extra, se le agregara a su salario {ExtraB*Contador}')
        else:
            print(f'{Blue}\nA {NombCompleto} le pagaran {DiaTurnoA} diario mensualmente seran {MensualA} al no trabajar los domingos 1')
    
    elif Turno == 2:
        if Extra == 'y':
            if TurnoExtra == 1:
                print(f'{Blue}\nA {NombCompleto} le pagaran {DiaTurnoB} diario mensaulmente son {MensualB} al hacer {Contador} domingos extra, se le agregara a su salario {ExtraA*Contador}')
            else:
                print(f'\n{Blue}A {NombCompleto} le pagaran {DiaTurnoB} diario mensaulmente son {MensualB} al hacer {Contador} domingos extra, se le agregara a su salario {ExtraB*Contador}')
        else:
            print(f'\n{Blue}A {NombCompleto} le pagaran {DiaTurnoB} diario mensualmente seran {MensualB} al no trabajar los domingos 2')


    Menu = input(str(f'\n{Yellow}Seguira agregando trabajadores? y/n: '))
    while Menu != 'y' and Menu != 'n':
            print(f'\n{Red}Caracter no valido')
            Menu = str(input(f'{Yellow}\n¿{NombCompleto} va a trabajar extra? y/n:{Green} '))

    if Menu == ('n'):

        print(f'\n{Magenta}Registros guardados tras ejecutar programa ')
        print(Green, Trabajadores, White)

        exit()
