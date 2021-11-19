from Datos.deporte import *
from Archivos.Archivos import *




#-----------------------------------------------------------------------
#   VALIDAR IFORMACION DE UN DEPORTE


def InformacionUnDeporte():
    print('\n---------------------------------------------------------------------------------')
    print('----------------------------- Mostrar Deporte ------------------------------------')
    print('---------------------------------------------------------------------------------\n')
    if len(Deportes) == 0:
        print('No Existe Registro') 
    else:
        print('\n---------------------------------------------------------------------------------')
        print('DEPORTES EXISTENTES')
        print('\n---------------------------------------------------------------------------------')
        for D in Deportes:
            print(D,' --- ',Deportes[D]['Nombre'])
            print('\n---------------------------------------------------------------------------------')
        pass
    pass
    Patron = 'TEC##'
    print('\n---------------------------------------------------------------------------------\n')
    id = str(input(('Ingrese el ID TEC## ')))
    idDeporte = str('TEC##'+id)
    if not idDeporte in Deportes:
        print('\n---------------------------------------------------------------------------------')
        print('El deporte que desea eliminar,no existe en el registro de la base de datos del TEC en la cede central')
        print('---------------------------------------------------------------------------------')
        Menu2()
    pass
    print('---------------------------------------------------------------------------------')
    print(D,' --- ',Deportes[idDeporte]['Nombre'])
    print('-- ',Deportes[idDeporte]['Explicacion'])
    print('-- ',Deportes[idDeporte]['Lugar'])
    print('\n---------------------------------------------------------------------------------')
    Menu2()
pass


#-----------------------------------------------------------------------
#   VALIDAR INFORMACION SEGUN LUGAR

def InformacionSegunLugar():
    print('\n---------------------------------------------------------------------------------')
    print('----------------- Mostrar Deporte Segun Lugar ------------------------------------')
    print('---------------------------------------------------------------------------------\n')
    if len(Deportes) == 0:
        print('No Existe Registro') 
    else:
        print('\n---------------------------------------------------------------------------------')
        print('DEPORTES EXISTENTES')
        print('\n---------------------------------------------------------------------------------')
        for D in Deportes:
            print(D,' --- ',Deportes[D]['Nombre'],' --- ',Deportes[D]['Lugar'])
            print('\n---------------------------------------------------------------------------------')
        pass
    pass
    Lugar = str(input('Ingrese el lugar: '))
    for x in Deportes:
        if not Lugar in Deportes[x]['Lugar']:
            print('\n---------------------------------------------------------------------------------')
            print('El deporte que desea eliminar,no existe en el registro de la base de datos del TEC en la cede central')
            print('---------------------------------------------------------------------------------')
            Menu2()
        pass
        if Lugar in Deportes[x]['Lugar']:
            print('---------------------------------------------------------------------------------')
            print(x,' --- ',Deportes[x]['Nombre'])
            print('-- ',Deportes[x]['Explicacion'])
            print('-- ',Deportes[x]['Lugar'])
            print('\n---------------------------------------------------------------------------------')
        pass
    Menu2()
    pass
pass



#-----------------------------------------------------------------------
#   VALIDAR DATOS AL INSERTAR 


def ValidarInsertarDeporte():
    print('\n---------------------------------------------------------------------------------')
    print('----------------------------- Insertar Deporte ----------------------------------')
    print('---------------------------------------------------------------------------------\n')
    Patron = 'TEC##'
    print('\n---------------------------------------------------------------------------------\n')
    id = str(input(('Ingrese el ID TEC## ')))
    idDeporte = str('TEC##'+id)
    if idDeporte in Deportes:
        print('\n---------------------------------------------------------------------------------')
        print('Este ID ya existe')
        print('---------------------------------------------------------------------------------')
        Menu()
    pass    
    print('---------------------------------------------------------------------------------')
    Nom = str(input('Ingrese el nombre del deporte: '))
    if len(Nom) < 5:
        print('\n---------------------------------------------------------------------------------')
        print('Solo Se Admiten Datos Mayores a 5 Caracteres')
        print('---------------------------------------------------------------------------------')
        Menu()
    print('---------------------------------------------------------------------------------')
    Desc = str(input('Ingrese la descripcion: '))
    if len(Desc) < 5: 
        print('\n---------------------------------------------------------------------------------')
        print('Solo Se Admiten Datos Mayores a 5 Caracteres')
        print('---------------------------------------------------------------------------------')
        Menu()
    if len(Desc) > 50:
        print('\n---------------------------------------------------------------------------------')
        print('No Se Admiten Datos Mayores De 50 Caracteres')
        print('---------------------------------------------------------------------------------')
        Menu()
    print('---------------------------------------------------------------------------------')
    Lug = str(input('Ingrese El lugar: '))
    if len(Lug) < 5: 
        print('\n---------------------------------------------------------------------------------')
        print('No Se Admiten Datos Menores De 5 Caracteres')
        print('---------------------------------------------------------------------------------')
        Menu()
    if len(Lug) > 50:
        print('\n---------------------------------------------------------------------------------')
        print('Solo Se Admiten Datos Mayores De 50 Caracteres')
        print('---------------------------------------------------------------------------------')
        Menu()
    print('---------------------------------------------------------------------------------')
    valores = {'Nombre' : Nom, 'Descripcion': Desc, 'Lugar': Lug}
    Deportes.setdefault(idDeporte,valores)
    print('\n---------------------------------------------------------------------------------')
    print('Registro Exitoso')
    print('---------------------------------------------------------------------------------')
    Menu()
