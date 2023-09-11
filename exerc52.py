#Programa que leia um número inteiro e diga se ele é ou não um número primo.
print('\033[1;36m*-*\033[m'*30)
print('{:^100}'.format('\033[1;97;43m Verificador de número primo \033[m'))
print('\033[1;36m*-*\033[m'*30)

num = int(input('Qual número deseja verificar? '))
contador = 0 # Aloca o espaço para o contador de quantos divisores tem num.
if num == 1:
    print('\033[1;31mPor definição números primos devem ser maiores que 1\033[m')
else:
    for c in range(1, num+1):
        if num % c == 0:
            print('\033[1;32m{}\033[m'.format(c), end='  ')
            contador += 1
        else:
            print('\033[31m {}\033[m'.format(c), end='  ')
print('\n\033[1;36mO número {} foi divisível {} vezes\033[m'.format(num, contador))
print('\nE por isso ele {status}.'.format(status = '\033[1;4;32mÉ PRIMO\033[m' if contador == 2 else '\033[1;4;31mNÃO É PRIMO\033[m' ))


