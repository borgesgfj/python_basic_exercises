#calcular o aumento de salário, se inferior a R$1250,00 aumento de 15%, se superior a 1250,00 aumento
#de 10%
sal=float(input('Qual seu salário atual? '))
if sal > 1250:
    novo = sal + (sal*0.1)
    print('Seu salário atual é R$ {:.2f}, você receberá um aumento de 10%.'.format(sal))
else:
    print('Seu salário atual é R$ {:.2f}, você receberá um aumento de 15%.'.format(sal))
    novo = sal +(sal*0.15)
print('Seu novo salário com aumento será: R$ {:.2f}.'.format(novo))