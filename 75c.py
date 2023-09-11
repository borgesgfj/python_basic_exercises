# Programa que leia 4 números pelo teclado e guarde-os em uma tupla no final mostrar:
# quantas vezes apareceu o número 9; em que posição apareceu o primeiro valor 3; quais são os números pares.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
valores = (n1, n2, n3, n4)
''' Valores digitados '''
print(f'\033[1;33mVocê digitou os valores {valores}\033[m')
c9 = 0 # contador do número 9
for c in valores:
    if c == 9:
        c9 += 1
print(f'\033[31mO valor 9 apareceu {c9} vezes\033[m')
