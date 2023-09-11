# Um programa que leia um número e mostre na tela a sua tabuada.
n = int(input('Digite um número inteiro entre 1 e 9 '))
#n1=n*1
#n2=n*2
#n3=n*3
#n4=n*4
#n5=n*5
#n6=n*6
#n7=n*7
#n8=n*8
#n9=n*9
print('_'*20)
print('A tabuada do {} é: '.format(n))
print('{} x {:2} = {} '.format(n, 1, n*1))
print('{} x {:2} = {} '.format(n, 2, n*2))
print('{} x {:2} = {} '.format(n, 3, n*3))
print('{} x {:2} = {} '.format(n, 4, n*4))
print('{} x {:2} = {} '.format(n, 5, n*5))
print('{} x {:2} = {} '.format(n, 6, n*6))
print('{} x {:2} = {} '.format(n, 7, n*7))
print('{} x {:2} = {} '.format(n, 8, n*8))
print('{} x {:2} = {} '.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
print('_'*20)