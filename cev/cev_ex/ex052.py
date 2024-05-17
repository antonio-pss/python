num = int(input('Escreva um número inteiro: '))
primo = True

for i in range(1, num):
    if num % i == 0 and i != 1:
        primo = False

if primo != False:
    print('O número é primo.')
else:
    print('Não é primo.')