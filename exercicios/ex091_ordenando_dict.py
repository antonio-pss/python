from random import randint
from time import sleep
from operator import itemgetter

dados = dict()
dados = {'Jogador 1':randint(1, 6),
         'Jogador 2':randint(1, 6),
         'Jogador 3':randint(1, 6),
         'Jogador 4':randint(1, 6)}
ranking = dict()
for i, j in dados.items():
    print(f'{i} jogou {j}')
    sleep(0.5)

ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for i, j in enumerate(ranking):
    print(f'{i+1}º lugar: {j[0]} com {j[1]} pontos')


