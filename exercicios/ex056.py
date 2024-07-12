somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print(f'------ {c} PESSOA ------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print(f'A media de idade do grupo e de {mediaidade} anos')
print(f'O homem mais velho se chama {nomevelho} e tem {maioridade} anos de idade.')
print(f'Ao todo sao {totmulher20} mulheres com menos de 20 anos')
