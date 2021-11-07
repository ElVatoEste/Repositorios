#explicacion simple
'''
print('\n------------------------------------------------')
V1 = int(input('Ingrese el primer valor: '))
V2 = int(input('Ingrese el segundo valor: '))
print('------------------------------------------------\n')

if V1 > V2:
    print(f'El valor {V1} es el mayor')
if V1 < V2:
    print(f'El valor {V2} es el mayor')
if V1 == V2:
    print('Los valores son iguales')
'''

# ejercicio 1
print('\n------------------------------------------------')
V1 = float(input('Ingrese el precio de la manzana en la segunda tienda: '))
V2 = float(input('Ingrese el precio de la manzana en la primera tienda: '))
print('------------------------------------------------\n')

if V1 < V2:
    print('La primera tienda tiene mejor precio')
if V1 > V2:
    print('La segunda tienda tiene mejor precio')
if V1 == V2:
    print('Ambas tiendas tienen el mismo precio')
print('------------------------------------------------\n')