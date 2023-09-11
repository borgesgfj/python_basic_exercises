#números pares no intervalo de 1 a 50 (contando de 2 em 2)
print('{:*^55}'.format('\033[1;31m Números pares entre 1 e 50 \033[m'))
for c in range(2, 51, 2): #como 1 é ímpar desprezo ele! e vou de 2 em 2 até 51 para incluir o 50.
    if c < 50:
        print('{}'.format(c), end=', ')
    if c==50:
        print('{}'.format(c),end='.')

