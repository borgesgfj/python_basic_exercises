from random import randint
listagem = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = menor = listagem[0]
print('Os valores sorteados são: ', end='')
for c in listagem:
    print(c,end=' ')
print(f'\nO maior valor sorteado foi {max(listagem)}')
print(f'O menor valor sorteado foi {min(listagem)}')