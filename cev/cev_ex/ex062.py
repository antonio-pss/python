termo = int(input('Escreva o primeiro termo da PA: '))
raz = int(input('Escreva a razão da PA: '))
i = int(input('Quantos termos você quer mostrar? '))

while i > 0:
    print(f'{termo}', end=' ')
    termo += raz
    i -= 1
