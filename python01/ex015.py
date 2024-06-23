km=float(input('Digite a quantidade de KM rodados com o carro: '))
dia=int(input('Digite a quantidade de dias que voce ficou com o carro: '))
vlf=(km*0.15)+(dia*60)

print(f'O total a pagar e de R${vlf:.2f}')