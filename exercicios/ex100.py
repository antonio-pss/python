from random import randint

def sorteia(lista):
    for i in range(5):
        lista.append(randint(1, 10))
    print(f'A lista sorteada é {lista}.')

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos números pares da lista é {soma}.')

# PP
lista = list()
sorteia(lista)
somaPar(lista)
