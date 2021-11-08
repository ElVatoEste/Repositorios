Estudiante = {
    'Estudiante1': {'Nom1':'Jose', 'Nom2':'Antonio', 'Apellido1':'Martinez', 'Apellido2':'Cuadras', 'Edad':26,
    'Clases': {'Clase1': 'Fisica', 'Clase2': 'Matematica', 'Clase3': 'Ingles'}
    },
    'Estudiante2': {'Nom1':'Karen', 'Nom2':'Julieth', 'Apellido1':'Perez', 'Apellido2':'Mojica', 'Edad':24,
    'Clases': {'Clase1': 'Fisica', 'Clase2': 'Matematica', 'Clase3': 'Ingles'}
    },
    'Estudiante3': {'Nom1':'Hector', 'Nom2':'Migel', 'Apellido1':'Zapata', 'Apellido2':'Lopez', 'Edad':26,
    'Clases': {'Clase1': 'Fisica', 'Clase2': 'Matematica', 'Clase3': 'Ingles'}
    },
}

print('El diccionario contiene los valores de 3 estudiantes:')
print('\n', Estudiante['Estudiante1'], '\n')
print( Estudiante['Estudiante2'], '\n')
print( Estudiante['Estudiante3'], '\n')


# Area de modificacion

# Cambiar
Std = input(str(f'Ingrese el estudiante que desea modificar {Estudiante.keys()}: '))
Valor = input(str(f'Ingrese el valor que desea cambiar {Estudiante[Std].keys()}: '))
Nuevo = input(str(f'Cual sera el nuevo valor de ({Estudiante[Std][Valor]}): '))
print(f'Cambio realizado por "{Estudiante[Std][Valor]}"')
Cambio = Estudiante[Std][Valor] = Nuevo

print('\n', Estudiante[Std], '\n')

# Agregar
Std = input(str(f'Ingrese a que estudiante desea agregar una clase {Estudiante.keys()}: '))
Valor = input(str('Ingrese la clase que desea agregar: '))
Estudiante[Std]['Clases'].setdefault('Clase4', Valor)

print(f'\nActualizacion de datos: {Estudiante[Std]}\n')

# Eliminar
Std = str(input(f'Ingrese el estudiante {Estudiante.keys()}: '))
borrar = str(input(f'Ingrese cual valor desea borrar {Estudiante[Std].keys()}: '))
Estudiante[Std].pop(borrar)

print(f'\nActualizacion de datos: {Estudiante[Std]}\n')