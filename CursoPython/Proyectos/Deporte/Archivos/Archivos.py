from Datos.deporte import *

#-----------------------------------------------------------------------
#   MOSTRAR DATOS GUARDADOS


def MostrarDeporte():
    if len(Deportes) == 0:
        print('No Existe Registro') 
    else:
        print('------------------------------------------')
        print('DEPORTES EXISTENTES')
        print('------------------------------------------')
        for D in Deportes:
            print(D,' --- ',Deportes[D]['Nombre'])
            print('------------------------------------------')
        pass
    pass
pass

