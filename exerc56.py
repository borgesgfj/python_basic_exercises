# desenvolver um programa que leia nome, idade e sexo de 4 pessoas e no final mostre:
# A média de idade do grupo; qual é o homem mais velho; qauntas mulheres tem menos de 20 anos
nomes_h = []
nomes_m = []
idade_h = []
idade_m = []
for i in range(1, 5):
    sexo = str(input('Sexo [masculino/(m); feminino/(f)]: ')).strip().lower()
    if sexo == 'm':
        nomes_h.append(str(input('Qual seu nome? ')).strip())
        idade_h.append(int(input('Qual sua idade? ')))
        print('\033[1;35m -\033[m'*20)
    else:
        nomes_m.append(str(input('Qual seu nome? ')).strip())
        a = idade_m.append(int(input('Qual sua idade? ')))
        print('\033[1;35m -\033[m' * 20)
# calcular a média de idades do grupo.
sm = 0 # soma da idade das mulheres
sh = 0 # soma da idade dos homens.
contador_m = 0
# soma da idade das mulheres e contador de quantas tem menos de 20 anos e índice da maior idade entre homens:
# o índice da maior idade entre os homens será usado para imprimir o nome do homem mais velho.
for x in idade_m:
    sm += x # soma das idades das mulheres
    if x < 20:
        contador_m +=1
# soma da idade dos homens:
for j in idade_h:
    sh += j
    maior_idade_h = idade_h.index(max(idade_h))
#calcular a média:
média = (sm+sh)/4
print('\033[1;31mA média de idade do grupo é de {} anos\033[m'.format(média))
print('\033[1;32mO homem mais velho do grupo é o {}\033[m'.format(nomes_h[maior_idade_h]))
print('\033[1;34m{} mulheres tem menos de 20 anos\033[m'.format(contador_m))






