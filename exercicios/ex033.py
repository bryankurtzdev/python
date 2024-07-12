a: int = int(input('Digite o valor 1: '))
b = int(input('Digite o valor 2: '))
c = int(input('Digite o valor 3: '))
menor = a

if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f'O menor numero e {menor}')
print(f'O maior numero e {maior}')