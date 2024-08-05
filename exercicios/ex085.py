numeros = impares = pares = list()
for c in range(1, 8):
    n = int(input(f'Digite o {c}o. valor: '))
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 != 0:
        impares.append(n)
numeros.append(impares)
numeros.append(pares)
print(numeros)
