mais18 = homens = mulheresmenos20 = 0

while True:
    print('---'*20)
    print('CADASTRE UMA PESSOA')
    print('---'*20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:
        mais18 += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F':
        if idade < 20 :
            mulheresmenos20 += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Total de pessoascom mais de 18 anos: {mais18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheresmenos20} mulheres com menos de 20 anos')
