''' calcular os 10 primeiros termos de uma P.A usando um laço while'''

print('\033[1;30;107m{: ^100}\033[m'.format(' Calculando os 10 primeiros termos de uma P.A'))
print(' ')
a1 = float(input('\033[34mPrimeiro termo: \033[m'))
razão = float(input('\033[34mRazão da P.A: \033[m'))
c = 1
termo_n = a1
print('\033[1;34mOs 10 primeiros termos desta P.A são:\033[m')
print('\033[1;32;40m {}'.format(a1), end= '; ')
while c < 10:
    c += 1
    termo_n += razão
    if c != 10:
        print(termo_n,end='; ')
    else:
        print(termo_n, end='.')
print('\033[m\n ')
print(' '*50,'\033[1;30;107m FIM \033[m')
