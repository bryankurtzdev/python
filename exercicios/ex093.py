lista = {}
gols = list()
gols1 = 0
lista['nome'] = str(input('Nome do jogador: '))
nump = int(input(f'Quantas partidas {lista['nome']} jogou? '))
for c in range(0, nump):
    gol = int(input(f'Gols na partida {c}? '))
    gols1 += gol
    gols.append(gol)
lista['gols'] = gols[:]
lista['total'] = gols1
print('-='*20)
print(f'O campo nome tem o valor {lista['nome']}')
print(f'O campo gols tem o valor de {lista['gols']}')
print(f'O campo total tem o valor {lista['total']}')
print('-='*20)
for c in range(0, nump):
    print(f'    => Na partida {c}, fez {gols[c]}')
print(f'Foi um total de {lista['total']}')
