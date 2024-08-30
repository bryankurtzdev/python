def leiaDinheiro(p):
    vali = False
    while not vali:
        entrada = str(input(p))
        if entrada.isalpha():
            print(f'EROO: \"{entrada}\" e um preco invalido!')
        else:
            valido = True
            return float(entrada)
