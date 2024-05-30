'''
Dissecando uma variável usando tipos primitivos.
'''
print('===========================')
print('| DESCUBRA AS INFORMAÇÕES |')
print('===========================')

val = input('Digite algo: ')
print('------------')

print('Seu tipo primitivo é: ',type(val))
print('Só espeços: ',val.isspace())
print('É um número? ',val.isnumeric())
print('É alfabético? ',val.isalpha())
print('É alfanumérico? ',val.isalnum())
print('Está em maiúsculo? ',val.isupper())
print('Está em minúscula? ',val.islower())
print('Está capitalizada? ',val.istitle())

print('===========================')