# Programa que leia 4 números pelo teclado e guarde-os em uma tupla no final mostrar:
# quantas vezes apareceu o número 9; em que posição apareceu o primeiro valor 3; quais são os números pares.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
valores = (n1, n2, n3, n4)
''' Valores digitados '''
print(f'\033[1;33mVocê digitou os valores {valores}\033[m')
''' Quantas vezes aparece o valor 9 '''
print(f'\033[31mO valor 9 apareceu {valores.count(9)} vezes\033[m')
'''Posição do primeiro valor 3'''
if valores.count(3) == 0:
    print('\033[32mO valor 3 não foi digitado em nenhuma posição\033[m')
else:
    print(f'\033[32mO valor 3 foi digitado primeiro na {(valores.index(3))+1}ª posição\033[m')
'''Valores pares.'''
cont_par = 0
for c in valores:
    if c % 2 == 0:
        cont_par += 1
if cont_par == 0:
    print('\033[4;31mNão existem valores pares\033[m')
else:
    print('\033[1;34mOs valores pares digitados são:\033[m', end=' ')
    for c in valores:
        print(f'\033[1;34m{c}\033[m', end=' ')
