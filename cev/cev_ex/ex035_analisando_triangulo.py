from time import sleep
print('--=' * 9)
print('Analisador de Triângulo...')
print('--=' * 9)
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
print('PROCESSANDO...')
sleep(2)
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 +l2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
