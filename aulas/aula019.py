# Dicionário {}

dados = dict() # Declaração de dicionários.
dados = {'Nome':'Antônio', 'Idade':25} # Iniciando variáveis.
print(dados['Nome']) # Vai mostrar apenas o nome.
dados['sexo'] = 'M' # Adiciona mais uma parte.
del dados['Idade'] # Deleta uma parte.

filme = {'titulo': 'Star Wars',
         'ano': '1977',
         'diretor': 'George Lucas'}
print(filme.values()) # Pegar apenas apenas os valores. Ex: 1977
print(filme.keys()) # Pegar apenas as chaves. Ex: Ano
print(filme.items()) # Pegar valores e chaves.

for k, v in filme.items(): # Percorre o dicionário pelas keys e values.
    print(f'O {k} é {v}')

pessoas = dict()
sala = list()
for i in range(3):
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Idade'] = int(input('Idade: '))
    sala.append(pessoas.copy()) # Função que copia um dicinionário adicionando em uma lista lista.
print(sala)