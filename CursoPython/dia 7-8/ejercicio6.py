'''
En una tienda de computadoras se hace una promoción, donde el cliente obtiene un descuento
que depende de un número que escoge al azar. Si el número escogido es menor que 60, el 
descuento será el 30%, y si el número en mayor o igual a 60 el descuento será el 50%.
Calcular el descuento y el monto final a pagar. Solución:
Declaramos las variables correspondientes para luego ingresar los datos de entrada y
utilizar una estructura selectiva if que nos ayudara a hacer comparaciones.
por último, hacemos la operación respecto al descuento.

'''
# Importacion de la libreria random
import random

# Definir el rango del minimo y maximo de numero a optener
NumeroRandom = random.randrange(1, 100)

# Bienvenida
print('\n***********************************')
print('** Bienvenido a la tienda python **')
print('***********************************\n')

# Explicacion del sistema
print(f'Estimado cliente le notificamos que el dia de hoy estaremos\naplicando descuentos por el black friday, dependiento de su\nsuerte se le aplicara el 30% o 50% de decuento en su compra')

Nomb = str(input('\nIngrese el nombre del cliente: '))
Cantidad = float(input('Monto total a pagar: '))

# Si el numero sale igual o mayor a 6 se le aplica un descuento de 50%
if NumeroRandom >= 60:

    print('\n                 ¡¡¡¡FELICIFADES!!!')
    print('Usted a ganado el 50% porciento de descuento en su compra\n')

    # Operacion matematica 
    Total = Cantidad*0.5
    
    # use una funcion incluida en python (No la enseñaron pero busque como)
    # En entre estas esta center y format, asi sin importar el contenido de la factura
    # Se adecuara correctamente

    print('------------------------')
    print('-- Recibo a nombre de --')
    print(Nomb.center(22))
    print('------------------------')
    print('--  Cantidad a pagar  --')
    print(format(Total, '^22'))
    print('------------------------\n')

# Como caso contrario de no cumplir la condicion, se le aplicara un descuento de 30%
else:
    
    print('\nUsted a ganado el 30% porciento de descuento en su compra\n')
    
    # Operacion matematica
    Total = Cantidad*0.7

    # use una funcion incluida en python (No la enseñaron pero busque como)
    # En entre estas esta center y format, asi sin importar el contenido de la factura
    # Se adecuara correctamente

    print('------------------------')
    print('-- Recibo a nombre de --')
    print(Nomb.center(22))
    print('------------------------')
    print('--  Cantidad a pagar  --')
    print(format(Total, '^22'))
    print('------------------------\n')

print('** Gracias por su compra **')
print('       Vuelva pronto!\n')


