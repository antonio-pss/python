def notas(*notas, sit=False):
    val = dict()
    val['Notas'] = len(notas)
    val['Maior'] = max(notas)
    val['Menor'] = min(notas)
    val['Média'] = sum(notas)/len(notas)
    if sit:
        if val['Média'] < 6:
            val['Situação'] = 'Ruim'
        elif val['Média'] < 7:
            val['Situação'] = 'Ok'
        else:
            val['Situação'] = 'Boa'
    return val

turma = notas(6, 7, 10, 4, sit=True)
print(turma)