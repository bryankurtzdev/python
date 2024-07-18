num = cont = soma =0
num = int(input('Digite um numero: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um numero: '))
print(f'soma dos numeros foi de {soma}')
print(f'No total voce digitou {cont}')
