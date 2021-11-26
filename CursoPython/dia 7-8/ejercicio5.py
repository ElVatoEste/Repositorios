'''
Desarrolle un programa en Python que utilice una instrucción while para determinar el salario bruto
para cada uno de varios empleados. Los cuales trabajan 6 horas al día con una tarifa de 300 córdobas el día
Solicitar: El nombre del empleado y calcular el salario tomando en cuenta la cantidad de días trabajados

'''


print('\n----------------------------')
print('** Calculadora de salario ** ')
print('----------------------------\n')


Salarios={}

Salida = True

while Salida:

    Nombre = str(input('Cual es el nombre de su obrero?: '))
    Dias = int(input('Cuantas dias trabaja a la semana: '))

    # Datos

    Horas = 6
    Paga = 300 # Al dia

    Dia = Horas*Paga

    Salario = Dia*Dias

    ask = str(input('Desea salir del sistema? y/n: '))

    if ask == 'y' or ask == 'Y':
        Salida = False

print(f'\nEl obrero trabaja un total de {Dias} dias a la semana')
print(f'El obrero gana a la semana un total de {Salario} coordobas a la semana')
