nome = str(input('Escreva seu nome: ')).strip()
if nome.lower().find('silva') != -1:
    print('Seu nome tem "Silva".')
else:
    print('Seu nome não tem "Silva".')

if 'silva' in nome.lower():
    print('Seu nome tem "Silva".')