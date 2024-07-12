s = ''
while s != 'M' and s != 'F':
    s = str(input('Digite seu sexo [M/F]: ')).upper()
    if s != 'M' and s != 'F':
        print('O valor esta incorreto, por favor revise!')
    elif s == 'M' or s == 'F':
        print('Registrado!')
print('Fim')