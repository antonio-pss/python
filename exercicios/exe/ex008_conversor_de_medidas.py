medida = float(input("Uma medida em metros: "))
print(f"A medida de {medida}m corresponde a: \n"
      f"{medida / 1000}km \n"
      f"{medida / 100}hm \n"
      f"{medida / 10}dam \n"
      f"{medida * 10:.0f}dm \n"
      f"{medida * 100:.0f}cm \n"
      f"{medida * 1000:.0f}mm")