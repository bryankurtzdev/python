v = float(input('Quantos KM de distancia esta o seu destino? '))
if v <= 200:
    v = v*0.50
    print(f'Sua viagem vai custar R${v:.2f}')
else:
    v = v*0.45
    print(f'Sua viagem vai custar R${v:.2f}')