from random import shuffle
a1 = str(input('Primeiro aluno: '))
a2 = str(input('segundo aluno: '))
a3 = str(input('terceiro alino: '))
a4 = str(input('quarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print(' a ordem de apresentacao sera ')
print(lista)