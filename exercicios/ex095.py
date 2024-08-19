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
for k, v in lista.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
for c in range(0, nump):
    print(f'    => Na partida {c}, fez {gols[c]}')
print(f'Foi um total de {lista['total']}')