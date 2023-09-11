#programa que leia o peso de 5 pessoas e no final mostre qual o maior e o menor peso lidos.
pesos = [] # cria uma lista vazia que receberá os pessos das pessoas
for i in range(1, 6):
    pesos.append(float(input('Digite o peso (Kg) da {}ª pessoa: '.format(i))))
# o método .append() adiciona itens à lista pessoas. Aqui crio uma lista com os pesos informados
# Agora vou analisar qual dos valores é maior e o maior valor usando as funções max e min!

print('\033[1;35mO maior peso digitado é: {}\033[m'.format(max(pesos)))
print('\033[1;33mO menor peso digitado é: {}\033[m'.format(min(pesos)))


