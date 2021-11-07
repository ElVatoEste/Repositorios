<<<<<<< HEAD
# Primer Mensaje
print('\n\n  **Bienvenido a VatoCinemas**\n')

#Datos

Pelicula = str('Venom')
Ticket = int(100)
Hora = str('6pm - 8pm')
Combo = str ('Bebida + Nachos')
P_Combo = int(150)

# Cartelera

print('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛')
print('⬛   ** C A R T E L E R A **  ⬛')
print('⬛                            ⬛')
print(f'⬛      Pelicula: {Pelicula}       ⬛')
print(f'⬛     Tanda: {Hora}       ⬛')
print(f'⬛   Combo: {Combo}   ⬛')
print(f'⬛     Precio combo: {P_Combo}      ⬛')
print(f'⬛    Precio entrada: {Ticket}     ⬛')
print('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛')
print('\n-----------------------------------')

# Peticion de datos

C_Tickets = int(input('\nIngrese la cantidad de entradas que desea llevar: '))
C_Combo = int(input('Ingrese la cantidad de combos que desea llevar: '))
Nombre = str(input('Ingrese el nombre al cual desea la factura: '))
print('\n-----------------------------------')

# Operaciones

T_Combo = C_Combo*P_Combo
T_Ticket = C_Tickets*Ticket

print('\n-----------------------------------\n')
# Dato final

T_Paga = T_Combo + T_Ticket

# Recibo

print('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛')
print('⬛      ** R E C I B O **     ⬛')
print('⬛                            ⬛')
print(f'      Factura de {Nombre}     ')
print('⬛                            ⬛')
print(f'⬛       Pelicula: {Pelicula}      ⬛')
print(f'⬛      Tanda: {Hora}      ⬛')
print('⬛                            ⬛')
print(f'      Monto Total C$ {T_Paga}    ')
print('⬛                 VatoCinemas⬛')
print('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛')

=======
# Primer Mensaje
print('\n\n  **Bienvenido a VatoCinemas**\n')

#Datos

Pelicula = str('Venom')
Ticket = int(100)
Hora = str('6pm - 8pm')
Combo = str ('Bebida + Nachos')
P_Combo = int(150)

# Cartelera

print('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛')
print('⬛   ** C A R T E L E R A **  ⬛')
print('⬛                            ⬛')
print(f'⬛      Pelicula: {Pelicula}       ⬛')
print(f'⬛     Tanda: {Hora}       ⬛')
print(f'⬛   Combo: {Combo}   ⬛')
print(f'⬛     Precio combo: {P_Combo}      ⬛')
print(f'⬛    Precio entrada: {Ticket}     ⬛')
print('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛')
print('\n-----------------------------------')

# Peticion de datos

C_Tickets = int(input('\nIngrese la cantidad de entradas que desea llevar: '))
C_Combo = int(input('Ingrese la cantidad de combos que desea llevar: '))
Nombre = str(input('Ingrese el nombre al cual desea la factura: '))
print('\n-----------------------------------')

# Operaciones

T_Combo = C_Combo*P_Combo
T_Ticket = C_Tickets*Ticket

print('\n-----------------------------------\n')
# Dato final

T_Paga = T_Combo + T_Ticket

# Recibo

print('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛')
print('⬛      ** R E C I B O **     ⬛')
print('⬛                            ⬛')
print(f'      Factura de {Nombre}     ')
print('⬛                            ⬛')
print(f'⬛       Pelicula: {Pelicula}      ⬛')
print(f'⬛      Tanda: {Hora}      ⬛')
print('⬛                            ⬛')
print(f'      Monto Total C$ {T_Paga}    ')
print('⬛                 VatoCinemas⬛')
print('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛')

>>>>>>> 186abf19ab9f2a79d2746b5b473d7784ac388d12
