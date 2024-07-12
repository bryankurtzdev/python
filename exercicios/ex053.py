frase = str(input('Escreva alguma frase: ')).strip().upper()
pal = frase.split()
junto = ''.join(pal)
inverso = junto[::-1]
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada nao e um palindromo!')