from collections import Counter
'''
Num = [1,2,3,1,2,5]
Var = 'Python'

print(Counter(Var))

print(Counter(Num))
'''

Frase = 'Hola Mundo Hola Python'
C = Counter(Frase.split())

print(C.most_common())
print(C.most_common(1))
print(C.most_common(2))
print(C.most_common(3))
