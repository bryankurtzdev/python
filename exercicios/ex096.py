def area():
    print(f'A area de um terreno {lar}x{comp} e de {soma:.2f}m quadrados.')


print('     controle de terrenos    ')
print('-'*30)
lar = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
soma = lar * comp
area()