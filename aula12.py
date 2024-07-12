nome = str(input('Qual e seu nome? ')).strip().lower()
if nome == 'gustavo':
    print('Que nome lindo o seu! ')
elif nome == 'bryan' or nome == 'august' or 'libano':
    print('Seu nome e bem diferente!')
elif nome in 'juliana claudia jormungarder faxineira':
    print('Seu nome e LENDARIO! ')
else:
    print('Seu nome e bem normal! ')
print(f'Tenha um bom dia {nome}')