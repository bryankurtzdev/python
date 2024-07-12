
p = float(input('Qual o seu peso? [KILOS] '))
a = float(input('Qual a sua altura? [METROS] '))
imc = p / (a**2)

print(f'O seu IMC e de {imc:.1f}')
if imc < 18.5:
    print('Voce esta abaixo do peso.')
elif imc <= 18.5 or imc < 25:
    print('Voce esta no peso ideal.')
elif imc <= 25 or imc < 30:
    print('Voce esta sobrepeso.')
elif imc <= 30 or imc < 40:
    print('Voce esta Obeso.')
else:
    print('Voce esta com obesidade morbida, cuidado!')

