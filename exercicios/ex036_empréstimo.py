casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prest = casa/(anos*12)
print(f'Para pagar uma casa de R${casa:.2f} em {anos} a prestação será de R${prest:.2f}')
if prest > sal*0.30:
    print('Empréstimo NEGADO!!!')
else:
    print('Empréstimo CONCEDIDO!!!')
