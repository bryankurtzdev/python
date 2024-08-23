from time import sleep
def maior(* num):
    cont = maior = 0
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end=' ')
        sleep(0.3)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior=valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


maior(9, 3, 5, 12, 5, 123, 1)
maior(-1, -6, 0)
maior(5, 6, 1, 3, 5, 6, 7, 21)
maior()