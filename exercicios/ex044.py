compras = float(input('Quanto deu sua compra? R$'))
print('De que forma irá pagar? ')
print('[1] A vista.')
print('[2] A vista no cartão.')
print('[3] 2x no cartão.')
print('[4] 3x ou mais no cartão.')
escolha = int(input('Sua escolha: '))

if escolha == 1:
    print(f'Sua compra de R${compras} vai custar R${compras*0.90} a vista.')
elif escolha == 2:
    print(f'Sua compra de R${compras} vai custar R${compras*0.95} a vista no cartão.')
elif escolha == 3:
    print(f'Sua compra de R${compras} não mudará em 2x no cartão.')
elif escolha == 4:
    parcelas = int(input('Em quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas} vezes de {(compras*1.20)/parcelas} com juros.')
    print(f'Sua compra de R${compras} irá custa R${compras*1.20} no final.')
else:
    print('Você digitou errado...')