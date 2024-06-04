'''
Calculando o desconto de um valor.
'''
print('========================')
print('| CÁLCULO DE DESCONTOS |')
print('========================')

desc = float(input('Sem adicionar [%], informe de quanto será o desconto: '))
print('---')
val = float(input('Valor do produto: R$'))
print('=======')

desconto = val * (desc / 100)
val_total = val - desconto

print('Com o desconto de',desc,'%, o valor que antes era de R$',val,'vai passar a ser de R$',val_total)
print('========================')