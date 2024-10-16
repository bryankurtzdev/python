from random import randint
from time import sleep

def quente_ou_frio(numero_jogado, numero_sorteado):
    if numero_jogado < numero_sorteado:
        print(f'O numero {numero_jogado} e menor que o numero sorteado.')
    elif numero_jogado > numero_sorteado:
        print(f'O numero {numero_jogado} e maior que o numero jogado')


nome = str(input('Digite seu nome: ')).upper()
comeco = 1
c = 0
jogada = 0
totrodadas = 0
if nome == 'LUANNE':
    nome = 'Tetinha'
elif nome == 'BRYAN':
    nome = 'Mestre'
print(f'Ola, seja bem-vindo {nome}')
print('------------ DIFICULDADE ------------')
print('''
[1] facil
[2] medio
[3] dificil
[4] impossivel
[5] !!INFERNO!!''')
print('-------------------------------------')
numero = int(input('Resposta: '))
if numero == 1:
    sorteio = randint(1, 5)
    fim = 5
elif numero == 2:
    sorteio = randint(1, 10)
    fim = 10
elif numero == 3:
    sorteio = randint(1, 100)
    fim = 100
elif numero == 4:
    print('Voce e ousado!')
    sorteio = randint(1, 1000)
    fim = 1000
elif numero == 5:
    print('Acha mesmo que consegue me vencer?')
    print('Essa dificuldade e quase impossivel de acertar!')
    print('Voce precisara acertar um numero no meio de 1 trilhao!!')
    print('--'*20)
    sorteio = randint(1, 1000000000000)
    fim = 1000000000000

print('Pensando...')
sleep(1)
print(f'voce precisa acertar o numero sorteado que esta entre {comeco} e {fim}')
if numero == 5:
    print('Como voce escolheu esta dificuldade voce so tera 3 chances de acertar.')
    for c in range(1, 4):
        jogada = int(input('Digite o numero que voce acha que eu pensei: '))
        
        if jogada == sorteio:
            print('impossive-')
            print('Como voce acertou!?')
            print('Aparentemente voce e um escolhido, peco desculpas por ser grosso.')
        else:
            print('Eu lhe disse que era quase impossivel!')
            print('Tente novamente, talvez em alguns anos tentando voce consegue...')
        quente_ou_frio(jogada, sorteio)
if numero == 4:
    print('Como voce escolheu esta dificuldade voce so tera 10 chances de acertar.')
    for c in range(1, 11):
        jogada = int(input('Digite o numero que voce acha que eu pensei: '))
        if jogada == sorteio:
            print('Caramba!')
            print('Como voce acertou!?')
            print('Voce tem MUITA sorte!')
        else:

            print('Tente novamente, talvez em alguns dias tentando voce consegue...')
        quente_ou_frio(jogada, sorteio)

if numero == 3:
    print('Como voce escolheu esta dificuldade voce so tera 50 chances de acertar.')
    for c in range(1, 51):
        jogada = int(input('Digite o numero que voce acha que eu pensei: '))
        if jogada == sorteio:
            print('Voce acertou!')
            print('tens sorte!')
        else:

            print('Tente novamente, talvez em algumas horas tentando voce consegue...')
        quente_ou_frio(jogada, sorteio)

if numero != 5 and numero != 4 and numero != 3:
    while jogada != sorteio:
        jogada = int(input('Digite o numero que voce acha que eu pensei: '))
        if jogada == sorteio:
            totrodadas += 1
            print('Parabens!')
            if totrodadas == 1:
                print(f'Voce acertou o numero que eu pensei de primeira!')
            else:
                print(f'Voce acertou o numero que eu pensei em {totrodadas} tentativas!')
        else:
            totrodadas += 1
            print('Errou, tente novamente!')
        quente_ou_frio(jogada, sorteio)
print('Fim...')
