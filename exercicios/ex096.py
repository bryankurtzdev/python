def area(lar, comp):
    a = lar * comp
    print(f'A area de um terreno {lar}x{comp} e de {a}m quadrados.')


print('     controle de terrenos    ')
print('-'*30)
lar = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(lar, comp)
