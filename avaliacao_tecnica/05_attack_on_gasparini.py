# Declaração de Variáveis e Entrada de Dados.
numero_titas = int(input('Digite o número de titãs: '))
tamanho_muralha = int(input('Digite o tamanho da muralha: '))
tamanho_titas = str(input('Digite o tamanho dos titãs (Ex: PMG): ')).strip().upper()
tita_p = int(input('Digite o tamanho do titã pequeno: '))
tita_m = int(input('Digite o tamanho do titã médio: '))
tita_g = int(input('Digite o tamanho do titã grande: '))

# Quantidade de muralhas em um vetor onde cada Titã irá passar.
muralhas = [tamanho_muralha]

# Variáveis auxiliares para usar com o while.
i: int = 0
j: int

# Processamento dos dados com a lógica necessária.
while i < numero_titas:
    if tamanho_titas[i] == 'P':
        j = 0
        while j < len(muralhas):
            if muralhas[j] >= tita_p:
                muralhas[j] -= tita_p
                i += 1
                break
            else:
                j += 1
                if j == len(muralhas):
                    muralhas.append(tamanho_muralha)
    elif tamanho_titas[i] == 'M':
        j = 0
        while j < len(muralhas):
            if muralhas[j] >= tita_m:
                muralhas[j] -= tita_m
                i += 1
                break
            else:
                j += 1
                if j == len(muralhas):
                    muralhas.append(tamanho_muralha)
    elif tamanho_titas[i] == 'G':
        j = 0
        while j < len(muralhas):
            if muralhas[j] >= tita_g:
                muralhas[j] -= tita_g
                i += 1
                break
            else:
                j += 1
                if j == len(muralhas):
                    muralhas.append(tamanho_muralha)
    else:
        print('Os tamanhos do titãs não foram digitados corretamente.')
        i = numero_titas
    print(f'O {i}º titã chega, olhe como as muralhas estarão: {muralhas}')

print(f'Será necessário criar {len(muralhas)} muralha(s).')