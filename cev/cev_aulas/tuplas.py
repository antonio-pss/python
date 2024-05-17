# Tuplas são variáveis compostas. Elas são declaradas com ().
# Tuplas são imutáveis.
lanche = ('Pizza', 'Cachorro-Quente', 'Pudim')

for comida in lanche:
    print(comida)

for cont in range(len(lanche)):
    print(lanche[cont])

for cont, comida in enumerate(lanche):
    print(f'Posição {cont}, Comida {comida}')

print(sorted(lanche))
print(lanche)

a = (2, 5, 4)
b = (8, 1, 3, 3)
c = b + a
print(c)
print(c.count(3))
print(c.index(8, 0, 1))

pessoa = ('Antônio', 19, 'M', '1.65')
print(pessoa)
del(pessoa)
# print(pesso) - Agora vai dar erro, pois não existe mais.