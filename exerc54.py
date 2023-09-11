#Programa que leia o ano de nascimento de 7 pessoas e conte quantas ainda não atingiram a maioridade
#considere maioridade =21 anos
from datetime import date
contador = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        contador += 1
print('Das sete pessoas {} são maiores de idade e {} ainda não atingiram a maioridade'.format(contador, 7-contador))
