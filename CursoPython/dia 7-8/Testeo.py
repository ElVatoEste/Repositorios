Red = '\033[91m'
Green = '\033[92m'
Yellow ='\033[93m'
Blue = '\033[94m'
Magenta = '\033[95m'
Cyan = '\033[96m'
White = '\033[97m'
Black = '\033[90m'
Gray = '\033[98m'


Trabajadores = {
    'Manuel' : {'Nombre': 'Manuel','Edad': 17, 'Salario': 10},
    'Pedro' : {'Nombre': 'Pedro', 'Edad': 20, 'Salario': 200}}

for x in Trabajadores:
    print(Trabajadores[x]['Nombre'])