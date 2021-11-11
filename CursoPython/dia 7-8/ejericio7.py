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


print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~ Sistemas de tarifas laborales ~~~')
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

    Nomb = str(input('Ingrese el nombre del trabajador: '))
    Apellido = str(input('Ingrese el apellido del trabajador: '))
    
    #Junto el nombre
    NombCompleto = Nomb+(' ')+Apellido

    Turno = int(input(f'\n {NombCompleto} opto por:\n1. Turno Diuno = {TurnoA} semanal\n2. Turno Nocturno = {TurnoB} semanal\n'))

    while Turno != 1 and Turno != 2:
        print('\nLa opcion que eligio no corresponde a ninguna de la lista')
        Turno = int(input(f'{NombCompleto} opto por:\n1. Turno Diuno = {TurnoA} semanal\n2. Turno Nocturno = {TurnoB} semanal\n'))
    
    if Turno == 1:
        Salario.append(TurnoA)
        
    else:
        Salario.append(TurnoB)


    Extra = str(input(f'\n¿{NombCompleto} va a trabajar extra? y/n: '))
    while Extra != 'y' and Extra != 'n':
            print('\nCaracter no valido')
            Extra = input(str(f'{NombCompleto} va a trabajar extra? y/n: '))

    if Extra == 'y':
        Contador = int(input('\nCuantos Domingos desea trabajar? [1-4]: '))

        while Contador > 4:
            print('\nLa cantidad sobrepasa el limite maximo por semana [4]')
            Contador = int(input('Cuantos Domingos desea trabajar? [1-4]: '))

        TurnoExtra = int(input(f'\n{NombCompleto} los domingos hace:\n1. Turno Diuno = {ExtraA} el dia\n2. Turno Nocturno = {ExtraB} el dia\n'))

        while TurnoExtra != 1 and TurnoExtra != 2:
            print('\nLa opcion que eligio no corresponde a ninguna de la lista')
            TurnoExtra = int(input(f'{NombCompleto} los domingos hace:\n1. Turno Diuno\n2. Turno Nocturno\n'))

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
                print(f'\nA {NombCompleto} le pagaran {DiaTurnoA} diario mensaulmente son {MensualA}\aal hacer {Contador} domingos extra, se le agregara a su salario {ExtraA*Contador}')
            else:
                print(f'\nA {NombCompleto} le pagaran {DiaTurnoA} diario mensaulmente son {MensualA}\nal hacer {Contador} domingos extra, se le agregara a su salario {ExtraB*Contador}')

        print(f'\nA {NombCompleto} le pagaran {DiaTurnoA} diario mensualmente seran {MensualA} al no trabajar los domingos ')
    else:
        if Extra == 'y':
            if TurnoExtra == 1:
                print(f'\nA {NombCompleto} le pagaran {DiaTurnoB} diario mensaulmente son {MensualB}\aal hacer {Contador} domingos extra, se le agregara a su salario {ExtraA*Contador}')
            else:
                print(f'\nA {NombCompleto} le pagaran {DiaTurnoB} diario mensaulmente son {MensualB}\nal hacer {Contador} domingos extra, se le agregara a su salario {ExtraB*Contador}')

        print(f'\nA {NombCompleto} le pagaran {DiaTurnoB} diario mensualmente seran {MensualB} al no trabajar los domingos ')


    Menu = input(str('\nSeguira agregando trabajadores? y/n: '))
    if Menu == ('n'):

        print('Registros guardados tras ejecutar programa ')
        print(Trabajadores)

        exit()
