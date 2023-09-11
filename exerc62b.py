# Programa que calcula inicialmente os 10 primeiros termos de uma P.A e ao invés de acabar pergunta
# mais quantos termos deseja mostrar se o usuário digitar 0 ele encerra.
# agora vai mostrar apenas do os novos termos.
print('\033[1;30;107m{: ^100}\033[m'.format(' Calculadora de P.A'))
print(' ')
a1 = float(input('\033[34mPrimeiro termo: \033[m'))
razão = float(input('\033[34mRazão da P.A: \033[m'))
c = 0
total_termos = 10
termo_n = a1
x = 1 # quantidade a mais de termos.
while x != 0:
    c += 1
    if c == 1:
        print('\033[1;33mOs {} primeiros termos desta P.A são:\033[m'.format(total_termos))
        print('\033[31m{}'.format(a1), end='; \033[m')
    elif 1 < c < total_termos:
        termo_n += razão
        print('\033[31m{}'.format(termo_n), end='; ')
    elif c == total_termos:
        termo_n += razão
        print('\033[31m{}'.format(termo_n), end='.\033[m \n')
        x = int(input('\033[34mDeseja saber mais quantos termos? \033[m'))
        total_termos += x
        if x != 0:
            print('\033[1;97mOs termos de {} à {} são: \033[m'.format(total_termos + 1 - x, total_termos ))
print('\033[1;30;107m A progressão foi mostrada com {} termos.\033[m'.format(total_termos))
print(' '*50,'\033[1;30;107m FIM \033[m')

# podia ter copiado o programa anterior e colocar dentro de um while x !=0: