s = 0
c = 0
for c in range(0, 6):
    n = int(input('Digite um numero: '))
    if n%2 == 0:
        s += n
        c += 1
print(f'Voce informou {c} numeros e a soma dos numeros pares foi {s}')