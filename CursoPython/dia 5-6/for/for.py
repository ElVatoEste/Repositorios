# Semana =  ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']

#for x in Semana:
#    print(x)
#    if x == 'Miercoles':
#        print('Encontre')
    
# Primer ejecicio

Cantidad = int(input('Digite la cantidad de persona: '))

Nombre=[]
Salario=[]
for x in range(Cantidad):
    Nom=str(input('Ingrese su nombre: '))
    Nombre.append(Nom)
    Sueldo=float(input('Ingrese su salario: '))
    Salario.append(Sueldo)

i = 0
for i in range(Cantidad):
    print(Nombre[i],Salario[i] )
    