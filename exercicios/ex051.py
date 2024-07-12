print('='*28)
print('10 TERMOS DE UMA PA')
print('='*28)

n = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = n + (10 - 1) * razao
for c in range(n, decimo + razao, razao):
    print(f'{c}', end=' -> ')
print('ACABOU!')