def aumentar(preco=0, porc=0):
    f = (porc * preco) / 100
    return f + preco


def dobro(n=0):
    return n * 2


def metade(n=0):
    return n / 2


def reduzindo(preco=0, porc=0):
    f = (porc * preco) / 100
    return preco - f


def moeda(preco):
    return f'R${preco:.2f}'
