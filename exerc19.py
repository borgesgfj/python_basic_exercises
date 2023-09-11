#Sortear uma dentre 4 pessoas e escrever seu nome na tela
from random import choice
a1=input('Nome do(a) primeiro(a) aluno(a): ')
a2=input('Nome do(a) segundo(a) aluno(a): ')
a3=input('Nome do(a) terceiro(a) aluno(a): ')
a4=input('Nome do(a) quarto(a) aluno(a): ')

print('O(A) aluno(a) sorteado(a) é: {}'.format(choice([a1,a2,a3,a4])))