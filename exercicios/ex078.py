maior = maior = 0
posmenor = posmaior = lista = list()
for cont in range(0, 6):
    lista.append(int(input(f'Digite um valor para a posicao {cont}: ')))
    if cont == 1:
        maior = lista[cont]
        menor = lista[cont]
        pos = cont
    if lista[cont] > maior:
        maior = lista[cont]
        posmaior.append(cont)
    if lista[cont] < menor:
        menor = lista[cont]
        posmenor.append(cont)
print(maior, posmaior)
print(menor, posmenor)
