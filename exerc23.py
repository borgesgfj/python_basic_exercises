#Digitar um número de 0 à 9999 mostrando na tela a unidade, dezena, centena e milhar
# Se for fazer com string sem usar um laço não dá certo. Pq seria digitar um numero (num) e perdir
# para mostrar os n-essimo elemento da string: num[n] (n=0,1,2,3). Se o número digitado tiver menos
#do que 4 algarismos vai dar um erro.
# O melhor caminho é usar a variavel como um inteiro
num=int(input('Digite um número entre 0 e 9999 '))
u=(num//1)%10
d=(num//10) %10
c=(num//100) % 10
m=(num//1000) % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {} '.format(d))
print('Centena: {} '.format(c))
print('Milhar: {} '.format(m))