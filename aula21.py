from datetime import datetime


def voto(ano):
    idd = datetime.now().year - ano
    if idd < 16:
        print(f'Devido a idade de {idd} anos seu nao e PERMITIDO!')
        return idd
    elif 16 < idd < 18:
        print(f'Devido a idade de {idd} anos seu voto e OPCIONAL!')
        return idd
    else:
        print(f'Devido a sua idade de {idd} anos seu voto e OBRIGATORIO!')
        return idd


idd = voto(int(input('Ano de nasciento: ')))
