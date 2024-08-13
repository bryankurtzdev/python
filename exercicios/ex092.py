from datetime import datetime
lista = dict()
lista['nome'] = str(input('Digite seu nome: '))
nasc = int(input('Ano de Nascimento: '))
lista['idade'] = datetime.now().year - nasc
lista['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))
if lista['ctps'] != 0:
    lista['contratacao'] = int(input('Ano de Contratacao: '))
    lista['salario'] = float(input('Salario: R$'))
    lista['aposentadoria'] = lista['idade'] + ((lista['contratacao'] + 35) - datetime.now().year)
print('-='*30)
for k, v in lista.items():
    print(f'  - {k} tem o valor {v}')
