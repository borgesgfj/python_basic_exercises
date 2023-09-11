# Calcula o preço de um produto e mostra o preço com 5% de desconto
p=float(input('Qual o preço normal do produto? '))
pd=p-(p*(5/100))
print('O preço do produto com 5% de desconto é: R$ {:.2f}'.format(pd))
