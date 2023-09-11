#programa que calcula o preço de um produto dependendo da condição de pagamento.
#à vista/dinheiro = 10% de desconto; à vista cartão 5% de desconto; Até 2x no cartão = preço normal; 3x ou mais = 20% juros

print('*-*'*15)
print('{:*^55}'.format('\033[1;31m Lojinha do Gil \033[m')) #escreve lojinha do gil formatado com 55 espaços preenchidos por *
print('*-*'*15)

valor_normal = float(input('Qual o preço do produto? '))
print('\033[1;97;44mDigite: 1 - À vista no dinheiro ou cheque | 2 - À vista no débito | 3 - Parcelado no cartão\033[m')
forma = int(input('\033[1;4;34mSelecione a forma de pagamento:\033[m ')) #escolhe a forma de pagamento
if forma == 1:
    valor_final = valor_normal - (valor_normal*0.1)
elif forma == 2:
    valor_final = valor_normal - (valor_normal*0.05)
elif forma == 3:
    parcelas = int(input('Quantas vezes deseja parcelar? '))
    if parcelas <= 2:
        valor_final = valor_normal
    else:
        valor_final = valor_normal + (valor_normal*0.2)
print('Valor do produto: R${:.2f} \nValor a pagar R${:.2f}'.format(valor_normal, valor_final))
print('Dividido em {} parcelas de R${:.2f}'.format(parcelas, valor_final/parcelas) if forma == 3 else '')
print('Obrigado por comprar na Lojinha do Gil! Tenha um bom dia!')


