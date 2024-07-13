resposta = 0

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
while resposta != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair dp programa''')
    resposta = int(input('Opcao escolhida: '))
    if resposta == 4:
        while resposta != 5:
            n1 = float(input('Digite um valor: '))
            n2 = float(input('Digite outro valor: '))
            print('''
            [1] somar
            [2] multiplicar
            [3] maior
            [4] novos numeros
            [5] sair dp programa''')
            resposta = int(input('Opcao escolhida: '))
        if resposta == 1:
            print(f'A soma de {n1} com {n2} e {n1 + n2}')
        elif resposta == 2:
            print(f'{n1} x {n2} e igual a {n1*n2}')
        elif resposta == 3:
            maior = n1
            if n2 > maior:
                maior = n2
            print(f'O maior numero entre os dois e {maior:.1f}')

