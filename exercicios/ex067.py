while True:
    tabuada = int(input('quer ver a tabuada de qual valor? '))
    if tabuada < 0:
        break
    for c in range(1, 11):
        print(f'{tabuada} x {c} = {tabuada*c}')
print('Programa de tabuada encerrado. Volte sempre!')
