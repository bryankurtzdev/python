nome = str(input('Escreva seu nome completo: ')).strip()
nomediv = nome.split()

print('nome em maiusculas', nome.upper())
print('nome em minusculas', nome.lower())
print('letras ao todo', len(nome) - nome.count(" "))
print(f'o primeiro nome tem {len(nomediv[0])} letras')
