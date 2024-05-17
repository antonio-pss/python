from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
if 0 < idade <= 9:
    print('Atleta MIRIM.')
elif 9 < idade <= 14:
    print('Atleta INFANTIL.')
elif 14 < idade <= 19:
    print('Atleta JUNIOR.')
elif 19 < idade <= 25:
    print('Atleta SÊNIOR.')
elif idade > 25:
    print('Atleta MASTER.')
else:
    print('??????????????')
