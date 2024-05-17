frase = str(input('Escreva algo: ')).upper().strip().split()
frase = ''.join(frase)

if frase[::-1] == frase:
    print('O que você escreveu é um palíndromo.')
else:
    print('Tudo normal por aqui.')