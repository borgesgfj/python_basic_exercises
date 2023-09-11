# Criar uma tupla única contendo nome de produtos e seus preços. No final mostrar uma saída tabular.
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.00)
print('\033[1;32m-\033[m'*40)
print('{: ^55}'.format('\033[1;30;107m Lista de Produtos \033[m'))
print('\033[1;32m-\033[m'*40)
for c in range(0, len(produtos), 2):
    print(f'\033[1;35m{produtos[c]:.<30}\033[m\033[1;31mR$ {produtos[c+1]:>6.2f}')
print('\033[1;32m-\033[m'*40)