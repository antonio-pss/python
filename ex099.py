def maior(*val):
    print(f'Foram passados: {val}')
    print(f'Foram passados {len(val)} valores e o maior entre eles é {max(val)}')

# PP
maior(1, 4, 5, 10, -2, 123, 1)