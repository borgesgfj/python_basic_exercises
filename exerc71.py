# Programa que simula o funcionamento de um caixa eletrônico. Pergunta o valor a ser sacado e informar
# quantas cédulas de cada valor serão entregues (cédulas de 50; 20; 10; 1)
print('\033[1;35m~-~\033[m'*30)
print('\033[1;91;103m{: ^90}\033[m'.format(' Banco do Gil '))
print('\033[1;35m~-~\033[m'*30)
valor = int(input('Qual valor deseja sacar? R$'))
c = 0
x = valor
while True:
    c += 1
    if c == 1:
        notas_50 = x // 50
        resto = x % 50
        x = resto
        if notas_50 != 0:
            print(f'\033[1;34mTotal de {notas_50} cédulas de R$50\033[m')
    elif c == 2:
        notas_20 = x // 20
        resto = x % 20
        x = resto
        if notas_20 != 0:
            print(f'\033[1;34mTotal de {notas_20} cédulas de R$20\033[m')
    elif c == 3:
        notas_10 = x // 10
        resto = x % 10
        x = resto
        if notas_10 != 0:
            print(f'\033[1;34mTotal de {notas_10} cédulas de R$10\033[m')
    elif c == 4:
        notas_1 = x // 1
        resto = x % 1
        print(f'\033[1;34mTotal de {notas_1} cédulas de R$1\033[m')
    if resto == 0:
        break
print('\033[1;35m~-~\033[m'*30)
print('\033[1;97;41m Volte sempre ao Banco do Gil! Tenha um bom dia! \033[m')








