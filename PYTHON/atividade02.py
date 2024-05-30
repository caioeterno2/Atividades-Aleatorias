'''
Mostrando o dobro, triplo e raiz quadrada de um valor
'''

print('===============================')
print('| DOBRO - TRIPLO - R.QUADRADA |')
print('===============================')

val = float(input('Digite um valor numérico: '))
print('---------------------------')

dob = 2 * val
tri = 3 * val
raiz = val ** (1/2) 

print('O dobro de',val,'é',dob)
print('Seu triplo é',tri)
print('E sua raiz quadrada é','%.2f'%raiz)

print('===============================')