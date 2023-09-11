# ler vários números inteiros pelo teclado. Parar quando digitar 999 (flag).
# Ao final mostrar quantos números foram digitados e qual a soma entre eles desconsiderando o flag
c = 0 # contador
s = 0 # soma
flag = 999
n = 1
while n != flag:
    n = int(input('\033[34mDigite um número inteiro: \033[m'))
    print('\033[1;32;40m Para sair digite 999 \033[m')
    if n != 999:
        c += 1
        s += n
print('\033[31mForam digitados {} números\033[m'.format(c))
print('\033[1;33mA soma de todos os números digitados é {}\033[m'.format(s))

