num = float(input("Informe um número: "))
print(f"Analisando o número {num:.0f}...\n"
      f"Unidade: {num%10:.0f}\n"
      f"Dezena: {(num/10)%10:.0f}\n"
      f"Centena: {(num/100)%10:.0f}\n"
      f"Milhar: {(num/1000)%10:.0f}")