lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = terc = maior = 0
for c in range(0, 3):
    for b in range(0, 3):
        lista[c][b] = int(input(f'Digite um valor para a [{c}, {b}]: '))
        if lista[c][b] % 2 == 0:
            par += lista[c][b]
        if b == 2:
            terc += lista[c][b]
        if c == 0:
            maior = lista[1][b]
        elif lista[1][b] > maior:
            maior = lista[1][b]
print('-='* 30)
for c in range(0, 3):
    for b in range(0, 3):
        print(f'[{lista[c][b]:^5}]', end='')
    print()
print('-='* 30)
print(f'A soma dos valores pares e de {par}.')
print(f'A soma dos valores da terceira coluna e {terc}.')
print(f'O maior valor da segunda linha e {maior}.')
