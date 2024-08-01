lista = list()
while True:
    n = int(input('Digite um valor para coloca-lo na lista: '))
    if n not in lista:
        lista.append(n)
        print('Valor adcionado com sucesso! ')
    else:
        r = str(input('Quer continuar? [S/N] ')).upper().strip()
    if r == 'N':
        break
lista.sort()
print(lista)
