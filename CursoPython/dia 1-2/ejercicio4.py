# Primer Mensaje
print('--------------------')
print('     Bienvenido!')
print('--------------------')

# Datos a usar

Total_clases = int(input('¿Cuantas clases tienes?:'))
Clases_Aprovadas = int(input('¿Cuantas clases aprobastes?: '))

# Operaciones internas

Promedio = Clases_Aprovadas*100/Total_clases # Operacion de Promedio  
Promedio_negativo =100-Promedio

# Mensaje en la consola
print('\n------------------------------------------------------------')
print(f'El Promedio de clases aprobadas es: {Promedio}%')
print(f'El Promedio de clases reprobadas es: {Promedio_negativo}%')
print('------------------------------------------------------------')