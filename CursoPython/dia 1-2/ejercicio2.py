<<<<<<< HEAD
# Primer Mensaje
print('--------------------')
print('     Bienvenido!')
print('--------------------')

# Datos a usar

Dias = int(input('Cuantas dias trabaja a la semana: '))
Horas = int(input('Cuantas horas trabaja al dia: '))
Salario =  int(input('Cual es el salario semanal: ')) # Salario semanal

# Operaciones internas

Horas_semanales = Horas*Dias
Salario_Hora = Salario/Horas_semanales

# Mensaje en la consola

print(f'\nEl obrero trabaja un total de {Horas_semanales} a la semana')
print(f'El obrero gana a la semana un total de {Salario} coordobas a la semana')
=======
# Primer Mensaje
print('--------------------')
print('     Bienvenido!')
print('--------------------')

# Datos a usar

Dias = int(input('Cuantas dias trabaja a la semana: '))
Horas = int(input('Cuantas horas trabaja al dia: '))
Salario =  int(input('Cual es el salario semanal: ')) # Salario semanal

# Operaciones internas

Horas_semanales = Horas*Dias
Salario_Hora = Salario/Horas_semanales

# Mensaje en la consola

print(f'\nEl obrero trabaja un total de {Horas_semanales} a la semana')
print(f'El obrero gana a la semana un total de {Salario} coordobas a la semana')
>>>>>>> 186abf19ab9f2a79d2746b5b473d7784ac388d12
print(f'Gana por hora {Salario_Hora:.2f} coordobas')