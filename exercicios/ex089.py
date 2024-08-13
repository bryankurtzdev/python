ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = str(input('Nota 1: '))
    nota2 = str(input('Nomta 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('uer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='* 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{1:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'* 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando... ')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
