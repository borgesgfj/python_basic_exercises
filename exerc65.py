# Ler vários valores. Ao final mostar a média entre eles,  qual o maior e qual o menor valor lido.
# perguntar ao usuário se ele deseja continuar digitando.
from time import sleep
c = 0 # contador
s = 0 # soma
r = 'S' # flag
maior = 0
menor = 0
while r == 'S':
    n = int(input('\033[31mDigite um valor: '))
    c += 1
    s += n
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('\033[1;37;40m Deseja continuar? [S/N] \033[m')).strip().upper()
    if r != 'S' and r != 'N':
        print('\033[1;97;41m OPÇÃO INVÁLIDA. DIGITE S PARA CONTINUAR E N PARA SAIR\033[m')
        sleep(1)
        r = str(input('\033[1;37;40m Deseja continuar? [S/N] \033[m')).strip().upper()
média = s/c
print('\033[1;32mA média entre os números digitados é: {}\033[m'.format(média))
print('O MAIOR valor digitado foi: \033[4;34m{}\033[m'.format(maior))
print('O MENOR valor digitado foi: \033[4;35m{}\033[m'.format(menor))




