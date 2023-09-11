# Jogo da adivinhação 2.0
from random import randint
from time import sleep
print('\033[1;35m{:~^100}\033[m'.format(' Jogo da adivinhação 2.0 '))
print('{: ^120}'.format('\033[1;30;105m Tente adivinhar o número que estou pensando \033[m'))
num_pc = randint(0,  10)
jogador = 11
tent = 0 # contador para saber o número de tentativas.
dica = ''
sleep(1)
print('\033[1;96;40mPronto pensei!\033[m')
while jogador != num_pc:
    jogador = int(input('Escolha um número entre 0 e 10: '))
    tent += 1
    if jogador > 10:
        print('\033[1;31m Ô humano é um número entre 0 e 10. Vai de novo. \033[m')
        sleep(1)
    if jogador <=10 and jogador != num_pc:
        if jogador < num_pc:
            dica = 'MAIOR'
        elif jogador > num_pc:
            dica = 'MENOR'
        print('\033[1;33mO número que pensei é {} do que {}. Tente novamente!\033[m'.format(dica, jogador))
if tent == 1:
    print('\033[1;32mAê acertou de primiera! Que sorte!\033[m')
else:
    print('\033[34mAcertou!\033[m')
    print('\033[30;107mMas você precisou de {} tentativas\033[m'.format(tent))


