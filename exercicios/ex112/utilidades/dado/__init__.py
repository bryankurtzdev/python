def leiaDinheiro(p):
    vali = False
    while not vali:
        entrada = str(input(p)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mEROO: \"{entrada}\" e um preco invalido!\033[m')
        else:
            valido = True
            return float(entrada)
