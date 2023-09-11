# Jogo de par ou ímpar.
from time import sleep
from random import randint
print('\033[1;34m=-=\033[m'*40)
print(' '*30, '\033[1;44;30m Vamos Jogar par ou ímpar\033[m')
print('\033[1;34m=-=\033[m'*40)
print('')
c = 0
while True:
    pc = randint(0, 10)
    sleep(1)
    print('\033[30;107mPronto escolhi meu valor!\033[m')
    num_jogador = int(input('\033[34mDiga um valor (entre 0 e 10): \033[m'))
    ''' Caso o usuário erre a escolha '''
    if num_jogador > 10:
        while num_jogador > 10:
            print('\033[1;30;41mOpção inválida! Presta atenção meu amigo o número é entre 0 e 10.\033[m')
            sleep(1)
            num_jogador = int(input('\033[34mDiga um valor (entre 0 e 10): \033[m'))
    ''' Fim da prevenção de erro '''
    escolha_jogador = ' '
    ''' Caso o usuário digite errado '''
    while escolha_jogador not in 'PpIi':
        escolha_jogador = str(input('\033[34mPar ou ímpar? [P/I] \033[m')).strip().upper()[0]
    ''' Fim da prevenção de erro '''
    soma = pc + num_jogador
    ''' Resultado do jogo (se deu par ou ímpar) '''
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    ''' Analisando a condição de vitória do jogador '''
    if escolha_jogador == 'P' and resultado == 'PAR' or escolha_jogador == 'I' and resultado == 'ÍMPAR':
        status = 'VENCEU'
        c += 1
        print('\033[1;34m-\033[m'*50)
        print(f'\033[1;32mVocê jogou {num_jogador} e computador {pc}. Total de {soma}.\033[m \033[1;31;4mDEU {resultado}')
        print('\033[1;34m-\033[m' * 50)
        print(f'\033[1;44;30m Você {status}! \033[m')
        print('\033[32mVamos jogar novamente...')
        print('\033[1;34m=-=\033[m' * 30)
    else:
        status = 'PERDEU'
        print('\033[1;34m-\033[m'*50)
        print(f'\033[1;32mVocê jogou {num_jogador} e computador {pc}. Total de {soma}.\033[m \033[1;31;4mDEU {resultado}')
        print('\033[1;34m-\033[m' * 50)
        print(f'\033[1;44;30m Você {status}! \033[m')
        print('\033[1;34m=-=\033[m' * 30)
        print(f'\033[31mGAME OVER! Você venceu {c} vezes.\033[m')
        break

