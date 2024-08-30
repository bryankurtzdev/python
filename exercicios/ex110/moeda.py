def aumentar(preco=0, porc=0, formato=False):
    f = preco + (porc * preco/100)
    return f if formato is False else moeda(f)


def dobro(n=0, formato=False):
    f = n * 2
    return f if formato is False else moeda(f)


def metade(n=0, formato=False):
    f = n / 2
    return f if formato is False else moeda(f)


def reduzindo(preco=0, porc=0, formato=False):
    f = preco - (porc * preco/100)
    return f if formato is False else moeda(f)


def moeda(preco=0, moeda= 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

    a
def resumo(preco=0, txau=10, txre=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preco analisado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco, True)}')
    print(f'Metade do preco: \t{metade(preco, True)}')
    print(f'{txau}% de aumento: \t{aumentar(preco, txau, True)}')
    print(f'{txre}% de reducao: \t{reduzindo(preco, txre, True)}')
    print('-'*30)
aumentar()