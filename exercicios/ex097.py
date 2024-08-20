def escreva():
    traco = len(msg) + 2
    print('-'*traco)


for c in range(0, 3):
    msg = str(input('Escreva sua mensagem: '))
    escreva()
    print(msg)
    escreva()
