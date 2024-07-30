num = (int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')))
print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 2 in num:
    print(f'P valor 3 apareceu na posicao {num.index(3)}')
else:
    print(f'O valor 3 nao foi digitado em nenhuma posicao ')
print('Os valores pares digitados foram ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
