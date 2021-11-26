'''
Desarrolle un programa en Python que utilice una instrucción while para determinar el salario bruto
para cada uno de varios empleados. Los cuales trabajan 6 horas al día con una tarifa de 300 córdobas el día
Solicitar: El nombre del empleado y calcular el salario tomando en cuenta la cantidad de días trabajados

'''


print('\n----------------------------')
print('** Calculadora de salario ** ')
print('----------------------------')


Salarios={}

Salida = True

while Salida:

    Nombre = str(input('\nCual es el nombre de su obrero?: '))
    Dias = int(input('Cuantas dias trabaja a la semana: '))

    # Datos

    Horas = 6
    Paga = 300 # Al dia

    Dia = Horas*Paga

    Salario = Dia*Dias

    Salarios.setdefault(Nombre, {'Nombre': Nombre, 'Salario':Salario})

    ask = str(input('\nSeguira agregando trabajadores? y/n: '))

    if ask == 'n' or ask == 'N':
        Salida = False

for x in Salarios:
    print('\n-------------------------------------')
    print('El trabajador', Salarios[x]['Nombre'],'gana', Salarios[x]['Salario'], 'a la semana ')
    print('-------------------------------------')