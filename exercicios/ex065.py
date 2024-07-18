r = 's'
soma = quant = media = maior = menor = 0
while r in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior > num
        if num < menor:
            menor = num
    r = str(input('Quer continuar? [N/S] '))
media = soma / quant
print(f'Voce digitou {quant} numeros e a media foi {media}')
print(f'O maior numero foi {maior} e o menor foi {menor}')
