#Converter um número decimal para binário; octal ou hexadecimal.
#o usuário escolhe. 1 - binário; 2- octal ; 3 - hexadecimal
from time import sleep
print('\033[1;31m*-*\033[m'*30)
print(' '*20,'\033[1;97;101m Conversor de número inteiro \033[m')
print('\033[1;31m*-*\033[m'*30)
num = int(input('\033[1;32mDigite o número inteiro a ser convertido:\033[m '))
print('')
print('\033[1;30;104mBase para a conversão: 1 - binário | 2 - octal | 3 - hexadecimal\033[m')
sleep(2)
base = int(input('\033[1;32mEscolha a base para conversão:\033[m '))
if base > 3:
    print('Opção inválida tente novamente.')
elif base == 1:
    num_convert = bin(num)
    tipo_saida = 'binário'
    print('O número \033[1;32m{}\033[m convertido para \033[1;4;34m{}\033[m é: \033[1;31m{}\033[m'.format(
        num, tipo_saida, num_convert[2:]))
elif base == 2:
    num_convert = oct(num)
    tipo_saida = 'octal'
    print('O número \033[1;32m{}\033[m convertido para \033[1;4;34m{}\033[m é: \033[1;31m{}\033[m'.format(
        num, tipo_saida, num_convert[2:]))
elif base == 3:
    num_convert = hex(num)
    tipo_saida = 'hexadecimal'
    print('O número \033[1;32m{}\033[m convertido para \033[1;4;34m{}\033[m é: \033[1;31m{}\033[m'.format(
        num, tipo_saida, num_convert[2:]))


