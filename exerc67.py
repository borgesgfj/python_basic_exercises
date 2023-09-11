# leia a Tabuada de vários números e o programa será interrompido quando o valor digitado for negativo
print('{:^100}'.format('\033[1;35;107;7m Cáclculadora de tabuada \033[m'))
print('')
while True:
    n = int(input('\033[31mQuer saber a tabuada de qual valor? (Valor negativo para sair) \033[m'))
    print('\033[1;35m~~\033[m' * 40)
    if n < 0:
        break
    for c in range(1, 11):
        prod = n * c # não é necessário pq posso colocar essa conta dentro da f string.
        print(f'\033[1;32m{n} x {c:2} =\033[m \033[1;31m {prod:2}\033[m')
    print('\033[1;35m~~\033[m' * 40)
print('\033[1;32;107m Programa Cálculadora de tabuada encerrado. Obrigado! \033[m')