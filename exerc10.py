# Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos doláres
#ela pode comprar.
r=float(input('Quanto dinheiro você possui em reais? '))
d=r/5.27
print('Com R$ {} você pode compar {:.2f} doláres!'.format(r, d))
