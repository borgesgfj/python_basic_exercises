#Programa para aprovar um empréstimo bancário.
# Ler o valor do imóvel, o salário da pessoa, quantos anos será o pagamento
#mostrar o valor da prestação, e se esse valor exceder 30% do salario negar o empréstimo.
print('\033[1;97;40m=*'*20,'Banco do Gil','=*'*20,'\033[m')

valor=float(input('Qual o valor do imóvel a ser financiado? R$')) #Lê o valor do imóvel
salario = float(input('Qual o seu rendimento mensal? R$')) #Lê o salário da pessoa
anos  = int(input('Em quantos anos deseja pagar o empréstimo? '))
prest = valor / (anos*12) # calcula o valor das prestações
print('\033[1;30;102mO valor total do empréstimo será R${:.2f}, dividido em {} prestações mensais de R${:.2f}\033[m'.format(valor, (anos*12), prest))
if prest <= (salario*0.3):
    print('\033[1;104;30mO seu empréstimo pode ser aprovado. Parabéns!\033[m')
else:
    print('\033[1;40;91mInfelizmente o valor das prestações não é compatível com seu rendimento mensal.\033[m')
    print('\033[1;31mSeu empréstimo não será aprovado.\033[m')
