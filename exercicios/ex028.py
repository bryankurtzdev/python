from random import randint
n = randint(0,10)
print('-+-+-' * 20)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('-+-+-' * 20)
jo = int(input('Escolha um numero entre 0 e 10: '))

print('Pensando...')
if jo == n:
    print('Parabens voce acertou o numero que eu pensei!!')
else:
    print('Voce nao acertou o numero! tente novamente. ')
    print(f'Eu tinha pensado no numero {n}')