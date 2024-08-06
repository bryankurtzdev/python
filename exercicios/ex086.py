lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for b in range(0, 3):
        lista[c][b] = int(input(f'Digite um valor para a [{c}, {b}]: '))
print('-='* 30)
for c in range(0, 3):
    for b in range(0, 3):
        print(f'[{lista[c][b]:^5}]', end='')
    print()
