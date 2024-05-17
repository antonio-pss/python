# Listas
lanche = ['Bubugue', 'Suco', 'Pizza', 'Pudim'] # Inicia com variáveis.
lanche[3] = 'Picolé' # Adiciona na posição.
lanche.append('Cockie') # Adiciona uma variável na última posição.
lanche.insert(2, 'Pudim') # Adiciona uma variável na posição escolhida e passa os outros para o lado.
del lanche[3] # Deleta na posição escolhida.
lanche.pop(0) # Deleta na posição escolhida.
lanche.pop() # Deleta na última posição.
lanche.remove('Pudim') # Elimina a variável e volta os outros.
lanche.clear() # Limpa toda a lista.

var = list(range(4, 27, 3)) # Cria uma lista com comando.
var.sort() # Deixa a lista em ordem crescente.
var.sort(reverse=True) # Deia a lista em ordem reversa.

janta = lanche # Isso não faz uma cópia, isso liga as duas listas.
café = lanche[:] # Isso sim faz uma cópia.

# Listas Compostas

p1 = ['Pedro', 25] # Cria um lista/vetor composta.
p2 = ['Maria', 19] # Cria um lista/vetor composta.
pessoas = [] # Cria uma lista/vetor que será transformada em matriz.
pessoas.append(p1[:]) # Adiciona a lista/vetor na posição 0 - Fazendo assim uma matriz composta.
pessoas.append(p2[:]) # Adiciona a lista/vetor na posição 1 - Fazendo assim uma matriz composta.
print(pessoas)

refeições=[['Café', 6], ['Almoço', 12], ['Lanche', 15], ['Janta', 19]] # Cria uma matriz composta [[]].
print(refeições) # Mostra tudo.
print(refeições[0][0]) # Mostra só a posição 0 da posição 0.
print(refeições[2]) # Mostra toda a posição 2 sendo Lanche e 15.

for l in refeições: # A variável p vira uma lista com as variáveis da posição específica da matriz.
    print(f'O {l[0]} será ás {l[1]}') # Forma de mostrar as duas posições.

amigos = []
dado = list()
for c in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    amigos.append(dado[:]) # Faz a cópia.
    dado.clear() # Limpa o dado.
