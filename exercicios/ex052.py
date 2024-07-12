n = int(input('Digite um numero: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}')
print(f'\n\033[mO numero {n} foi divisivel {tot} vezes')
if tot == 2:
    print(f'E por isso o {n} e primo.')
else:
    print(f'E por isso o numero {n} nao e primo.')
