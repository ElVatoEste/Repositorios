
import time

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
time.sleep(0.3)
print('⬛   ** C A R T E L E R A **  ⬛')
time.sleep(0.3)
print('⬛                            ⬛')
time.sleep(0.3)
print(f'⬛      Pelicula: {Pelicula}       ⬛')
time.sleep(0.3)
print(f'⬛     Tanda: {Hora}       ⬛')
time.sleep(0.3)
print(f'⬛   Combo: {Combo}   ⬛')
time.sleep(0.3)
print(f'⬛     Precio combo: {P_Combo}      ⬛')
time.sleep(0.3)
print(f'⬛    Precio entrada: {Ticket}     ⬛')
time.sleep(0.3)
print('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛')
time.sleep(1)
print('\n-----------------------------------')
time.sleep(2)

# Peticion de datos

C_Tickets = int(input('\nIngrese la cantidad de entradas que desea llevar: '))
time.sleep(1)
C_Combo = int(input('Ingrese la cantidad de combos que desea llevar: '))
time.sleep(1)
Nombre = str(input('Ingrese el nombre al cual desea la factura: '))
time.sleep(2)

print('\n-----------------------------------')
time.sleep(3)
# Operaciones

T_Combo = C_Combo*P_Combo
T_Ticket = C_Tickets*Ticket


print('\n-----------------------------------\n')
time.sleep(2)
# Dato final

T_Paga = T_Combo + T_Ticket

# Recibo

print('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛')
time.sleep(0.3)
print('⬛      ** R E C I B O **     ⬛')
time.sleep(0.3)
print('⬛                            ⬛')
time.sleep(0.3)
print(f'       Factura de {Nombre}       ')
time.sleep(0.3)
print('⬛                            ⬛')
time.sleep(0.3)
print(f'⬛       Pelicula: {Pelicula}      ⬛')
time.sleep(0.3)
print(f'⬛      Tanda: {Hora}      ⬛')
time.sleep(0.3)
print('⬛                            ⬛')
time.sleep(0.3)
print(f'      Monto Total C$ {T_Paga}    ')
time.sleep(0.3)
print('⬛                 VatoCinemas⬛')
time.sleep(0.3)
