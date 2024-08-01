lista = list()
r = ''
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()
    if r not in 'SN':
        print('O valor digitado esta incorreto. Digite novamente.')
        r = str(input('Quer continuar? [S/N] ')).upper().strip()
        if r == 'N':
            break
print(f'N total foram digitados {lista.__len__()}')
print(f'A lista e ordem decrescente fica {lista.sort(reverse=True)}')
print(f'')