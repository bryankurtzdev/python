soma = caro = menor = cont = 0
barato = ' '
print('---'*20)
print('Loja Super Baratao')
print('---'*20)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preco do produto: '))
    cont += 1
    soma += preco
    if preco > 1000:
        caro += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [N/S] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'O total gasto foi de R${soma:.2f}')
print(f'no total voce comprou {caro} produtos acima de R$1000')
print(f'O produto mais barato foi o {barato} que custou R${menor:.2f}')