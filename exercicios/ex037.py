n = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao: 
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opcao: '))

if opcao == 1:
    print(f'{n} convertido para BINARIO e igual a {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} convertido para OCTAL e igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} convertido para HEXADECIMAL e igual a {hex(n)[2:]}')
else:
    print('Opcao INVALIDA!')
