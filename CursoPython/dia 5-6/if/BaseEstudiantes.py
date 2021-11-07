#diccionario con los datos de los estudiantes
Estudiantes = { 
    'Es1': {'PrimerNombre': 'Julio','SegundoNombre': 'Antonio', 'PrimerApellido':'Perez','SegundoApellido':'Perez', 'Edad':20, 
    'Clases': {'Clase1': 'Ingles', 'Clase2':'Calculo', 'Clase3': 'Fisica' }
    },
    'Es2': {'PrimerNombre': 'Antonio','SegundoNombre': 'Jose', 'PrimerApellido':'Palacios','SegundoApellido':'Jerez', 'Edad':20, 
    'Clases': {'Clase1': 'Ingles', 'Clase2':'Calculo', 'Clase3': 'Fisica'}
    },
    'Es3': {'PrimerNombre': 'Elia','SegundoNombre': 'Fernanda', 'PrimerApellido':'Perez','SegundoApellido':'Guzman', 'Edad':19, 
    'Clases': {'Clase1': 'Ingles', 'Clase2':'Calculo', 'Clase3': 'Fisica'}
    }
}
print('El diccionario contiene los valores de ')
print(f' Es1: {Estudiantes["Es1"]["PrimerNombre"]} {Estudiantes["Es1"]["SegundoNombre"]} {Estudiantes["Es1"]["PrimerApellido"]} {Estudiantes["Es1"]["SegundoApellido"]}, {Estudiantes["Es1"]["Edad"]} años. Clases: {Estudiantes["Es1"]["Clases"]["Clase1"]}, {Estudiantes["Es1"]["Clases"]["Clase2"]}, {Estudiantes["Es1"]["Clases"]["Clase3"]}')
print(f' Es2: {Estudiantes["Es2"]["PrimerNombre"]} {Estudiantes["Es2"]["SegundoNombre"]} {Estudiantes["Es2"]["PrimerApellido"]} {Estudiantes["Es2"]["SegundoApellido"]}, {Estudiantes["Es2"]["Edad"]} años. Clases: {Estudiantes["Es2"]["Clases"]["Clase1"]}, {Estudiantes["Es2"]["Clases"]["Clase2"]}, {Estudiantes["Es2"]["Clases"]["Clase3"]}')
print(f' Es3: {Estudiantes["Es3"]["PrimerNombre"]} {Estudiantes["Es3"]["SegundoNombre"]} {Estudiantes["Es3"]["PrimerApellido"]} {Estudiantes["Es3"]["SegundoApellido"]}, {Estudiantes["Es3"]["Edad"]} años. Clases: {Estudiantes["Es3"]["Clases"]["Clase1"]}, {Estudiantes["Es3"]["Clases"]["Clase2"]}, {Estudiantes["Es3"]["Clases"]["Clase3"]}')
#menu para elegir lo que se quiere hacer
opcion = int(input(f' 1. Modificar valores \n 2. Elimine valores \n 3. Agregar una materia \n'))

if opcion == 1:
    #Cambio de valores del diccionario
    est = str(input(f'Ingrese el estudiante que desea cambiar {Estudiantes.keys()} : \n'))
    valor = str(input(f'Ingrese cual valor desea cambiar {Estudiantes[est].keys()}: \n'))
    #opcion por si los valores que se quieren cambiar son las clases
    if valor == 'Clases':
        cambiocla = str(input(f'Ingrese cual clase quisiera cambiar {Estudiantes[est]["Clases"].keys()}: \n'))
    
    elif valor == 'PrimerNombre' or valor == 'SegundoNombre' or valor == 'PrimerApellido' or valor == 'SegundoApellido' or valor == 'Edad':
        cambio = str(input(f'Ingrese cual seria el nuevo valor de {Estudiantes[est][valor]}: \n'))
        Estudiantes[est][valor] = cambio
    #si ninguna de esas condiciones se da ocurre esto
    else:
        print('No existe ese valor en el diccionario')
    #print(f'Estudiante: {Estudiantes[est]["PrimerNombre"]} {Estudiantes[est]["SegundoNombre"]} {Estudiantes[est]["PrimerApellido"]} {Estudiantes[est]["SegundoApellido"]}, {Estudiantes[est]["Edad"]} años. Clases: {Estudiantes[est]["Clases"]["Clase1"]}, {Estudiantes[est]["Clases"]["Clase2"]}, {Estudiantes[est]["Clases"]["Clase3"]}')

if opcion == 2:
    est = str(input(f'Ingrese el estudiante {Estudiantes.keys()} : \n'))
    #para borrar se pide que valor se quiere borrar y se usa el metodo pop para eliminarlo
    borrar = str(input(f'Ingrese cual valor desea borrar {Estudiantes[est].keys()}: \n'))
    Estudiantes[est].pop(borrar)

if opcion == 3:
    #se agrega una clase con el metodo setdefault, este metodo solo agrega la clase si no existe ya
    est = str(input(f'Ingrese el estudiante que desea cambiar {Estudiantes.keys()} : \n'))
    clase = str(input(f'Ingrese la materia que desea agregar: \n'))
    Estudiantes[est]['Clases'].setdefault('Clase4',clase)
    print(Estudiantes[est])
    #print(f'Estudiante: {Estudiantes[est]["PrimerNombre"]} {Estudiantes[est]["SegundoNombre"]} {Estudiantes[est]["PrimerApellido"]} {Estudiantes[est]["SegundoApellido"]}, {Estudiantes[est]["Edad"]} años. Clases: {Estudiantes[est]["Clases"]["Clase1"]}, {Estudiantes[est]["Clases"]["Clase2"]}, {Estudiantes[est]["Clases"]["Clase3"]}, {Estudiantes[est]["Clases"]["Clase4"]}')

print(Estudiantes['Es1'])


