# calcular o fatorial de um número usando o laço for.
print('{: ^100}'.format('\033[1;97;40m Cálculo de fatorial \033[m'))
num = int(input('\033[34mQual número deseja calcular o fatorial?\033[m '))
if num == 0:
    print('\033[1;35;40m Por definição 0! = 1 \033[m')
else:
    fator = num
    print('\033[1;35;40m {}! = {}'.format(num, num), end=' x ')
    for c in range(num-1, 0, -1):
        fator *= c
        print(c,'x ' if c != 1 else '', end='')
    print('= {} \033[m'.format(fator))