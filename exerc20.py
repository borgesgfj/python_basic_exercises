#Mostre o nome de quatro pessoas e mostre uma ordem de apresentação sorteada.
from random import sample
a1=input('Digite o nome do(a) primeiro(a) aluno(a): ')
a2=input('Digite o nome do(a) segundo(a) aluno(a): ')
a3=input('Digite o nome do(a) terceiro(a) aluno(a): ')
a4=input('Digite o nome do(a) quarto(a) aluno(a): ')
l=[a1,a2,a3,a4]
s=sample(l,k=len(l))
print('_'*40)
print('A ordem de apresentação será a seguinte: ')
print('_'*40)
print(' 1º) {}\n 2º) {} \n 3º) {} \n 4º) {} '.format(s[0], s[1], s[2], s[3]))
print('_'*40)