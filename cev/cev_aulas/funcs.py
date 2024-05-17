# Parte 1 Funções
def soma(a, b):
    print(f'A soma de {a} + {b} é {a+b}')

def leitor(*num): # O * diz que vai ser vários parâmetros.
    print(f'Recebi os valores {num} e ao todo são {len(num)} valores.') # Ele cria uma tupla num e mostra na tela.

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

def contador(i, f, p): # Função com DOCSTRING.
    """
    => Faz uma contagem e mostra na tela.
    :param i: Início da contagem.
    :param f: Fim da contagem.
    :param p: Valor adicional da contagem.
    :return: Vazio.
    """
    while i < f:
        print(i, end=' ')
        i += p

def somar(a, b, c=0): # O c, como recebe 0, se torna opcional. Todos os valores podem ser opcionais.
    s = a + b + c
    print(s)

def escopo():
    global b
    a = 3
    b = 5
    print()



# Programa principal # Em python, variáveis goblais são as declaradas na mais.
soma(3, 5) # Inicialização normal.
soma(a=4, b=6) # Inicialização expliciatada.
soma(b=5, a=2) # Inicialização com as váriavéis em ordem diferente.

leitor(1, 2, 5, 0, -1) # Inicializa a função com quantos valores quiser.

lista = [1, 2, 3, 4, 5]
dobra(lista) # Chama a função com uma variável lista.
print(f'A lista com os valores dobrados é {lista}') # Para o Python, toda passada de parâmetro é uma referência.

# Parte 2 Funções
help(contador) # Mostra a docstring.

somar(1, 2, 3) # Chama o somar com todos as variáveis.
somar(5, 4) # Chama o somar com apenas duas variáveis.

a = 2
b = 3

print(f'A vale {a}')
print(f'B vale {b}')
# Após chamar a função, apenas aquelas variáveis faladas global mudarão, no caso, o b.
escopo()
print(f'A vale {a}')
print(f'B vale {b}')



