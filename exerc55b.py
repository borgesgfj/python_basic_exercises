# Proposto pelo Guanabara, sem usar uma lista
#primeiro declara variaveis maior e menor inicializando com um número, no caso o 0
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Digite o peso (Kg) da {}ª pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
        # pois para o primeiro valor dado, ele é o maior e o menor, dado que não tem outros valores!
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
        # o menor e o maior peso vão estar alocados com um valor (das interações anteriores), então ele checa
        # se o novo valor é maior ou menor do que o que está alocado, caso seja ele substitui.
print('\033[1;35mO maior peso digitado é: {}\033[m'.format(maior))
print('\033[1;33mO menor peso digitado é: {}\033[m'.format(menor))

