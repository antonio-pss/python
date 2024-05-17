import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print(f'Seno = {seno :.2f}')
print(f'Cosseno = {cosseno :.2f}')
print(f'Tangente = {tangente :.2f}')
