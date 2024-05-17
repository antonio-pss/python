termo = int(input('Escreva o primeiro termo da PA: '))
raz = int(input('Escreva a razão da PA: '))
i = 10

while i > 0:
    print(f'{termo}')
    termo += raz
    i -= 1
