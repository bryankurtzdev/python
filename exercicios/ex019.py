from random import choice
a1 = str(input('Primeiro aluno: '))
a2 = str(input('segundo aluno: '))
a3 = str(input('terceiro alino: '))
a4 = str(input('quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)

print(f'o aluno escolhido foi {escolhido}')
