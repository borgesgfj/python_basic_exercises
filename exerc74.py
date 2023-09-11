# Formar um tupla com 5 números aleatórios. Mostrar a listagem de números, menor e maior valores
from random import randint
listagem = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = menor = listagem[0]
print('Os valores sorteados são: ', end='')
for c in listagem:
    print(c,end=' ')
    if c > maior:
        maior = c
    elif c < menor:
        menor = c
print(f'\nO maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')
