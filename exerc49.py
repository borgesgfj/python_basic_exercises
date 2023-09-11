#Tabuada de um número
print('\033[1;32m*-*\033[m'*15)
print(' '*9,'\033[1;97;41mCalculadora de tabuada\033[m')
print('\033[1;32m*-*\033[m'*15)

n = int(input('Digite um número para saber a sua tabuada '))
print('\033[1;33m--\033[m'*15)
print(' '*5,'\033[1;97;42m Tabuada do {} \033[m'.format(n))
print('\033[1;33m--\033[m'*15)
for c in range(1, 11):
    print('\033[1;34m{} x {:2} =\033[m \033[1;31m{:2}\033[m'.format(n, c, n*c))
