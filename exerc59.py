# um programa que leia dois valores e mostre um menu na tela:
''' [1] somar; [2] multiplicar; [3] maior [4] entrar com novos números; 5 [sair] '''
from time import sleep
n1 = int(input('Digite o primeiro valor: ')) #entra o primiero valor
n2 = int(input('Digite o segundo valor: ')) # entra o segundo valor
opção = 0
while opção != 5:
    print('\033[1;33m=-\033[m'*40)
    print('{: ^100}'.format('\033[1;30;105m O que deseja fazer? \033[m'))
    print('\033[1;97;44m [1]Somar | [2]multiplicar | [3] maior valor | [4] Novos valores | [5]Sair \033[m')
    print('\033[1;33m=-\033[m'*40)
    opção = int(input('Digite uma opção: '))
    if opção != 1 and opção != 2 and opção != 3 and opção != 4 and opção != 5:
        print('\033[1;97;41m Opção inválida. Tente nomavemnte!\033[m')
        sleep(1)
    if opção == 1:
        s = n1 + n2
        print('\033[1;30;107mO primeiro valor digitado foi {} e o segundo foi {} \033[m'.format(n1, n2))
        print(' '*8,'\033[1;34;107m {} + {} = {} \033[m'.format(n1, n2, s))
        sleep(1)
    elif opção == 2:
        p = n1*n2
        print('\033[1;30;107m O primeiro valor digitado foi {} e o segundo foi {} \033[m'.format(n1, n2))
        print(' '*8,'\033[1;34;107m {} x {} = {} \033[m'.format(n1, n2, p))
        sleep(1)
    elif opção == 3:
        maior = n1
        print('\033[1;30;107m O primiero valor digitado foi {} o segundo valor digitado foi {} \033[m'.format(n1, n2))
        print(' '*8, '\033[1;34;107m {result} \033[m'.format(result = 'O SEGUNDO VALOR É MAIOR' if n2 > n1 else ' O PRIMEIRO VALOR É MAIOR'))
        sleep(1)
    elif opção == 4:
        n1 = int(input('Digite o primeiro valor: '))  # entra o primiero valor
        n2 = int(input('Digite o segundo valor: '))  # entra o segundo valor
print('{: ^100}'.format('\033[1;30;105m FIM \033[m'))



