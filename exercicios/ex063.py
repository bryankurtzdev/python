n = int(input('Quantidade de termos: '))
n1 = 0
n2 = 1
n3 = 0
tottermos = 0
while tottermos < n:
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    tottermos += 1
    print(' - ', n2, end=' ')