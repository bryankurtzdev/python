pessoa = dict()
galera = list()
som = med = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    som += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print("-=" * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = som / len(galera)
print(f'A media de idade e de {media:5.2f} anos.')
print('As mulheres cadastradas foram', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p['nome']} ', end='')
print()
print('Lista de pessoas que estao acima da media: ', end='')
for p in galera:
    if p['idade'] >= media:
        print(f' {p['nome']} ')
print('<< ENCERANDO >>')
