lista = listaimp = listapar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimp.append(n)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'NnSs':
        print('Resposta foi digitada incorretamente!')
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
print('-=-'* 30)
print(f'A lista principal ficou assim {lista}')
print(f'A lista com os numeros impares ficou assim {listaimp}')
print(f'A lista com os numeros pares ficou assim {listapar}')
