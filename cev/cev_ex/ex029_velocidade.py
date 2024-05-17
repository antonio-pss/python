velocidade = float(input('Qual a velocidade atual do seu carro? '))
if velocidade > 80:
    print(f'Você foi multado, deve pagar R${(velocidade-80)*7:.2F}')
else:
    print('Tenha um bom dia! Dirija com segurança!')