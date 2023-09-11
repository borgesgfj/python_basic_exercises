#Computador escolhe um número entre 0 e 5 e o usuário tenta adivinhar este número
import emoji
from random import randint
num_pc=randint(0,5)
print('Tente advinhar um número ente 0 e 5 que o computador escolheu!')
num_usr=int(input('Digite um número entre 0 e 5: '))
if num_usr==num_pc:
    print('Você acertou! Vai ganhar um beijinho!')
else:
    print('Você errou! O número escolhido pelo computador foi {} e você digitou {}.'.format(num_pc, num_usr))
