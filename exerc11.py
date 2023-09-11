#Programa que entra com a altura e a largura de uma parede, calcula sua área e a quantidade de
#tinta necessária para pintá-la. Dado: 1 litro de tinta pinta 2m²
print('Vamos calcular a quantidade de tinta necessária para pintar uma parede')
a = float(input('Qual a altura da parede em metros? '))
l = float(input('Qual a largura da parede em metros? '))
area = a*l # calcula a área da parede
qt = area/2 #calcula a quantidade de tinta necessária
print('A área desta parede é {:.2f}m²'.format(area))
print('Para pintar esta parede você precisará de {:.2f} litros de tinta.'.format(qt))
