#jogo de Jokenpô (pedra tesoura ou papel)
from random import choice
from time import sleep
print('\033[1;33m*-*\033[m'*20)
print(' '*15,'\033[1;97;45m Vamos Jogar Jokenpô!\033[m')
print('\033[1;33m*-*\033[m'*20)

opções = ['pedra', 'tesoura', 'papel']
escolha_pc = choice(opções) #PC vai sortear um dos elementos de opções.
sleep(1)
print('\033[1;32mJá escolhi a minha opção. Escolha a sua e tente me vencer.\033[m') # pc indica que já escolheu.
print('\033[1;97;44mDigite: 0 - pedra | 1 - tesoura | 2 - papel \033[m') #imprime o código númerico das opções
escolha_usr = int(input('Sua Jogada: ')) # Usuário entra com um número
usr = opções[escolha_usr] #converte o número escolhido em pedra tesoura ou papel dependendo da escolha
#calculado as condições de vitória
if usr == 'pedra' and escolha_pc == 'tesoura' or usr == 'tesoura' and escolha_pc == 'papel' or usr == 'papel' and escolha_pc == 'pedra':
    resultado = '\033[1;4;34mVocê venceu!\033[m'
elif escolha_pc == 'pedra' and usr == 'tesoura' or escolha_pc == 'tesoura' and usr == 'papel' or escolha_pc == 'papel' and usr == 'pedra':
    resultado = '\033[1;4;31mEu ganhei, sou o melhor!\033[m'
elif escolha_pc == usr:
    resultado = '\033[1;4;33mOps! Empatamos!\033[m'

print('Eu escolhi \033[4;32m{}\033[m e você escolheu \033[4;32m{}\033[m.'.format(escolha_pc, usr))
print('{}'.format(resultado))