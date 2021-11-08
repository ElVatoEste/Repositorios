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

print('\n El diccionario contiene la informacion de 3 estudiantes:\n')
print(f' Estudiante1: {Estudiante["Estudiante1"]["Nom1"]} {Estudiante["Estudiante1"]["Nom2"]} {Estudiante["Estudiante1"]["Apellido1"]} {Estudiante["Estudiante1"]["Apellido2"]}, {Estudiante["Estudiante1"]["Edad"]} años. Clases: {Estudiante["Estudiante1"]["Clases"]["Clase1"]}, {Estudiante["Estudiante1"]["Clases"]["Clase2"]}, {Estudiante["Estudiante1"]["Clases"]["Clase3"]}')
print(f' Estudiante2: {Estudiante["Estudiante2"]["Nom1"]} {Estudiante["Estudiante2"]["Nom2"]} {Estudiante["Estudiante2"]["Apellido1"]} {Estudiante["Estudiante2"]["Apellido2"]}, {Estudiante["Estudiante2"]["Edad"]} años. Clases: {Estudiante["Estudiante2"]["Clases"]["Clase1"]}, {Estudiante["Estudiante2"]["Clases"]["Clase2"]}, {Estudiante["Estudiante2"]["Clases"]["Clase3"]}')
print(f' Estudiante3: {Estudiante["Estudiante3"]["Nom1"]} {Estudiante["Estudiante3"]["Nom2"]} {Estudiante["Estudiante3"]["Apellido1"]} {Estudiante["Estudiante3"]["Apellido2"]}, {Estudiante["Estudiante3"]["Edad"]} años. Clases: {Estudiante["Estudiante3"]["Clases"]["Clase1"]}, {Estudiante["Estudiante3"]["Clases"]["Clase2"]}, {Estudiante["Estudiante3"]["Clases"]["Clase3"]}')

# Area de modificacion

# Cambiar
Std = input(str(f'\nIngrese el estudiante que desea modificar {Estudiante.keys()}: '))
Valor = input(str(f'Ingrese el valor que desea cambiar {Estudiante[Std].keys()}: '))
Nuevo = input(str(f'Cual sera el nuevo valor de ({Estudiante[Std][Valor]}): '))
print(f'Cambio realizado por "{Estudiante[Std][Valor]}"')
Cambio = Estudiante[Std][Valor] = Nuevo

print(f'\nActualizacion de datos: {Estudiante[Std]}\n')

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