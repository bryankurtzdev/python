import math
c1 = float(input('Digite o comprimento do cateto oposto: '))
c2 = float(input('Digite o comprimento do cateto adjacente: '))
h = math.sqrt((c1**2) + (c2**2))

print(f'o valor de hipotenusa e igual a {h}')