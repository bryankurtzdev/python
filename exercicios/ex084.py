lista = []
listamenor = []
listamaior = []
tot = pesado = leve = 0
r = ''
while True:
    n = str(input('Nome: '))
    p = int(input('Peso: '))
    lista.append(n)
    lista.append(p)
    tot += 1
    if p < 70:
        listamenor.append(n)
        listamenor.append(p)
    elif p > 100:
        listamaior.append(n)
        listamaior.append(p)
    r = str(input('Quer contiuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'A lista com as pessoas mais pesadas ficou {listamaior}')
print(f'A lista com as pessoas mais leves ficou {listamenor}')
