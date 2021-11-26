'''
Realizar un programa que solicite una temperatura en grados Fahrenheit y convierta el
resultado a grados Celsius.
Para realizar el algoritmo se ha de utilizar la siguiente formula:
Centigrados = ( 5/9 ) * ( Grados Fahrenheit – 32 )

'''
print('\n---------------------------------------------------')
print('  Bienvenido al sistema de medidas de temperatura')
print('---------------------------------------------------\n')

y_n = ['Y', 'N', 'n', 'y']

while True:
    print('Seleccione la medida a la que se desea convertir: ')
    print('1. Grados centigrados a Fahreheit\n2. Grados Fahreheit a Centigrados')
    
    Opcion = int(input('Ingrese opción: '))
    
    while Opcion != 1 and Opcion != 2:
            print('\n-----------------------------------------')
            print('           Caracter no valido')
            print('-----------------------------------------\n')
            print('1. Grados centigrados a Fahreheit\n2. Grados Fahreheit a Centigrados')
            Opcion = int(input('Ingrese opción: '))
    
    if Opcion == 1:
        GradosC = float(input('\nIngrese la cantidad de Grados Centigrados que desea convertir: '))
        GradosF = (GradosC*9/5)+32
        print(f'{GradosC}ºC son {GradosF}ºF')
    else:
        GradosF = float(input('\nIngrese la cantidad de Grados Centigrados que desea convertir: '))
        GradosC = (GradosF-32)*5/9
        print(f'\n{GradosF}ºF son {GradosC}ºC')
    
    Salida = input('\n¿Desea salir del sistema? y/n: ')
    while Salida not in y_n:
        print('\n-----------------------------------------')
        print('           Caracter no valido')
        print('-----------------------------------------')
        Salida = input('\n¿Desea salir del sistema? y/n: ')

    if Salida == 'y' or Salida == 'Y':
        print('\nMuchas gracias por usar nuestro sistema de medidad')
        print('             !! Vuelva pronto ¡¡\n')
        exit()
