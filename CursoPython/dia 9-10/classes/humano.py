class humano():
    def __init__(self, edad, nombre, ocupacion):
        self.edad = edad
        self.nombre = nombre
        self.ocupacion = ocupacion
    def Presentar(self):
        presentar = ('Hola soy {}, mi edad es {} y mi ocupacion es {}')
        print(presentar.format(self.nombre, self.edad, self.ocupacion))
    def Contratar(self, puesto):
        self.puesto = puesto
        print('{} fua contratado como {}'.format(self.nombre, self.puesto))
        self.ocupacion = puesto

P = humano(31, 'Pedro', 'Desocupado')

P.Presentar()
P.Contratar('Obrero')
P.Presentar()

