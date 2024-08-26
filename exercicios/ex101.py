def voto(ano):
    from datetime import datetime
    idd = datetime.now().year - ano
    if idd < 16:
        return f'Devido a idade de {idd} anos seu voto nao e PERMITIDO!'
    elif 16 < idd < 18 or idd > 65:
        return f'Devido a idade de {idd} anos seu voto e OPCIONAL!'
    else:
        return f'Devido a sua idade de {idd} anos seu voto e OBRIGATORIO!'


nasc = voto(int(input('Ano de nasciento: ')))
print(nasc)
