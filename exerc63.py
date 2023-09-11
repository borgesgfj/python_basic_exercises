# Ler um número inteiro n e mostar os n primeiros termos de uma sequência de Fibonacci.
F1 = 0
F2 = 1
c = 3
print('\033[1;31m~\033[m'*50)
print('{: ^50}'.format('\033[1;32;40m Cálculadora de Sequência de Fibonacci \033[m'))
print('\033[1;31m~\033[m'*50)
n = int(input('\033[1;34mQuantos termos deseja: \033[m')) # vai determinar quantos termos mostrar.
print('\033[1;31mOs {} primeiros termos da Sequência de Fibonacci são:\033[m'.format(n))
print('\033[35m{}\033[m \033[1;31m\u2192\033[m \033[35m{}\033[m'.format(F1, F2), end=' \033[1;31m\u2192\033[m ')
while c <= n:
    Fn = F1 + F2
    print('\033[35m{}\033[m'.format(Fn), end=' \033[1;31m\u2192\033[m ')
    F1 = F2 # Isso faz o F(n-2)
    F2 = Fn # Isso faz o F(n-1)
    c += 1
print('FIM')


