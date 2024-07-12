n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

if m < 5:
    print('Voce esta reprovado!')
elif 7 > m >= 5:
    print('Voce esta de recuperacao')
elif 7 <= m:
    print('PARABENS, Voce esta aprovado!')
