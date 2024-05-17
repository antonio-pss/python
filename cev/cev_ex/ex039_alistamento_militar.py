from datetime import date
ano = int(input('Em que ano você nasceu? '))
atual = int(date.today().year)
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} em {atual}.')
if idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} ano(s).')
    print(f'Seu alistamento foi em {atual - (ano+18)}')
elif idade == 18:
    print('Vai se alistar!!!')
else:
    print(f'Ainda faltam {18 - idade} anos para o alistamento.')
    print(f'Seu alistamento será em {(18 - idade) + atual}.')

