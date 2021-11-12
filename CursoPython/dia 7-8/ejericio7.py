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

# Condicion while true para hacer el blucle infinito
while True:

    # Uso una lista para usalar como sistema de suma
    # Dejo dentro del bucle para reiniciar mi sistema de suma cada vez que se reinicie el bucle
    # Y que no se guarden los datos del trabajador anterior

    Salario = [] 

    # Solicito el nombre y apellido dle trabajador
    Nomb = str(input(f'{Yellow}Ingrese el nombre del trabajador:{Green} '))
    Apellido = str(input(f'{Yellow}Ingrese el apellido del trabajador:{Green} '))
    
    #Junto el nombre
    NombCompleto = Nomb+(' ')+Apellido

    # Pregunto en que turno estara
    Turno = int(input(f'{Yellow}\n{NombCompleto} opto por:\n1. Turno Diuno = {TurnoA} semanal\n2. Turno Nocturno = {TurnoB} semanal\n{Green}'))

    # Una condicion while para validar que el numero esta dentro de la lista
    while Turno != 1 and Turno != 2:
        print(f'\n{Red}La opcion que eligio no corresponde a ninguna de la lista')
        Turno = int(input(f'{Yellow}\n{NombCompleto} opto por:\n1. Turno Diuno = {TurnoA} semanal\n2. Turno Nocturno = {TurnoB} semanal\n{Green}'))
    
    # Condicion if para ver por que salario opto, si el de dia o noche
    if Turno == 1:
        Salario.append(TurnoA)
        
    else:
        Salario.append(TurnoB)

    # Pregunto si va a trabajar los domingos
    Extra = str(input(f'{Yellow}\n¿{NombCompleto} va a trabajar extra? y/n:{Green} '))

    # Valido la respuesta
    while Extra != 'y' and Extra != 'n':
            print(f'\n{Red}Caracter no valido')
            Extra = str(input(f'{Yellow}\n¿{NombCompleto} va a trabajar extra? y/n:{Green} '))

    # En caso que trabaje, le pregunto cuantos dias al mes
    if Extra == 'y':
        Contador = int(input(f'{Yellow}\nCuantos Domingos desea trabajar al mes? [1-4]: '))

        # Valido la cantidad
        while Contador > 4:
            print(f'{Red}\nLa cantidad sobrepasa el limite maximo por semana [4]')
            Contador = int(input(f'{Yellow}\nCuantos Domingos desea trabajar? [1-4]: '))

        # Solicito el turno
        TurnoExtra = int(input(f'{Yellow}\n{NombCompleto} los domingos hace:\n1. Turno Diuno = {ExtraA} el dia\n2. Turno Nocturno = {ExtraB} el dia\n'))

        # Valido datos
        while TurnoExtra != 1 and TurnoExtra != 2:
            print(f'{Red}\nLa opcion que eligio no corresponde a ninguna de la lista')
            TurnoExtra = int(input(f'{Yellow}\n{NombCompleto} los domingos hace:\n1. Turno Diuno = {ExtraA} el dia\n2. Turno Nocturno = {ExtraB} el dia\n'))

        # Condicion if para ver que turno escogio y asi agregar su salario
        if TurnoExtra == 1:
            Salario.append(ExtraA*Contador)

        else:
            Salario.append(ExtraB*Contador)
    
    # Sumo el total de todo su salario
    Total = sum(Salario)
    
    # Agrego los datos a un diccionario
    Trabajadores.setdefault(NombCompleto, Total)
    
    # Condicciones para ver que mensaje se enviara

    # opcion si se eligio el turno matutino normal
    if Turno == 1:

        # opcion si se trabajo extra
        if Extra == 'y':
            # Si se trabajo de dia los domingos
            if TurnoExtra == 1:
                print(f'{Blue}\nA {NombCompleto} le pagaran {DiaTurnoA} diario mensaulmente son {MensualA} al hacer {Contador} domingos extra, se le agregara a su salario {ExtraA*Contador}')
            # Si se trabajo de noche los domingos
            else:
                print(f'{Blue}\nA {NombCompleto} le pagaran {DiaTurnoA} diario mensaulmente son {MensualA} al hacer {Contador} domingos extra, se le agregara a su salario {ExtraB*Contador}')
        
        # Mensaje si no se trabajo los domingos
        else:
            print(f'{Blue}\nA {NombCompleto} le pagaran {DiaTurnoA} diario mensualmente seran {MensualA} al no trabajar los domingos 1')
    
        # opcion si se eligio el turno nocturno normal
    elif Turno == 2:

        # opcion si se trabajo extra
        if Extra == 'y':
            # Si se trabajo de dia los domingos
            if TurnoExtra == 1:
                print(f'{Blue}\nA {NombCompleto} le pagaran {DiaTurnoB} diario mensaulmente son {MensualB} al hacer {Contador} domingos extra, se le agregara a su salario {ExtraA*Contador}')
            # Si se trabajo de noche los domingos
            else:
                print(f'\n{Blue}A {NombCompleto} le pagaran {DiaTurnoB} diario mensaulmente son {MensualB} al hacer {Contador} domingos extra, se le agregara a su salario {ExtraB*Contador}')
        
        # Mensaje si no se trabajo los domingos
        else:
            print(f'\n{Blue}A {NombCompleto} le pagaran {DiaTurnoB} diario mensualmente seran {MensualB} al no trabajar los domingos 2')

    # Preguntar si se seguira agregando

    Menu = input(str(f'\n{Yellow}Seguira agregando trabajadores? y/n: '))
    
    # while para validar opcion
    while Menu != 'y' and Menu != 'n':
            print(f'\n{Red}Caracter no valido')
            Menu = str(input(f'{Yellow}\n¿{NombCompleto} va a trabajar extra? y/n:{Green} '))

    # If para que en caso que no se quiera se de por terminado el blucle
    if Menu == ('n'):

        # Imprimir todos los trabajadores que se hicieron y que se guardaron en cache
        print(f'\n{Magenta}Registros guardados tras ejecutar programa ')
        print(Green, Trabajadores, White)

        exit()
