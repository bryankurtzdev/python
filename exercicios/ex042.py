print('=*=' * 20)
print('Analisador de segmentos')
print('=*=' * 20)

r1 = float(input('Escreva o primeiro segmento: '))
r2 = float(input('Escreva o segundo segmento: '))
r3 = float(input('Escreva o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('ISOCELES!')
    else:
        print('ESCALENO!')
else:
    print('Os segmentos acima NAO PODEM FORMAR um triangulo.')
