import datetime
from datetime import date

pessoa = {'Nome':[], 'Ano de Nascimento':[], 'Idade':[], 'CTPS':[], 'Ano de Contratação':[], 'Salário':[], 'Aposentadoria':[]}

pessoa['Nome'].append(str(input('Nome: ')))
pessoa['Ano de Nascimento'].append(int(input('Ano de Nascimento: ')))
pessoa['Idade'].append(date.today().year - pessoa['Ano de Nascimento'][0])
pessoa['CTPS'].append(int(input('Carteira de Trabalho (Se não tiver digite 0): ')))
if pessoa['CTPS'][0] != 0:
    pessoa['Ano de Contratação'].append(int(input('Ano de contratação: ')))
    pessoa['Salário'].append(float(input('Salário: ')))
    pessoa['Aposentadoria'].append(pessoa['Idade'][0] + 35 - (date.today().year - pessoa['Ano de Contratação'][0]))
    if pessoa['Aposentadoria'][0] < 1:
        pessoa['Aposentadoria'][0] = 0
else:
    pessoa['Ano de Contratação'].append(0)
    pessoa['Salário'].append(0)
    pessoa['Aposentadoria'].append(0)

print(pessoa)
