frase = input("Digite uma frase: ").strip().lower()
print(f"A letra 'A' aparece {frase.count('a')} na frase.")
print(f"A primeira ocorrência da letra 'A' é na posição {frase.find('a')+1}")
print(f"A última ocorrência da letra 'A' é na posição {frase.rfind('a')+1}")