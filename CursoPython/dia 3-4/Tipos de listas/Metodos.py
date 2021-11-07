# dict sirve para convertir una lista en diccionario 

D = dict(Nombre = 'Manuel', Apellido = 'Lopez', Edad = 17, Padres = ['Manuel', 'Ruth'])
print('\n--------------------------------------------------------------------------------')
print(D)
print('--------------------------------------------------------------------------------')

# Mostrar tipo de elemento con type
print('\n--------------------------------------------------------------------------------')
print(type(D['Nombre']))
print('--------------------------------------------------------------------------------')

# zip funciona auto emparejar los valores y llaves en un diccionario

Z = dict(zip('abcd', [1, 2, 3, 4]))
print('\n--------------------------------------------------------------------------------')
print(Z)
print('--------------------------------------------------------------------------------')

# zip tambien sirve para definiciones fuera de linea

Keys = 'key1', 'Key2'
Valores = 1, 2
print('\n--------------------------------------------------------------------------------')
print(dict(zip(Keys, Valores)))
print('--------------------------------------------------------------------------------')