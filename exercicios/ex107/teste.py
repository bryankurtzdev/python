from exercicios.ex107 import moeda

p = float(input('Digite o preco: R$'))
print(f'A metade de {p} e R${moeda.metade(p)}')
print(f'O dobro de {p} e R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos R${moeda.reduzindo(p, 13)}')
