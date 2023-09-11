#Dado os catetos de um triângulo calcular sua hipotenusa.
from math import hypot
co= float(input('Digite o valor do cateto oposto '))
ca= float(input('Digite o valor do cateto adjacente '))
print('Se o cateto oposto vale {} e o cateto adjacente vale {} \n a hipotenusa do triângulo é {:.2f}:'.format(co, ca, hypot(co,ca)))
