n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2
print(f'Sua media foi de {m:.1f}')
if m >=6:
    print('Parabens! Voce esta acima da media')
else:
    print('Voce esta abaixo da media! Estude mais!')
