Series = ['Rick & Morty', 'StarWars', 'Sherk', 'Dark', 'Who?']
print(f'\n{Series}')
print('------------------------------------')
print('------------------------------------')
# Modificar
print('Dato cambiado "Sherk"')
Series[2] = 'Loki'
print(f'{Series}')
print('------------------------------------\n')

# Eliminar
print('------------------------------------')
print('Dato quitado "Rick & Morty"')
Series.remove('Rick & Morty')
print(Series)
print('------------------------------------\n')
print('------------------------------------')
# Agregar
print('Agregando "Pou"')
Series.extend(['Pou'])
print(Series)
print('------------------------------------\n')
# Agregar modificar quitar