def notas(*n, sit=False):
    """
    -> Funcao para analisar notas e situacoes de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando a situacao do aluno.
    :return: dicionario com varias informacoes sobre a situacao da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r ['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas(5.5, 5.2, 9, 10, 4.2)
print(resp)