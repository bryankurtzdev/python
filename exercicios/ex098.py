def contador():
    print()
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.5)


def cabecalho():
    print('-='*30)


from time import sleep
cabecalho()
print('Contagem de 1 ate 10 em 1 em 1.')
for c in range(1, 11):
    print(c, end=' ')
    sleep(0.5)
print()
cabecalho()
print('Contagem de 10 ate 0 de 2 em 2')
for c in range(10, -1, -2):
    sleep(0.5)
    print(c, end=' ')
print()
cabecalho()
print('Agora e sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
cabecalho()
contador()
