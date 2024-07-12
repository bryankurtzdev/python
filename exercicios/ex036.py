imp = float(input('Valor da Casa: R$'))
sal = float(input('Salario: R$'))
anos = int(input('Quantos anos de financiamento? '))
cont = imp / (anos * 12)
por = sal * 30 / 100

print(f'Para pagar uma casa de R${imp:.2f} em {anos} anos a prestacao sera de R${cont:.2f}')
if por < cont:
    print('Eprestimo ACEITO!')
else:
    print('Emprestimo NEGADO!')





