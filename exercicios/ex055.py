mpesado = 0
mleve = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c} pessoa: '))
    if c == 1:
        mpesado = peso
        mleve = peso
    else:
        if peso > mpesado:
            mpesado = peso
        if peso < mleve:
            mleve = peso
print(f'O maior peso lido foi de {mpesado}KG')
print(f'O menor peso lido foi de {mleve}KG')
