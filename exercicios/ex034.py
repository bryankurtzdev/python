s = float(input('Digite o valor do seu salario: '))
sp = 0
if s <= 1250.00:
    sp = (15/100)*s
    s = s + sp
    print(f'Seu novo salario e de {s:.2f}')
else:
    sp = (10/100)*s
    s = s + sp
    print(f'Seu novo salario e de {s:.2f}')