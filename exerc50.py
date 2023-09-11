#desenvolva um programa que leia 6 números inteiros e mostra a soma apenas dos números pares
s=0 #aloca a variável soma
for c in range(1, 7):
    n = int(input(' Digite um número inteiro: '))
    if n % 2 == 0:
        s += n
print('\033[1;31mA soma dos números pares digitados é {}\033[m'.format(s))