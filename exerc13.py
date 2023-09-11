#Calcula o salário de uma pessoa com 15% de aumento
s=float(input('Qual o seu salário atual (sem aumento)? '))
sa=s+s*(15/100) #calcula o salário com 15% de aumento
print('O seu salário com 15% de aumento é: R$ {:.2f}'.format(sa))