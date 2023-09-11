#Programa que leia o ano de nascimento de um atleta e mostra a sua categoria de acordo com a idade
from datetime import date
print('*-'*20)
print('Cálculo da categória de atleta')
print('*-'*20)
nascimento = int(input('Qual o seu ano de nascimento? '))
idade = date.today().year - nascimento
if idade <= 9:
    categoria = 'MIRIM'
elif idade <=14: # se não for menor do que 9 então ele pura para a próxima condição.
    categoria = 'INFANTIL'
elif idade <= 19: #se não for menor do que 14 então ele pula para a próxima condição
    categoria = 'JUNIOR'
elif idade <= 20: #se não for menor que 19 ele ele pura para essa condição
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print('O(A) atleta tem {} anos. Ele(a) está na categoria \033[1;4;34m{}\033[m'.format(idade, categoria))