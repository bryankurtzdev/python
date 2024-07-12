km = int(input('Quantos Km/h voce esta? '))
if km <= 80:
    print('Voce esta dentro das regras!')
else:
    mult = (km - 80)*7
    print('Voce esta acima da velocidade! ')
    print(f'Sua multa foi de R${mult:.2f}')
    