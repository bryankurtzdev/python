from exercicios.ex109 import moeda

p = float(input('Digite o preco: R$'))
print(f'A metade de {moeda.moeda(p)} e {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} e {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.reduzindo(p, 13, True)}')
