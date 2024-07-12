from random import randint
from time import  sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('=+'*20)
print('''Suas opcaoes:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual e a sua jogada? '))
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO!!')
print(f'Computador jogou {itens[computador]}')
print(f'Voce jogou {itens[jogador]}')
print('=+'*20)
if computador == 0:
    if  jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Voce GANHOU!')
    elif jogador == 2:
        print('Computador GANHOU!')
    else:
        print('Jogada invalida!')
elif computador == 1:
    if jogador == 0:
        print('Computador GANHOU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Voce GANHOU!')
    else:
        print('Jogada invalida!')
elif computador == 2:
    if jogador == 0:
        print('Voce GANHOU!')
    elif jogador == 1:
        print('Computador GANHOU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada Invalida!')