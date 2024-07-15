from math import factorial
n = int(input('Escreva um numero: '))
c = n
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(factorial(n))
