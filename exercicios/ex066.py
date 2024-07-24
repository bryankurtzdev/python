n = s = numdigitados = 0
while True:
    n = int(input('Digite um numero [999 PARA PARAR]: '))
    if n == 999:
        break
    s += n
    numdigitados += 1
print(f'A soma foi de {s}')
print(f'Voce digitou {numdigitados} numeros')
