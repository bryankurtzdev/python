from random import randint
from time import sleep
n = randint(0,10)
jogada = 11
nrodadas = 0
print('-+-+-' * 20)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('-+-+-' * 20)
print('Pensando...')
sleep(1)
while n != jogada:
    jogada = int(input('Digite o numero que voca acha que eu pensei: '))
    if n == jogada:
        nrodadas += 1
        print('Parabens, Voce acertou em cheio!!!')
    else:
        nrodadas += 1
        print('Errou, tente denovo!!')
if nrodadas > 8:
    print('Demorou ein.')
elif nrodadas < 2:
    print('Voce tem sorte!')
print(f'Voce precisou de {nrodadas} para acertar o numero que eu pensei')

