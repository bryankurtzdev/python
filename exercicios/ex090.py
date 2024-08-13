aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Media de {aluno['nome']}: '))
print(f'     Nome e igual a {aluno['nome']}')
print(f'     Media e igual a {aluno['media']}')
if aluno['media'] > 7:
    print('     Situacao e igual a Aprovado')
else:
    print('     Situacao e igual a Reprovado')