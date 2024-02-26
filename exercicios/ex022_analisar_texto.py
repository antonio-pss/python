nome = input("Digite seu nome: ").strip()
print("Analisando seu nome...\n"
      f"Seu nome em maiúsculas é {nome.upper()}\n"
      f"Seu nome em minúsculas é {nome.lower()}\n"
      f"Seu nome tem ao todo {len(nome) - nome.count(' ')}\n"
      f"Seu primeiro nome é {nome[0:nome.find(' ')]}\n"
      f"Seu primeiro nome tem {nome.find(' ')} letras.")

