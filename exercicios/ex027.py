n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()

print('Muito Prazer em te conhecer!')
print(f'Seu primeiro nome e {nome[0]}')
print(f'Seu ultimo nome e {nome[len(nome)-1]}')
