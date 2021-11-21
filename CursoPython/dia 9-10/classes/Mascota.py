class Mascota():
    def __init__(self):
        self.Nombre = str(input('Cual es el nombre de la mascota: '))
        self.Edad = int(input('Cual es la edad de la mascota: '))

    def MostrarDatos(self):
        print(f'\nNombre {self.Nombre} \nEdad: {self.Edad}\n')

m = Mascota()
m.MostrarDatos()