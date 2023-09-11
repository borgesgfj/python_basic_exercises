#Analisador de triângulo 2.0; além de dizer se 3 segmentos formam um triângulo dizer se ele é
#equilatero; isóceles, escaleno
print('=-'*20)
print('Analisador de triângulos 2.0')
print('=-'*20)
a = float(input('Valor do primeiro segmento de reta: '))
b = float(input('Valor do segundo segmento de reta: '))
c: float = float(input('Valor do terceiro segmento de reta: '))
if (a+b) > c and (a+c) > b and (b+c) > a:
    #Se formam um triângulo vamos agora analisar o tipo.
    if a == b and a == c: #logo c==b, pois a==b! O phyton (esse lindo) aceita colocar a == b == c
        tipo = 'EQUILÁTERO'
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        tipo = 'ISÓCELES'
    else:
        tipo = 'ESCALENO'
    print('Os três segmentos de reta formam um triângulo \033[1;4;34m{}\033[m'.format(tipo))
else:
    print('\033[1;31m Os três segmentos de reta não formam um triângulo\033[m')


