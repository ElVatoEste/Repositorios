<<<<<<< HEAD
Estudiantes = {
    'Estudiante1' : dict(zip(['Nombre', 'Apellido', 'Edad', 'Materia'], ['Manuel', 'Lopez', 17, 'Fisica'])),
    'Estudiante2' : dict(zip(['Nombre', 'Apellido', 'Edad', 'Materia'], ['Frederick', 'Jimenez', 16, 'Matematica'])),
    'Estudiante3' : dict(zip(['Nombre', 'Apellido', 'Edad', 'Materia'], ['Cesar', 'Augusto', 17, 'Quimica'])),
}
print('\n\n Informacion de estudiantes')
print('Estudiante #1')
print(Estudiantes['Estudiante1'], '\n')
print('Estudiante #2')
print(Estudiantes['Estudiante2'], '\n')
print('Estudiante #3')
print(Estudiantes['Estudiante3'],'\n')

# Modificaciones
print('-----------------------------------------------')
print('Cambio de nombre del estudiante #1'), '\n'
Estudiantes['Estudiante1']['Nombre'] = 'Diego'
print(Estudiantes['Estudiante1'])
print('-----------------------------------------------')

print('\n-----------------------------------------------')
print('Eliminar apellido #3')
Estudiantes['Estudiante3'].pop('Apellido')
=======
Estudiantes = {
    'Estudiante1' : dict(zip(['Nombre', 'Apellido', 'Edad', 'Materia'], ['Manuel', 'Lopez', 17, 'Fisica'])),
    'Estudiante2' : dict(zip(['Nombre', 'Apellido', 'Edad', 'Materia'], ['Frederick', 'Jimenez', 16, 'Matematica'])),
    'Estudiante3' : dict(zip(['Nombre', 'Apellido', 'Edad', 'Materia'], ['Cesar', 'Augusto', 17, 'Quimica'])),
}
print('\n\n Informacion de estudiantes')
print('Estudiante #1')
print(Estudiantes['Estudiante1'], '\n')
print('Estudiante #2')
print(Estudiantes['Estudiante2'], '\n')
print('Estudiante #3')
print(Estudiantes['Estudiante3'],'\n')

# Modificaciones
print('-----------------------------------------------')
print('Cambio de nombre del estudiante #1'), '\n'
Estudiantes['Estudiante1']['Nombre'] = 'Diego'
print(Estudiantes['Estudiante1'])
print('-----------------------------------------------')

print('\n-----------------------------------------------')
print('Eliminar apellido #3')
Estudiantes['Estudiante3'].pop('Apellido')
>>>>>>> 186abf19ab9f2a79d2746b5b473d7784ac388d12
print(Estudiantes['Estudiante3'])