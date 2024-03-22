cidade = str(input('Escreva a cidade em que você nasceu: ')).strip().lower()
if cidade[0:5] == 'santo':
    print('Sua cidade começa com "Santo".')
else:
    print('Sua cidade não começa com "Santo".')