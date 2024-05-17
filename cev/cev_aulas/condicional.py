idade = int(input('Quantos anos você têm? '))
if idade >= 18:
    print('Você é maior de idade.')
elif idade > 100:
    print('Você deveria estar morto...')
elif idade < 0:
    print('Você ainda não nasceu...')
else:
    print('Você é menor de idade.') # Uma estrutura condicional não precisa terminar em else, pode terminar com elif ou só o if mesmo.

carTempo = int(input('Quantos anos tem seu carro?'))
print('Carro Novo.'if carTempo<=3 else'Carro Velho.')