pass


#-----------------------------------------------------------------------
#   VALIDAR IFORMACION


def InformacionCompleta():
    if len(Deportes) == 0:
        print('No Existe Registro') 
    else:
        print('\n---------------------------------------------------------------------------------')
        print('DEPORTES EXISTENTES')
        print('\n---------------------------------------------------------------------------------')
        for D in Deportes:
            print(D,' --- ',Deportes[D]['Nombre'])
            print('-- ',Deportes[D]['Explicacion'])
            print('-- ',Deportes[D]['Lugar'])
            print('\n---------------------------------------------------------------------------------')
        Menu2()
    pass
pass


#-----------------------------------------------------------------------
#   VALIDAR DATOS AL ELIMINAR


def ValidarEliminarDeporte():
    print('\n---------------------------------------------------------------------------------')
    print('----------------------------- Eliminar Deporte ----------------------------------')
    print('---------------------------------------------------------------------------------\n')
    Patron = 'TEC##'
    print('\n---------------------------------------------------------------------------------\n')
    id = str(input(('Ingrese el ID TEC## ')))
    idDeporte = str('TEC##'+id)
    if not idDeporte in Deportes:
        print('\n---------------------------------------------------------------------------------')
        print('El deporte que desea eliminar,no existe en el registro de la base de datos del TEC en la cede central')
        print('---------------------------------------------------------------------------------')
        Menu()
    pass
    print('---------------------------------------------------------------------------------')
    validar = str(input(f'¿Esta seguro que desea eliminar el deporte {idDeporte} S/N ? '))
    if validar == 'S' or validar == 's':
        Deportes.pop(idDeporte)
        print('\n---------------------------------------------------------------------------------')
        print('Registro Eliminado Exitosamente')
        print('---------------------------------------------------------------------------------')
        Menu()
    if validar == 'N'  or validar == 'n':
        print('\n---------------------------------------------------------------------------------')
        print('Proceso cancelado')
        print('---------------------------------------------------------------------------------')
        Menu()
    pass
pass


#-----------------------------------------------------------------------
#   MOSTRAR MENU


def Menu():
    while True:
        print('\n---------------------------------------------------------------------------------')
        print('Bienvenidos al DEPORSIS')
        print('---------------------------------------------------------------------------------\n')
        MostrarDeporte()
        print('\n---------------------------------------------------------------------------------')
        print('----------------------------- Menu De Opciones ----------------------------------')
        print('---------------------------------------------------------------------------------\n')
        print('Opc #1 -- Ingresar Deporte')
        print('Opc #2 -- Eliminar Deporte')
        print('Opc #3 -- Submenu  Deporte')
        print('Opc #4 -- Salir')
        print('\n---------------------------------------------------------------------------------\n')
        opc = int(input('Ingrese la opcion: '))
        print('\n---------------------------------------------------------------------------------\n')
        if opc == 1: 
            ValidarInsertarDeporte()
        if opc == 2:
            ValidarEliminarDeporte()
        if opc == 3:
            Menu2()
        if opc == 4:
            print('\n---------------------------------------------------------------------------------')
            print('----------------------------- Fin Del Programa ----------------------------------')
            print('---------------------------------------------------------------------------------\n')
            exit()
        break


#-----------------------------------------------------------------------
#   VALIDAR SUBMENU


def Menu2():
    while True:
        print('\n---------------------------------------------------------------------------------')
        print('Bienvenidos al SUBMENU')
        print('---------------------------------------------------------------------------------\n')
        print('\n---------------------------------------------------------------------------------')
        print('----------------------------- Menu De Opciones ----------------------------------')
        print('---------------------------------------------------------------------------------\n')
        print('Opc #1 -- Informacion completa de todos los deportes')
        print('Opc #2 -- Informacion de un deporte')
        print('Opc #3 -- Informacion segun lugar')
        print('Opc #4 -- Salir al menu General')
        print('\n---------------------------------------------------------------------------------\n')
        opc = int(input('Ingrese la opcion: '))
        print('\n---------------------------------------------------------------------------------\n')
        if opc == 1: 
            InformacionCompleta()
        if opc == 2:
            InformacionUnDeporte()
        if opc == 3:
            InformacionSegunLugar()
        if opc == 4:
            Menu()
        break    