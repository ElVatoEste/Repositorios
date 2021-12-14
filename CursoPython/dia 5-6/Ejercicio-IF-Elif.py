
# Preguntamos los nombres
print('\n------------------------------------------------')
Per1 = str(input('¿Como se llama el primer estudiante? '))
Per2 = str(input('¿Como se llama el segundo estudiante? '))
Per3 = str(input('¿Como se llama el tercer estudiante? '))
print('------------------------------------------------')

# Preguntamos sus notas
Est1 = int(input(f'Ingrese la calificación de {Per1}: '))
Est2 = int(input(f'Ingrese la calificación de {Per2}: '))
Est3 = int(input(f'Ingrese la calificación de {Per3}: '))
print('------------------------------------------------')

# Establecemos condiciones
# Condicione para establecer quien salio mejor
if Est1 > Est2 and Est1 > Est3:
    print(f'{Per1} fue el que salio mejor')
    print('------------------------------------------------')
elif Est2 > Est1 and Est2 > Est3: 
    print(f'{Per2} fue el que salio mejor')
    print('------------------------------------------------')
elif Est3 > Est1 and Est3 > Est2 :
    print(f'{Per3} fue el que salio mejor')
    print('------------------------------------------------')

# Condiciones para establecer quien salio peor
if Est1 < Est2 and Est1 < Est3:
    print(f'{Per1} fue el que salio peor')
    print('------------------------------------------------\n')
elif Est2 < Est1 and Est2 < Est3: 
    print(f'{Per2} fue el que salio peor')
    print('------------------------------------------------\n')
elif Est3 < Est1 and Est3 < Est2 :
    print(f'{Per3} fue el que salio peor')
    print('------------------------------------------------\n')

# Condiciones si hay notas que se repiten (solo si se repiten), mencionar quienes coinciden
if Est1 == Est2 and Est1 == Est3 and Est2 == Est3:
    print(f'{Per1}, {Per2} y {Per3} tienen la misma nota de: {Est1}')
    print('------------------------------------------------\n')
elif Est1 == Est2 and Est1 != Est3:
    print(f'{Per1} y {Per2} tienen la misma nota de: {Est1}')
    print('------------------------------------------------\n')
elif Est1 == Est3 and Est1 != Est3:
    print(f'{Per1} y {Per3} tienen la misma nota de: {Est1}')
    print('------------------------------------------------\n')
elif Est2 == Est3 and Est3 != Est1:
    print(f'{Per2} y {Per3} tienen la misma nota de: {Est2}')
    print('------------------------------------------------\n')

