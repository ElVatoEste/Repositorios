
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


Std = input(str(f'Ingrese el estudiante que desea cambiar {Estudiante.keys()} : \n'))
Llave = input(str('Ingrese el nombre de la llave que sea agregar: '))
Valor = input(str('Ingrese el valor que desea agregar:'))
Estudiante[Std]['Clases'].setdefault(Llave, Valor)
