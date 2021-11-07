# Diccionario
Diccionario = {'Nombre' : 'Manuel', 'Apellido' : 'Lopez', 'Edad' : 17, 'Padres' : ['Manuel', 'Ruth']}
# Llaves del diccionario
print('\n------------------------------------')
print('El nombre es: ', Diccionario['Nombre'])
print('------------------------------------')
print('El apellido es:', Diccionario['Apellido'])
print('------------------------------------')
print('La edad es:', Diccionario['Edad'])
print('------------------------------------')
print('Sus padres son:', Diccionario['Padres'])
print('------------------------------------')

Diccionario['Nombre'] = 'Alejandro'

print(Diccionario,'\n')

Diccionario['Padres'][0] = 'Evenor'
print('\n',Diccionario,'\n')