# calcular o fatorial de um número usando o while.
print('{: ^100}'.format('\033[1;97;40m Cálculo de fatorial \033[m'))
num = int(input('\033[34mQual número deseja calcular o fatorial?\033[m '))
if num == 0:
    print('\033[1;35;40m Por definição 0! = 1 \033[m')
else:
    c = 0
    fator = num
    print('\033[1;35;40m {}! ='.format(num), end=' ')
    while c != num:
        parcela = num - c # calcula cada parcela do fatorial
        print(parcela,'x ' if (num -c) != 1 else '= ', end='') # imprime as parcelas do fatorial
        c += 1
        if c != num:
            fator *= (num - c) # calcula o fatorial
    print('{} \033[m'.format(fator),end='\n') #imprime o fatorial
print(' '*30, '\033[1;30;107m Fim \033[m')





