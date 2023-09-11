#números pares entre 1 e 50 maneira 2 (analisando se o número é par ou ímpar.
print('{:*^90}'.format('\033[1;31m Números pares entre 1 e 50 \033[m'))
for c in range(1, 51):
    if c % 2 == 0 and c !=50:
        print('{}'.format(c), end=', ')
    if c % 2 == 0 and c == 50:
        print('{}'.format(c), end='.')
print('\nFIM')
# O problema aqui é que ele faz um laço duas vezes, antes de imprimir o que interessa, então gasta mais processador