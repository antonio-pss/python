def voto(nasc):
    from datetime import date # Escopo de Importação
    idade = date.today().year - nasc
    if idade < 16:
        return f'Com {idade}: Voto NEGADO.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade}: Voto OPCIONAL'
    else:
        return f'Com {idade}: Voto OBRIGATÓRIO'

nascimento = int(input('Data de Nascimento: '))
vot = voto(nascimento)
print(vot)
