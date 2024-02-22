string = input("Digite algo: ")
print(f"O tipo primitivo desse valor é {type(string)}")
print(f"Só tem espaços {string.isspace()}")
print(f"É um número? {string.isnumeric()}")
print(f"É alfabético? {string.isalpha()}")
print(f"É alfanumérico? {string.isalnum()}")
print(f"Está em maiúsculas? {string.isupper()}")
print(f"Está em minúsculas? {string.islower()}")
print(f"Está capitalizada? {string.istitle()}") #Se o começo das palavras está em maiúsculas e o resto em minúsculas.
