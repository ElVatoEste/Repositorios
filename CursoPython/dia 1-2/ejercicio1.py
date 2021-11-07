# Primer Mensaje
print('--------------------')
print('     Bienvenido!')
print('--------------------')

# Datos a usar

Dias = 7
Horas = 6
Salario = 2100 # Salario semanal

# Operaciones internas

Horas_semanales = Horas*Dias
Salario_Hora = Salario/Horas_semanales

# Mensaje en la consola

print(f'\nEl obrero trabaja un total de {Horas_semanales} a la semana')
print(f'El obrero gana a la semana un total de {Salario} coordobas a la semana')
print(f'Gana por hora {Salario_Hora} coordobas')