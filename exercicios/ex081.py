lista = list()
r = ''
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()
    if r not in 'SN':
        while r not in 'SNsn':
            print('O valor digitado esta incorreto. Digite novamente.')
            r = str(input('Quer continuar? [S/N] ')).upper().strip()
    if r in 'Nn':
        break
print(f'No total foram digitados {len(lista)} numeros')
lista.sort(reverse=True)
print(f'A lista e ordem decrescente fica {lista}')
if 5 in lista:
    print(f'O valor cinco esta na lista')
else:
    print('O valor 5 nao esta na lista!')
