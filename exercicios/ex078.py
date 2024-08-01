menor = maior = 0
lista = list()
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posicao {cont}: ')))
    if cont == 0:
        maior = lista[cont]
        menor = lista[cont]
    if lista[cont] > maior:
        maior = lista[cont]
    if lista[cont] < menor:
        menor = lista[cont]
print('=-'*30)
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posicoes ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f' {i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posicoes ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f' {i}...', end='')
print()
