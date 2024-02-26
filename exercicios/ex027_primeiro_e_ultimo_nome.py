nome = input('Digite seu nome: ').strip()
print(f'Seu primeiro nome é {nome[0:nome.find(' ')]}')
print(f'Seu último nome é {nome[nome.rfind(' ')+1:]}')