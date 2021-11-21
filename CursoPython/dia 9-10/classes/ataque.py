class ataque:
    def __init__(self, ip, puerto):
        self.ip = ip
        self.puerto = puerto
    def Mostrar(self):
        while True:
            print(f'ataque al host {self.ip} en el puerto {self.puerto}')
            print('Warning Infected')
A = ataque('10.220.32', 5023)
A.Mostrar()