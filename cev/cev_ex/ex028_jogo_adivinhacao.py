from random import choice
num = [0, 1, 2, 3, 4, 5]
escolhido = choice(num)
print('--=--=--=----=--=--=----=--=--=----=--=--=----=--=--=--')
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('--=--=--=----=--=--=----=--=--=----=--=--=----=--=--=--')
escolha = int(input('Em que número eu pensei? '))
if escolha == escolhido:
    print(f'PARABÉNS. O número que pensei foi {escolhido}, o mesmo que o seu.')
else:
    print(f'Que pena. O número que pensei foi {escolhido}, ele é diferente do seu.')

