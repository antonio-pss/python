from random import randint
from time import sleep
computador = randint(0, 5)
print('--=' * 19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('--=' * 19)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print(f'PARABÉNS! O número que pensei foi {computador}, o mesmo que o seu.')
else:
    print(f'GANHEI! O número que pensei foi {computador}, diferente do seu.')