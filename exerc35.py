#Um programa que determina se três segmentos de reta forma um triângulo.
#A condição para existencia do triângulo é: Se a soma das medidas de dois lados é maior que
#o terceiro lado, então o triangulo pode existir
a=float(input('Digite o comprimento do segmento de reta a: '))
b=float(input('Digite o comprimento do segmento de reta b: '))
c=float(input('Digite o comprimento do segmento de reta c: '))
if (a+b) > c and (b+c) > a and (a+c) > b:
    print('\033[1;32mEsses três segmentos de reta podem formar um triângulo!\033[m')
else:
    print('\033[1;31mEsses três segmentos de reta não formam um triângulo.\033[m')