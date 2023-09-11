#um programa que leia um ângulo e mostre o seu seno, cosseno e tangente
from math import sin,cos,tan,radians
ang=float(input('Digite um ângulo em graus '))
print('Para um ângulo de {}º'.format(ang))
print('_'*30)
print(' sen({}º) = {:.2f} \n cos({}º) = {:.2f} \n tan({}º) = {:.2f}'.format(ang, sin(radians(ang)), ang, cos(radians(ang)), ang, tan(radians(ang))))
print('_'*30)