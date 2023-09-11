# desenvolver um programa que leia nome, idade e sexo de 4 pessoas e no final mostre:
# A média de idade do grupo; qual é o homem mais velho; quantas mulheres tem menos de 20 anos
# dessa vez vou fazer sem usar lista.
#inicializando as variáveis para alocar espaço!
soma_idades = 0
contador_m = 0
maior_idade_h = 0
h_mais_velho = ''
for c in range(1,5):
    print('\033[1;35m{:-^50}\033[m'.format(' Nome da {}ª pessoa '.format(c)))
    nome = input('Nome da pessoa: ')
    idade_pessoa = int(input('Idade da pessoa: '))
    sexo = str(input('Sexo [M/F] ')).strip().upper()
    soma_idades += idade_pessoa
    if sexo == 'F' and idade_pessoa < 20:
        contador_m +=1
    if sexo == 'M':
        if maior_idade_h == 0: # significa que está se tratando do 1º homem da lista!
            maior_idade_h = idade_pessoa
            h_mais_velho = nome
        else:
            if idade_pessoa > maior_idade_h:
                maior_idade_h = idade_pessoa
                h_mais_velho = nome

média_idade = soma_idades/4

print('\033[1;31mA média de idade do grupo é de {} anos\033[m'.format(média_idade))
if h_mais_velho =='':
    print('\033[1;31mNão tem homens no grupo')
else:
    print('\033[1;32mO homem mais velho do grupo é o {} com {} anos \033[m'.format(h_mais_velho, maior_idade_h))
print('\033[1;34m{} mulheres tem menos de 20 anos\033[m'.format(contador_m))


