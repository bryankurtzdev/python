def aumentar(preco=0, porc=0):
    f = preco + (porc * preco/100)
    return f


def dobro(n=0):
    f = n * 2
    return f


def metade(n=0):
    f = n / 2
    return f


def reduzindo(preco=0, porc=0):
    f = preco - (porc * preco/100)
    return f
