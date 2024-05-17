l1 = float(input('Escreva o primeiro lado do triângulo: '))
l2 = float(input('Escreva o segundo lado do triângulo: '))
l3 = float(input('Escreva o terceiro lado do triângulo: '))

if l1+l2 < l3 and l1+l3 < l2 and l2+l3 < l1:
    print('Os lados digitados não podem formar um triângulo.')
elif l1 == l2 == l3:
    print('É um triângulo equilátero.')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('É um triângulo isôceles.')
elif l1 != l2 and l1 != l3 and l2 != l3:
    print('É um triângulo escaleno.')
else:
    print('Num sei não...')

