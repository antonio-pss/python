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

p1 = ['Pedro', 25]
p2 = ['Maria', 19]
pessoas = []
pessoas.append(p1[:])
pessoas.append(p2[:])
print(pessoas)

refeições=[['Café', 6], ['Almoço', '12'], ['Lanche', 15], ['Janta', 19]]
print(refeições)
print(refeições[0][0])
print(refeições[2])