# Programa que recebe um valor em metros e converta ele para centímetros e milímetros
m=float(input('Digite o valor em metros '))
mm=m*10**(3)
cm=m*10**(2)
print('{} metros é igual a {} milímetros ou {} centímetros'.format(m, mm, cm))

