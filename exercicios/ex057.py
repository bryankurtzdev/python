s = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while s not in 'MmFf':
    s = str(input('Dados invalidos. Por favor, informe seu sexo [M/F]: ')).upper().strip()[0]
print('Registrado!')
