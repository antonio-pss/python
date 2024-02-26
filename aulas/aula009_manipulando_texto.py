# Aula 9 - Manipulando Texto
frase = 'Curso em Vídeo Python' # A frase vai ocupar "mini espaços". ICI IuI IrI IsI IoI I I IeI ImI ...

# FATIAMENTO
frase[0] # A primeira letra = 'C'
frase[9:13] # A letra na posição 9 a 13 = 'Víde' - Mas a posição final, 13, fica de fora.
frase[9:21] # A frase só tem 21 caracteres, mas ele não considera a posição 21, então é igual a frase inteira.
frase[9:21:2] # O 2 significa que ele ira pular de 2 em 2, V, d, o, P, t, o.
frase[:5] # Vai da posição 0 a 5, omitindo a 5º posição.
frase[15:] # Vai da posição 15 até o final.
frase[9::3] # Vai do 9 até final pulando 3 letras. V, e, P, h.

# ANÁLISE
len(frase) # Vai mostrar o tamanho da frase, no caso, 21 caracteres.
frase.count('o') # O programa irá contar quantos 'o' tem na frase, no caso, 3.
frase.count('o', 0, 13) # Vai contar quantos 'o' tem da posição 0 a 13 (tirando a 13), no caso, 1.
frase.find('deo') # O programa irá dizer a posição que ele encontrou o 'deo', no caso, 11.
frase.rfind('') # O programa irá procurar o que você pediu, mas inciando do lado direito, por isso o 'r', de 'right'.
frase.find('Android') # Quando ele não encontra o que foi pedido, ele retorna -1.
'Curso' in frase # O in irá retornar True ou False

# TRANSFORMAÇÃO
frase.replace('Python', 'Android') # Onde tiver 'Python' ele vai subistituir para 'Android' mas não muda.
frase.upper() # Fara com que toda a frase fique em maiúsculas.
frase.lower() # Fara com que toda a frase fique em minúsculas.
frase.capitalize() # Fara com que a primeira letra fique em maiúscula e todas as outras em minúsculas.
frase.title() # Ele verá quantas frases tem e transformará todas primeiras letras para maiúsculas.

nFrase = '  Aprendenda Python  '
nFrase.strip() # Ele removerá todas os espaços 'inúteis'.
nFrase.rstrip() # Removerá todas os espaços 'inúteis' a direita.
nFrase.lstrip() # Removerá todas os espaços 'inúteis' a esquerda.

# DIVISÃO
frase.split() # Ele vai retirar os espaços e dividir as palavras. Palavra 1 = Curso; Palavra 2 = em...
print(frase[2][3]) # Ele irá mostrar a segunda palavra da frase, só a quarta posição.
# JUNÇÃO
'-'.join(frase) # Ele vai juntar os elementos separados mas colocando o que está em ''. Curso-em-Vídeo...


print("""AAAAAAAAA
AAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAA""")
