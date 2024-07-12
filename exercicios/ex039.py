idd = int(input('Qual a sua idade? '))

if idd < 18:
    print('Voce ainda vai se alistar ao servico militar. ')
elif idd == 18:
    print('Esta na hora de voce se alistar  ao exercito!')
else:
    print('Voce ja passou da idade para o alistamento obrigatorio!')