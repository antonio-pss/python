n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
print(f'A média do aluno é {media}.')
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO!')
elif media >= 7:
    print('O aluno foi APROVADO!')
else:
    print('O aluno foi REPROVADO!')