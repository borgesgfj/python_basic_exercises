#Programa que compara dois valores indicando o maior
from time import sleep
print('\033[1;32m*-\033[m'*30)
print('\033[1;30mAnalisador de valores\033[m')
print('\033[1;32m*-\033[m'*30)
n1 = float(input('Qual o primeiro valor a ser analisado? '))
n2 = float(input('Qual o segundo valor a ser analisado? '))
print('\033[1;36mO primeiro valor é {} e o segundo valor é {}\033[m'.format(n1, n2))
print('\033[1;34mAguarde analisando...\033[m')
sleep(2) #computador espera n s antes de analisar!
if n1 > n2:
    print('\033[31mO primeiro valor é maior\033[m')
elif n2 > n1:
    print('\033[31mO segundo valor é maior\033[m')
else:
    print('\033[1;97;101mNão existe valor maior, os dois valores são iguais\033[m')
