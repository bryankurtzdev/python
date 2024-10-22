from .lib.interface import *
from .lib.arquivo import *
from time import sleep

arq = 'tabelaNomes.txt'

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar Novo', 'Listar Pessoas', 'Sair do Sistema'])
    match resposta:
        case 1:
            cabecalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = leiaInt('Idade: ')
            cadastrar(arq, nome, idade)
        case 2:
            lerArquivo(arq)
        case 3:
            cabecalho('Saido do sistema... Ate logo!')
            break
    if 0 > resposta > 3:
        print('\033[31mERRO digite uma opcao valida!\033[m')
    sleep(2)
