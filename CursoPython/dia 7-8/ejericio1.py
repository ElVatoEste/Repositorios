'''
Realice un programa en Python que leer los datos (nombre, edad y sueldo) de n empleados
(máximo 10) e imprima los trabajadores con sueldo máximo y mínimo, así como la media de
los sueldos
'''

Trabajadores = {

}

print(Trabajadores)

print('\n*****************************')
print('** Sistema de trabajadores **')
print('*****************************\n')

exit()
while True:

    print('\n*****************************')
    print('** Sistema de trabajadores **')
    print('*****************************\n')

    Cantidad = int(input('¿Cuantos trabajadores desea agregar?: '))
    while Cantidad > 10:
        print('La cantidad solicitada excede el maximo disponible (10)')
        print('Ingrese nuevamente...')
        Cantidad = int(input('¿Cuantos trabajadores desea agregar?: '))
    
    for x in range(Cantidad):
        print('hola')