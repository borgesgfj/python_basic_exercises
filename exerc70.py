# programa que lê preço de vários produtos, e continua até o usuário digitar N
# no final mostrar a) Total de gastos; b) Quantos produtos custam mais de 1000,00 e c) Qual o nome no produto mais barato.

print('\033[1;34m==\033[m'*50)
print('\033[1;30;107m{: ^100}\033[m'.format('Lojinha do Gil'))
print('\033[1;34m==\033[m'*50)
total = c_1000 = c = 0
while True:
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preço = float(input('Preço: R$'))
    total += preço
    c += 1
    if preço > 1000:
        c_1000 += 1
    if c == 1:
        mais_barato = produto
        menor_preço = preço
    elif c > 1: # podia eliminar esse bloco fazendo no if de cima ' if c == 1 or preço < menor_preço: '
        if preço < menor_preço:
            mais_barato = produto
            menor_preço = preço
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print('\033[1;32;40m{:-^50}\033[m'.format('FIM DO PROGRAMA'))
print(f'\033[1;32mO total da compra foi R${total:.2f}\033[m')
print(f'\033[1;33mTemos {c_1000} produtos acima de R$1000.00\033[m')
print(f'\033[1;34mO produto mais barato foi {mais_barato} que custa R${menor_preço:.2f}\033[m')




