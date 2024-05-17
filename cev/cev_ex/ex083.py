expr = str(input('Expressão Matemática: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('V')
else:
    print('F')


'''if expr.count('(') == expr.count(')'):
    print('Expressão correta.')
else:
    print('Expressão incorreta.')'''

