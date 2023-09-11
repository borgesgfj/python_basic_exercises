#leia um número inteiro e diga se ele é par ou ímpar
num=int(input('\033[1;31;40mDigite um número inteiro qualquer: \033[m'))
if (num%2)==0:
    print('O número {} \033[1;34mé par\033[m'.format(num))
else:
    print('O número {} é \033[1;35mímpar\033[m'.format(num))
