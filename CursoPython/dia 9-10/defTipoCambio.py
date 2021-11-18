def Menu():
    print('\nQue desea cambiar: ')
    print('1- C$ - $')
    print('2- C$ - €')
    Cambio = int(input(''))
    if Cambio == 1:
        print('\n')
        Dolar()
    elif Cambio == 2:
        print('\n')
        Euro()
    else:
        print('\nHasta la proxima...\n')
        exit()

def Dolar():
    print('** Menu de opciones **')
    print('1- Coordoba a Dolar')
    print('2- Dolar a Coordoba')
    Ask = int(input())
    if Ask == 1:
        print('\n-------------------------------------------------------------------')
        Num1 = float(input('Ingrese la cantidad de coordobas que desea convertir: '))
        print('-------------------------------------------------------------------\n')
        CoorDolar =  Num1 * 0.028
        print(f'C${Num1} son aproximadamente ${CoorDolar:.2f}')
    elif Ask == 2:
        print('\n-------------------------------------------------------------------')
        Num1 = float(input('Ingrese la cantidad de dolares que desea convertir: '))
        print('-------------------------------------------------------------------\n')
        CoorDolar =  Num1 * 35.25
        print(f'${Num1} son aproximadamente C${CoorDolar:.2f}')
    else:
        print('Numero invaldido')

def Euro():
    print('** Menu de opciones **')
    print('1- Coordoba a Euro')
    print('2- Euro a Coordoba')
    Ask = int(input())
    if Ask == 1:
        print('\n-------------------------------------------------------------------')
        Num1 = float(input('Ingrese la cantidad de coordobas que desea convertir: '))
        print('-------------------------------------------------------------------\n')
        CoorEuro =  Num1 * 0.025
        print(f'C${Num1} son aproximadamente €{CoorEuro:.2f}')
    elif Ask == 2:
        print('\n-------------------------------------------------------------------')
        Num1 = float(input('Ingrese la cantidad de euros que desea convertir: '))
        print('-------------------------------------------------------------------\n')
        CoorEuro =  Num1 * 39.91
        print(f'€{Num1} son aproximadamente C${CoorEuro:.2f}')
    else:
        print('\nNumero invaldido...')

print('\n*************************************')
print('** Bienvenido al sistema de cambio **')
print('*************************************\n')

while True:
    Menu()
