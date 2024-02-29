sal = float(input('Digite o salário: R$'))
if sal > 1250:
    salN = sal * 1.10
else:
    salN = sal * 1.15

print(f'Quem ganhava R${sal:.2f} passa a ganhar R${salN:.2f}')
