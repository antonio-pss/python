file = open('path\\file.type', 'w+') # Abrir o arquivo e dizer que é apenas para escrita.
file.write('Hello, World.')
file.close()

file = open('path\\file.type', 'r') # r para apenas leitura.
content = file.read()
lines = file.readlines()
print(content)
print(lines[0])
file.close()

# open('path', 'a for append, t for trunc...')
