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