def escreva():
    traco = len(msg) + 4
    print('+'*traco)
    print(f'  {msg}')
    print('+' * traco)


for c in range(0, 3):
    msg = str(input('Escreva sua mensagem: '))
    escreva()
