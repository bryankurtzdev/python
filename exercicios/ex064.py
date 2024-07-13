fim = 0
totnumeros = 0
n1 = 0
while fim != 999:
    fim = int(input('Digite um numero: '))
    if fim != 999:
        n1 = fim
        soma = n1 + fim
        totnumeros += 1
print(f'soma dos numeros foi de {soma}')
print(f'No total voce digitou {totnumeros}')
